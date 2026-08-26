import streamlit as st
from streamlit_mic_recorder import speech_to_text


def initialise_voice_interview(questions):
    """
    Initialise or reset the voice interview session.
    """

    if "voice_questions" not in st.session_state:
        st.session_state.voice_questions = questions

    if "voice_question_index" not in st.session_state:
        st.session_state.voice_question_index = 0

    if "voice_answers" not in st.session_state:
        st.session_state.voice_answers = []

    if "voice_interview_complete" not in st.session_state:
        st.session_state.voice_interview_complete = False


def reset_voice_interview(questions):
    """
    Clear the current interview and start again.
    """

    st.session_state.voice_questions = questions
    st.session_state.voice_question_index = 0
    st.session_state.voice_answers = []
    st.session_state.voice_interview_complete = False
    st.session_state.voice_current_transcript = ""

    st.rerun()


def save_voice_answer(question, answer):
    """
    Save one question and its transcript.
    """

    clean_answer = answer.strip()

    if not clean_answer:
        return False

    question_number = st.session_state.voice_question_index + 1

    answer_record = {
        "question_number": question_number,
        "question": question,
        "answer": clean_answer
    }

    existing_numbers = [
        item["question_number"]
        for item in st.session_state.voice_answers
    ]

    if question_number in existing_numbers:
        for index, item in enumerate(st.session_state.voice_answers):
            if item["question_number"] == question_number:
                st.session_state.voice_answers[index] = answer_record
                break
    else:
        st.session_state.voice_answers.append(answer_record)

    return True


def render_voice_interview(questions):
    """
    Render a deterministic voice interview in Streamlit.
    """

    if not questions:
        st.info(
            "Generate the resume-based interview questions before "
            "starting the voice interview."
        )
        return

    initialise_voice_interview(questions)

    if st.session_state.voice_questions != questions:
        reset_voice_interview(questions)

    total_questions = len(st.session_state.voice_questions)
    current_index = st.session_state.voice_question_index

    if st.session_state.voice_interview_complete:
        render_interview_summary()

        if st.button(
            "🔄 Start Interview Again",
            use_container_width=True
        ):
            reset_voice_interview(questions)

        return

    current_question = st.session_state.voice_questions[current_index]

    st.markdown("### 🎤 Candidate Voice Interview")

    st.caption(
        "The candidate can listen to the question, record an answer, "
        "review the transcript and then submit it."
    )

    progress_value = current_index / total_questions
    st.progress(progress_value)

    st.markdown(
        f"**Question {current_index + 1} of {total_questions}**"
    )

    st.info(current_question)

    st.markdown("#### 🔊 Listen to the question")

    speak_question(current_question, current_index)

    st.markdown("#### 🎙️ Record your answer")

    transcript = speech_to_text(
        language="en",
        start_prompt="🎙️ Start Recording",
        stop_prompt="⏹️ Stop Recording",
        just_once=True,
        use_container_width=True,
        key=f"voice_answer_{current_index}"
    )    

    if transcript:
        st.session_state.voice_current_transcript = transcript

    if "voice_current_transcript" not in st.session_state:
        st.session_state.voice_current_transcript = ""

    st.markdown("#### 📝 Review your transcript")

    reviewed_answer = st.text_area(
        "Correct any speech-recognition errors before submitting:",
        value=st.session_state.voice_current_transcript,
        height=140,
        key=f"reviewed_answer_{current_index}"
    )

    button_col1, button_col2, button_col3 = st.columns(3)

    with button_col1:
        if st.button(
            "💾 Save Answer",
            use_container_width=True
        ):
            if save_voice_answer(current_question, reviewed_answer):
                st.success("Answer saved successfully.")
            else:
                st.warning(
                    "Please record or enter an answer before saving."
                )

    with button_col2:
        if st.button(
            "➡️ Save & Next",
            use_container_width=True
        ):
            if save_voice_answer(current_question, reviewed_answer):
                if current_index < total_questions - 1:
                    st.session_state.voice_question_index += 1
                    st.session_state.voice_current_transcript = ""
                else:
                    st.session_state.voice_interview_complete = True

                st.rerun()
            else:
                st.warning(
                    "Please record or enter an answer before continuing."
                )

    with button_col3:
        if st.button(
            "🔄 Reset Interview",
            use_container_width=True
        ):
            reset_voice_interview(questions)

    if st.session_state.voice_answers:
        with st.expander("📋 Saved answers"):
            for item in st.session_state.voice_answers:
                st.markdown(
                    f"**Question {item['question_number']}**"
                )
                st.write(item["question"])
                st.markdown("**Candidate answer**")
                st.write(item["answer"])
                st.divider()


def speak_question(question, question_index):
    """
    Use the browser Speech Synthesis API to read the question aloud.

    This is deterministic text-to-speech and does not use an LLM.
    """

    safe_question = (
        question
        .replace("\\", "\\\\")
        .replace("`", "\\`")
        .replace("${", "\\${")
    )

    st.components.v1.html(
        f"""
        <div style="display:flex; gap:10px;">
            <button
                onclick="speakQuestion{question_index}()"
                style="
                    background:#0B5CAB;
                    color:white;
                    border:none;
                    padding:10px 18px;
                    border-radius:8px;
                    cursor:pointer;
                    font-weight:600;
                "
            >
                🔊 Play Question
            </button>

            <button
                onclick="stopQuestion{question_index}()"
                style="
                    background:#374151;
                    color:white;
                    border:none;
                    padding:10px 18px;
                    border-radius:8px;
                    cursor:pointer;
                    font-weight:600;
                "
            >
                ⏹ Stop
            </button>
        </div>

        <script>
            function speakQuestion{question_index}() {{
                window.speechSynthesis.cancel();

                const message = new SpeechSynthesisUtterance(
                    `{safe_question}`
                );

                message.lang = "en-GB";
                message.rate = 0.9;
                message.pitch = 1.0;
                message.volume = 1.0;

                window.speechSynthesis.speak(message);
            }}

            function stopQuestion{question_index}() {{
                window.speechSynthesis.cancel();
            }}
        </script>
        """,
        height=60
    )


def render_interview_summary():
    """
    Display the completed interview evidence.
    """

    st.success("✅ Voice interview completed")

    st.markdown("### 📋 Interview Transcript")

    answers = st.session_state.voice_answers

    if not answers:
        st.warning("No candidate answers were saved.")
        return

    for item in answers:
        with st.container(border=True):
            st.markdown(
                f"#### Question {item['question_number']}"
            )
            st.write(item["question"])

            st.markdown("**Candidate response**")
            st.write(item["answer"])

            word_count = len(item["answer"].split())

            st.caption(
                f"Response length: {word_count} words"
            )

    st.info(
        "This transcript is evidence for authorised human review. "
        "The system does not independently select or reject a candidate."
    )
