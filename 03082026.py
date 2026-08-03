
from utils.resume_parser import extract_resume_text
from utils.jd_matcher import calculate_match
from utils.evaluation_engine import evaluate_candidate
from utils.interview_engine import generate_questions
from utils.interview_engine import generate_questions
import streamlit as st

st.set_page_config(
    page_title="TalentCopilot AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 TalentCopilot AI")

st.markdown("---")

tab1, tab2, tab3 = st.tabs(
    [
        "📄 Resume Screening",
        "🎤 AI Interview",
        "📊 Executive Scorecard"
    ]
)

with tab1:

    st.header("📄 Resume Screening")

    uploaded_resume = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

    job_description = st.text_area(
        "Paste Job Description",
        height=250
    )

    if uploaded_resume:
        st.success(
            f"Resume Uploaded: {uploaded_resume.name}"
        )

    if st.button("Analyze Candidate"):

        if uploaded_resume and job_description:

            resume_text = extract_resume_text(
                uploaded_resume
            )

        score, matched_skills, missing_skills = calculate_match(
            resume_text,
            job_description
        )

        recommendation = evaluate_candidate(score)

        questions = generate_questions(
            matched_skills,
            missing_skills
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Match Score",
                f"{score}%"
            )

        with col2:
            st.metric(
                "Recommendation",
                recommendation
            )

        st.subheader("✅ Matched Skills")
        st.write(matched_skills)

        st.subheader("❌ Missing Skills")
        st.write(missing_skills)

        st.subheader("💪 Candidate Strengths")

        for skill in matched_skills:
            st.success(skill)

        st.subheader("⚠️ Skill Gaps")

        for skill in missing_skills:
            st.warning(skill)

        st.subheader("🎤 AI Interview Questions")
        for i, question in enumerate(questions, start=1):
            st.write(f"{i}. {question}")

        with st.expander(
                    "Resume Text"
                ):
            st.write(
                resume_text[:5000]
            )

    else:

        st.warning(
            "Upload Resume and Job Description"
        )


with tab2:

    st.header("🎤 AI Interview")

    st.info(
        "Interview Question Generator Coming Soon"
    )


with tab3:

    st.header("📊 Executive Scorecard")

    st.info(
        "Candidate Evaluation Dashboard Coming Soon"
    )