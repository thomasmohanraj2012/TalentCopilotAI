from html import escape
from textwrap import dedent

import streamlit as st

from engines.resume_engine import analyse_candidate
from utils.interview_engine import generate_questions
from utils.voice_interview import render_voice_interview


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="TalentCopilotAI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def render_html(content):
    """
    Render compact HTML without Streamlit Markdown
    interpreting indented tags as code blocks.
    """

    compact_html = " ".join(
        line.strip()
        for line in dedent(content).splitlines()
        if line.strip()
    )

    st.markdown(
        compact_html,
        unsafe_allow_html=True
    )

def render_section_header(eyebrow, title, description):
    """
    Render one consistent section heading.
    """
    render_html(
        f"""
        <div class="tc-section-heading">
            <div class="tc-eyebrow">
                {escape(eyebrow)}
            </div>

            <div class="tc-section-title">
                {escape(title)}
            </div>

            <div class="tc-section-description">
                {escape(description)}
            </div>
        </div>
        """
    )


def render_skill_pills(skills, pill_type="matched"):
    """
    Render capability pills.
    """
    if not skills:
        st.info("No capability categories were identified.")
        return

    pill_class = (
        "tc-pill tc-pill-matched"
        if pill_type == "matched"
        else "tc-pill tc-pill-gap"
    )

    icon = "✓" if pill_type == "matched" else "!"

    pills = "".join(
        [
            (
                f'<span class="{pill_class}">'
                f'{icon}&nbsp;&nbsp;{escape(str(skill))}'
                f'</span>'
            )
            for skill in skills
        ]
    )

    render_html(
        f"""
        <div class="tc-pill-container">
            {pills}
        </div>
        """
    )


def get_assessment_style(score):
    """
    Return assessment presentation properties.
    """
    if score >= 85:
        return {
            "colour": "#24D18F",
            "background": "rgba(36, 209, 143, 0.12)",
            "label": "Strong alignment",
            "next_step": (
                "Candidate demonstrates strong category-level alignment. "
                "Proceed with structured validation."
            )
        }

    if score >= 70:
        return {
            "colour": "#F5B942",
            "background": "rgba(245, 185, 66, 0.12)",
            "label": "Further validation recommended",
            "next_step": (
                "Candidate demonstrates partial alignment. "
                "Use the structured interview to validate key areas."
            )
        }

    return {
        "colour": "#FF6B7A",
        "background": "rgba(255, 107, 122, 0.12)",
        "label": "Key requirements need validation",
        "next_step": (
            "Several category-level gaps were identified. "
            "Review the evidence before determining the next step."
        )
    }


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "analysis_complete": False,
    "questions": [],
    "score": 0,
    "matched_skills": [],
    "missing_skills": [],
    "recommendation": "",
    "resume_text": "",
    "candidate_file": ""
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# GLOBAL CSS
# =========================================================

render_html(
    """
    <style>

    /* ============================================
       BASE APPLICATION
       ============================================ */

    [data-testid="stHeader"] {
        display: none;
    }

    [data-testid="stToolbar"] {
        display: none;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 92% 8%,
                rgba(42, 159, 214, 0.15),
                transparent 27%
            ),
            radial-gradient(
                circle at 8% 92%,
                rgba(29, 78, 216, 0.14),
                transparent 32%
            ),
            linear-gradient(
                145deg,
                #04182F 0%,
                #082A50 50%,
                #103E70 100%
            );

        color: #FFFFFF;
    }

    .block-container {
        max-width: 1280px;
        padding-top: 1rem;
        padding-bottom: 3rem;
    }

    html,
    body,
    [class*="css"] {
        font-family:
            "Segoe UI",
            "Aptos",
            "Inter",
            sans-serif;
    }

    h1,
    h2,
    h3,
    h4,
    h5 {
        color: #FFFFFF !important;
    }

    p,
    label {
        color: #D7E6F5;
    }


    /* ============================================
       APPLICATION HERO
       ============================================ */

    .tc-hero {
        background:
            linear-gradient(
                125deg,
                rgba(8, 41, 83, 0.96),
                rgba(11, 92, 171, 0.92),
                rgba(8, 127, 165, 0.86)
            );

        border: 1px solid rgba(125, 224, 255, 0.35);
        border-radius: 20px;
        padding: 24px 30px;
        margin-bottom: 18px;
        box-shadow: 0 16px 38px rgba(0, 0, 0, 0.24);
        position: relative;
        overflow: hidden;
    }

    .tc-hero::after {
        content: "";
        position: absolute;
        width: 240px;
        height: 240px;
        right: -70px;
        top: -100px;
        border-radius: 50%;
        background: rgba(125, 224, 255, 0.10);
    }

    .tc-hero-eyebrow {
        color: #7DE0FF;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 3px;
        text-transform: uppercase;
    }

    .tc-hero-title {
        color: #FFFFFF;
        font-size: 18px;
        font-weight: 700;
        line-height: 1.15;
        margin-top: 7px;
    }

    .tc-hero-subtitle {
        color: #D9ECF8;
        font-size: 14px;
        line-height: 1.5;
        margin-top: 8px;
    }

    .tc-hero-badge {
        display: inline-block;
        margin-top: 14px;
        padding: 6px 12px;
        color: #FFFFFF;
        background: rgba(255, 255, 255, 0.13);
        border: 1px solid rgba(255, 255, 255, 0.23);
        border-radius: 20px;
        font-size: 10px;
        font-weight: 750;
        letter-spacing: 0.8px;
    }


    /* ============================================
       NAVIGATION
       ============================================ */

    .stTabs [data-baseweb="tab-list"] {
        background: rgba(3, 24, 48, 0.64);
        border: 1px solid rgba(88, 211, 255, 0.18);
        border-radius: 14px;
        padding: 5px;
        gap: 5px;
        margin-bottom: 15px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 43px;
        padding: 0 19px;
        border-radius: 10px;
        color: #AFC4DE !important;
        font-size: 14px;
        font-weight: 700;
        background: transparent;
    }

    .stTabs [aria-selected="true"] {
        color: #FFFFFF !important;
        background:
            linear-gradient(
                135deg,
                rgba(11, 92, 171, 0.90),
                rgba(32, 136, 190, 0.88)
            ) !important;
    }


    /* ============================================
       INPUT PANEL
       ============================================ */

    .tc-input-heading {
        margin-bottom: 9px;
    }

    .tc-input-label {
        color: #FFFFFF;
        font-size: 15px;
        font-weight: 750;
    }

    .tc-input-hint {
        color: #9FC1E1;
        font-size: 11px;
        margin-top: 3px;
    }

    [data-testid="stFileUploader"] {
        width: 100%;
        max-width: none !important;
        padding: 6px;
        background: rgba(8, 41, 83, 0.72);
        border: 1px solid rgba(88, 211, 255, 0.25);
        border-radius: 13px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
    }

    [data-testid="stFileUploaderDropzone"] {
        min-height: 92px !important;
        background: rgba(13, 55, 98, 0.68) !important;
        border: 1px dashed rgba(125, 224, 255, 0.62) !important;
        border-radius: 10px !important;
    }

    [data-testid="stFileUploaderDropzoneInstructions"] {
        display: none !important;
    }

    [data-testid="stFileUploader"] button {
        background: #58D3FF !important;
        color: #04182F !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 800 !important;
        padding: 8px 18px !important;
    }

    .stTextArea textarea {
        min-height: 105px !important;
        background: rgba(245, 249, 252, 0.98) !important;
        color: #102A43 !important;
        border: 1px solid #A9C7DB !important;
        border-radius: 13px !important;
        font-size: 14px !important;
        line-height: 1.5 !important;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
    }

    .stTextArea textarea:focus {
        border-color: #58D3FF !important;
        box-shadow: 0 0 0 3px rgba(88, 211, 255, 0.18) !important;
    }

    .stTextArea textarea::placeholder {
        color: #6F879B !important;
        opacity: 1 !important;
    }


    /* ============================================
       BUTTONS
       ============================================ */

    .stButton button {
        min-height: 46px;
        background:
            linear-gradient(
                135deg,
                #37BFED,
                #168FCC
            ) !important;

        color: #FFFFFF !important;
        border: none !important;
        border-radius: 11px !important;
        font-size: 14px !important;
        font-weight: 800 !important;
        box-shadow: 0 9px 22px rgba(0, 0, 0, 0.18);
        transition:
            transform 0.15s ease,
            box-shadow 0.15s ease;
    }

    .stButton button:hover {
        transform: translateY(-1px);
        box-shadow: 0 12px 26px rgba(0, 0, 0, 0.24);
    }


    /* ============================================
       SECTION HEADINGS
       ============================================ */

    .tc-section-heading {
        margin-top: 23px;
        margin-bottom: 14px;
    }

    .tc-eyebrow {
        color: #58D3FF;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 2px;
    }

    .tc-section-title {
        color: #FFFFFF;
        font-size: 25px;
        font-weight: 800;
        margin-top: 4px;
    }

    .tc-section-description {
        color: #AFC4DE;
        font-size: 12px;
        margin-top: 5px;
    }


    /* ============================================
       ASSESSMENT HERO
       ============================================ */

    .tc-assessment-hero {
        border-radius: 20px;
        padding: 28px;
        text-align: center;
        margin: 14px 0 20px 0;
        box-shadow: 0 14px 32px rgba(0, 0, 0, 0.22);
    }

    .tc-assessment-label {
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 2px;
    }

    .tc-assessment-score {
        color: #FFFFFF;
        font-size: 64px;
        font-weight: 850;
        line-height: 1;
        margin-top: 10px;
    }

    .tc-assessment-result {
        color: #FFFFFF;
        font-size: 21px;
        font-weight: 800;
        margin-top: 10px;
    }

    .tc-assessment-next {
        color: #D9ECF8;
        font-size: 12px;
        margin-top: 7px;
    }


    /* ============================================
       METRIC CARDS
       ============================================ */

    [data-testid="stMetric"] {
        min-height: 112px;
        padding: 18px !important;
        background: rgba(8, 41, 83, 0.74) !important;
        border: 1px solid rgba(88, 211, 255, 0.24) !important;
        border-radius: 14px !important;
        box-shadow: 0 9px 22px rgba(0, 0, 0, 0.14);
    }

    [data-testid="stMetricLabel"] {
        color: #9FC1E1 !important;
        font-size: 10px !important;
        font-weight: 800 !important;
        letter-spacing: 0.8px;
        text-transform: uppercase;
    }

    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-size: 26px !important;
        font-weight: 850 !important;
    }


    /* ============================================
       SKILL PILLS
       ============================================ */

    .tc-pill-container {
        display: flex;
        flex-wrap: wrap;
        gap: 9px;
        margin-bottom: 14px;
    }

    .tc-pill {
        display: inline-block;
        padding: 8px 13px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
    }

    .tc-pill-matched {
        color: #BDF9DC;
        background: rgba(36, 209, 143, 0.13);
        border: 1px solid rgba(36, 209, 143, 0.55);
    }

    .tc-pill-gap {
        color: #FFE1A0;
        background: rgba(245, 185, 66, 0.13);
        border: 1px solid rgba(245, 185, 66, 0.55);
    }


    /* ============================================
       QUESTION CARDS
       ============================================ */

    .tc-question-card {
        background:
            linear-gradient(
                135deg,
                rgba(8, 41, 83, 0.82),
                rgba(13, 55, 98, 0.72)
            );

        border: 1px solid rgba(88, 211, 255, 0.20);
        border-left: 4px solid #58D3FF;
        border-radius: 13px;
        padding: 15px 17px;
        margin-bottom: 10px;
        box-shadow: 0 7px 18px rgba(0, 0, 0, 0.12);
    }

    .tc-question-number {
        color: #58D3FF;
        font-size: 10px;
        font-weight: 850;
        letter-spacing: 1.3px;
    }

    .tc-question-text {
        color: #FFFFFF;
        font-size: 14px;
        font-weight: 500;
        line-height: 1.5;
        margin-top: 6px;
    }


    /* ============================================
       EXECUTIVE INSIGHTS
       ============================================ */

    .tc-executive-card {
        display: grid;
        grid-template-columns: 0.9fr 1.5fr;
        gap: 20px;
        background: rgba(8, 41, 83, 0.76);
        border: 1px solid rgba(88, 211, 255, 0.25);
        border-radius: 18px;
        padding: 23px;
        margin-bottom: 20px;
        box-shadow: 0 14px 32px rgba(0, 0, 0, 0.18);
    }

    .tc-executive-score {
        border-radius: 14px;
        padding: 20px;
        text-align: center;
    }

    .tc-executive-score-label {
        color: #AFC4DE;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 1.5px;
    }

    .tc-executive-score-value {
        color: #FFFFFF;
        font-size: 54px;
        font-weight: 850;
        line-height: 1;
        margin-top: 10px;
    }

    .tc-executive-title {
        color: #FFFFFF;
        font-size: 23px;
        font-weight: 800;
    }

    .tc-executive-description {
        color: #BFD9F5;
        font-size: 13px;
        line-height: 1.55;
        margin-top: 9px;
    }

    .tc-review-badge {
        display: inline-block;
        color: #7DE0FF;
        background: rgba(88, 211, 255, 0.12);
        border: 1px solid rgba(88, 211, 255, 0.35);
        border-radius: 20px;
        margin-top: 14px;
        padding: 6px 11px;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 0.8px;
    }


    /* ============================================
       OTHER COMPONENTS
       ============================================ */

    [data-testid="stProgress"] > div > div {
        background:
            linear-gradient(
                90deg,
                #0B5CAB,
                #58D3FF
            ) !important;
    }

    [data-testid="stExpander"] {
        background: rgba(8, 41, 83, 0.68);
        border: 1px solid rgba(88, 211, 255, 0.20);
        border-radius: 12px;
    }

    [data-testid="stAlert"] {
        border-radius: 11px;
    }

    hr {
        border-color: rgba(88, 211, 255, 0.15);
    }


    /* ============================================
       RESPONSIVE VIEW
       ============================================ */

    @media only screen and (max-width: 800px) {

        .tc-hero-title {
            font-size: 24px;
        }

        .tc-assessment-score {
            font-size: 50px;
        }

        .tc-executive-card {
            grid-template-columns: 1fr;
        }

        .block-container {
            padding-left: 0.8rem;
            padding-right: 0.8rem;
        }
    }

    </style>
    """
)


# =========================================================
# GLOBAL HERO
# =========================================================

render_html(
    """
    <div class="tc-hero">

        <div class="tc-hero-eyebrow">
            TALENTCOPILOTAI
        </div>

        <div class="tc-hero-title">
            🤖 திறனறிவு AI
        </div>

        <div style="
            color:#7DE0FF;
            font-size:16px;
            font-weight:700;
            margin-top:4px;
        ">
            by COMCAST
        </div>

        <div class="tc-hero-subtitle">
            Enterprise Talent Intelligence Platform
        </div>

        <div style="
            color:#D9ECF8;
            font-size:13px;
            margin-top:8px;
        ">
            AI Resume Screening • Interview Intelligence • Executive Hiring Insights
        </div>

        <div class="tc-hero-badge">
            RECRUITMENT INTELLIGENCE PROOF OF CONCEPT
        </div>

    </div>
    """
)


# =========================================================
# MAIN NAVIGATION
# =========================================================

tab1, tab2, tab3 = st.tabs(
    [
        "📄 Resume Intelligence",
        "🎤 AI Interview",
        "📊 Executive Insights"
    ]
)


# =========================================================
# TAB 1: RESUME INTELLIGENCE
# =========================================================

with tab1:

    render_section_header(
        "CANDIDATE INPUT",
        "Resume Intelligence",
        (
            "Compare a candidate resume with the target role and "
            "generate structured interview evidence."
        )
    )

    left_col, right_col = st.columns(
        [1, 2],
        gap="large"
    )

    with left_col:

        render_html(
            """
            <div class="tc-input-heading">
                <div class="tc-input-label">
                    📄 Candidate Resume
                </div>

                <div class="tc-input-hint">
                    Upload a PDF or DOCX resume
                </div>
            </div>
            """
        )

        uploaded_resume = st.file_uploader(
            "Candidate Resume",
            type=["pdf", "docx"],
            label_visibility="collapsed"
        )

        if uploaded_resume:
            st.success(
                f"Resume ready: {uploaded_resume.name}"
            )

    with right_col:

        render_html(
            """
            <div class="tc-input-heading">
                <div class="tc-input-label">
                    📋 Target Job Description
                </div>

                <div class="tc-input-hint">
                    Add the role requirements used for comparison
                </div>
            </div>
            """
        )

        job_description = st.text_area(
            "Target Job Description",
            height=105,
            label_visibility="collapsed",
            placeholder="Paste the target job description here..."
        )

    analyse_clicked = st.button(
        "🚀 Analyse Candidate",
        use_container_width=True,
        type="primary"
    )

    if analyse_clicked:

        if not uploaded_resume or not job_description.strip():
            st.warning(
                "Upload a resume and enter the target job description."
            )

        else:
            with st.spinner(
                "Analysing candidate alignment and preparing interview questions..."
            ):
                analysis = analyse_candidate(
                    uploaded_resume,
                    job_description
                )

                score = analysis["score"]
                matched_skills = analysis["matched_skills"]
                missing_skills = analysis["missing_skills"]
                recommendation = analysis["recommendation"]
                resume_text = analysis["resume_text"]

                questions = generate_questions(
                    matched_skills,
                    missing_skills,
                    resume_text,
                    job_description
                )

                st.session_state["questions"] = questions
                st.session_state["score"] = score
                st.session_state["matched_skills"] = matched_skills
                st.session_state["missing_skills"] = missing_skills
                st.session_state["recommendation"] = recommendation
                st.session_state["resume_text"] = resume_text
                st.session_state["candidate_file"] = uploaded_resume.name
                st.session_state["analysis_complete"] = True

    # Results remain visible after Streamlit reruns.
    if st.session_state.get("analysis_complete"):

        score = st.session_state["score"]
        matched_skills = st.session_state["matched_skills"]
        missing_skills = st.session_state["missing_skills"]
        recommendation = st.session_state["recommendation"]
        resume_text = st.session_state["resume_text"]
        questions = st.session_state["questions"]

        assessment = get_assessment_style(score)

        render_section_header(
            "CANDIDATE INTELLIGENCE",
            "Candidate Fit Overview",
            (
                "Category-level resume alignment and areas requiring "
                "interviewer validation."
            )
        )

        render_html(
            f"""
            <div
                class="tc-assessment-hero"
                style="
                    background:
                        linear-gradient(
                            135deg,
                            {assessment["background"]},
                            rgba(8, 41, 83, 0.92)
                        );

                    border:
                        1px solid
                        {assessment["colour"]};
                "
            >

                <div
                    class="tc-assessment-label"
                    style="color:{assessment["colour"]};"
                >
                    CANDIDATE ASSESSMENT
                </div>

                <div class="tc-assessment-score">
                    {score}%
                </div>

                <div class="tc-assessment-result">
                    {escape(str(recommendation))}
                </div>

                <div class="tc-assessment-next">
                    {escape(assessment["next_step"])}
                </div>

            </div>
            """
        )

        metric1, metric2, metric3, metric4 = st.columns(4)

        with metric1:
            st.metric(
                "Match Score",
                f"{score}%"
            )

        with metric2:
            st.metric(
                "Matched Skills",
                len(matched_skills)
            )

        with metric3:
            st.metric(
                "Validation Areas",
                len(missing_skills)
            )

        with metric4:
            st.metric(
                "Assessment",
                assessment["label"]
            )

        st.progress(
            min(max(float(score) / 100, 0.0), 1.0)
        )

        skill_col, gap_col = st.columns(
            2,
            gap="large"
        )

        with skill_col:

            render_section_header(
                "ROLE ALIGNMENT",
                "Matched Capabilities",
                "Capability categories identified in both the resume and role."
            )

            render_skill_pills(
                matched_skills,
                "matched"
            )

        with gap_col:

            render_section_header(
                "INTERVIEW FOCUS",
                "Validation Areas",
                "Role capability categories not identified in the resume."
            )

            render_skill_pills(
                missing_skills,
                "gap"
            )

        render_section_header(
            "STRUCTURED INTERVIEW",
            "Recommended Interview Questions",
            (
                "Selected from resume evidence, role requirements, "
                "identified gaps and behavioural question pools."
            )
        )

        if questions:
            for index, question in enumerate(
                questions,
                start=1
            ):
                safe_question = escape(
                    str(question)
                )

                render_html(
                    f"""
                    <div class="tc-question-card">

                        <div class="tc-question-number">
                            QUESTION {index:02d}
                        </div>

                        <div class="tc-question-text">
                            {safe_question}
                        </div>

                    </div>
                    """
                )

        else:
            st.info(
                "No interview questions were generated."
            )

        with st.expander(
            "📄 View Extracted Resume Evidence"
        ):
            st.text(
                resume_text[:5000]
            )


# =========================================================
# TAB 2: AI INTERVIEW
# =========================================================

with tab2:

    render_section_header(
        "INTERVIEW INTELLIGENCE",
        "Structured AI Interview",
        (
            "Present one question at a time, capture the candidate "
            "response and retain transcript evidence for human review."
        )
    )

    if st.session_state.get("questions"):

        render_voice_interview(
            st.session_state["questions"]
        )

    else:
        st.info(
            "Analyse a candidate in Resume Intelligence before "
            "starting the structured interview."
        )


# =========================================================
# TAB 3: EXECUTIVE INSIGHTS
# =========================================================

with tab3:

    render_section_header(
        "DECISION SUPPORT",
        "Executive Insights",
        (
            "A concise view of candidate alignment, identified "
            "capabilities and validation areas."
        )
    )

    if not st.session_state.get("analysis_complete"):

        st.info(
            "Analyse a candidate to populate Executive Insights."
        )

    else:

        score = st.session_state["score"]
        matched_skills = st.session_state["matched_skills"]
        missing_skills = st.session_state["missing_skills"]
        recommendation = st.session_state["recommendation"]
        candidate_file = st.session_state.get(
            "candidate_file",
            "Candidate resume"
        )

        assessment = get_assessment_style(score)

        render_html(
            f"""
            <div class="tc-executive-card">

                <div
                    class="tc-executive-score"
                    style="
                        background:{assessment["background"]};
                        border:
                            1px solid
                            {assessment["colour"]};
                    "
                >

                    <div class="tc-executive-score-label">
                        CANDIDATE FIT
                    </div>

                    <div class="tc-executive-score-value">
                        {score}%
                    </div>

                    <div
                        style="
                            color:{assessment["colour"]};
                            font-size:13px;
                            font-weight:800;
                            margin-top:11px;
                        "
                    >
                        {escape(str(recommendation))}
                    </div>

                </div>

                <div>

                    <div class="tc-executive-title">
                        Executive Candidate Assessment
                    </div>

                    <div class="tc-executive-description">
                        <strong>Candidate evidence:</strong>
                        {escape(str(candidate_file))}
                    </div>

                    <div class="tc-executive-description">
                        The profile has been compared with the target
                        role requirements. Matched capabilities and
                        validation areas should guide the authorised
                        review and structured interview.
                    </div>

                    <div class="tc-review-badge">
                        HUMAN REVIEW REQUIRED
                    </div>

                </div>

            </div>
            """
        )

        executive1, executive2, executive3 = st.columns(3)

        with executive1:
            st.metric(
                "Resume Match",
                f"{score}%"
            )

        with executive2:
            st.metric(
                "Matched Capabilities",
                len(matched_skills)
            )

        with executive3:
            st.metric(
                "Validation Areas",
                len(missing_skills)
            )

        st.progress(
            min(max(float(score) / 100, 0.0), 1.0)
        )

        st.subheader("📋 Executive Summary")

        if score >= 85:
            st.success(
                "The resume demonstrates strong category-level "
                "alignment with the target role. Proceed with "
                "structured technical validation."
            )

        elif score >= 70:
            st.warning(
                "The resume demonstrates partial alignment. "
                "Validate the identified gaps and technical depth "
                "during the structured interview."
            )

        else:
            st.error(
                "Several role capability categories were not identified "
                "in the resume. Review the evidence and targeted "
                "interview responses before determining next steps."
            )

        insight_col1, insight_col2 = st.columns(
            2,
            gap="large"
        )

        with insight_col1:

            st.subheader("✅ Matched Capabilities")

            render_skill_pills(
                matched_skills,
                "matched"
            )

        with insight_col2:

            st.subheader("⚠️ Validation Areas")

            render_skill_pills(
                missing_skills,
                "gap"
            )

        if st.session_state.get("interview_complete"):

            interview_score = st.session_state.get(
                "interview_score"
            )

            if interview_score is not None:
                st.subheader("🎤 Interview Evidence")

                st.metric(
                    "Interview Response Score",
                    f"{interview_score}/10"
                )

        else:
            st.info(
                "Complete the structured interview to add interview "
                "response evidence to this view."
            )

        st.caption(
            "TalentCopilotAI provides decision-support evidence. "
            "Final candidate decisions remain with authorised human reviewers."
        )