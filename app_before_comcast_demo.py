from engines.resume_engine import analyse_candidate
from utils.voice_interview import render_voice_interview
from utils.resume_parser import extract_resume_text
from utils.jd_matcher import calculate_match
from utils.evaluation_engine import evaluate_candidate
from utils.interview_engine import generate_questions
import streamlit as st

st.set_page_config(
    page_title="TalentCopilot AI",
    page_icon="🤖",
    layout="wide"
)

st.markdown(
    """
    <style>
        [data-testid="stHeader"] {
            display:none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<div style="
background:rgba(13,37,72,0.60);
backdrop-filter:blur(12px);
padding:20px;
border-radius:16px;
border:1px solid rgba(88,211,255,0.25);
text-align:center;
margin-bottom:20px;
">

<div style="
font-size:14px;
color:#58D3FF;
font-weight:700;
letter-spacing:3px;
">
TALENTCOPILOTAI
</div>

<div style="
color:white;
font-size:34px;
font-weight:700;
margin-top:8px;
">
🤖 Comcast - திறன்
</div>

<div style="
color:#B5C8DF;
font-size:15px;
margin-top:10px;
">
AI Resume Screening • AI Interview Intelligence • Executive Hiring Insights
</div>

</div>
""", unsafe_allow_html=True)

if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete = False

st.markdown("""
<style>

/* ---------- Fonts ---------- */

html, body, [class*="css"] {
    font-family:
    'Segoe UI',
    'Inter',
    sans-serif;
    }

/* ---------- Main Background ---------- */

.stApp {

    background:

    radial-gradient(
        circle at top right,
        rgba(88,211,255,0.15),
        transparent 30%
    ),

    radial-gradient(
        circle at bottom left,
        rgba(17,77,142,0.35),
        transparent 40%
    ),

    linear-gradient(
        135deg,
        #02152D,
        #082953,
        #123B70
    );

    color: white;
}

section.main > div {
    padding-top: 0rem !important;
}

/* ---------- Headers ---------- */

h1,h2,h3,h4,h5 {
    color: white !important;
}

/* ---------- Text ---------- */

# p, span, label {
#     color: #D7E3F4 !important;
# }

/* ---------- Tabs ---------- */

.stTabs [data-baseweb="tab"] {

    color: #BFD9F5 !important;

    font-size: 15px !important;

    font-weight: 700;

    height: 45px;

    border-radius: 12px;

    padding-left: 20px;

    padding-right: 20px;

    background: rgba(255,255,255,0.03);
}

.stTabs [aria-selected="true"] {

    background: rgba(88,211,255,0.15) !important;

    color: white !important;

    border-radius: 10px;

    border-bottom: none !important;
}

/* ---------- Buttons ---------- */

.stButton button {
    background-color: #58D3FF;
    color: #02152D;
    border-radius: 10px;
    font-weight: bold;
}

/* ---------- Input Boxes ---------- */

# .stTextArea textarea {

#     background-color: #0D2548 !important;

#     color: #FFFFFF !important;

#     font-size: 14px !important;

#     border: 1px solid #58D3FF !important;
# }

.stTextArea textarea {

    background-color: rgba(13,37,72,0.85) !important;

    color: white !important;

    border-radius: 10px !important;

    border: 1px solid rgba(88,211,255,0.30) !important;
}

.stTextArea textarea::placeholder {

    color: #AFC4DE !important;

    opacity: 1 !important;
}

/* ---------- Upload Box ---------- */

[data-testid="stFileUploader"] {

    background-color: rgba(13,37,72,0.85);

    border-radius: 12px;

    padding: 6px;

    border: 1px solid rgba(88,211,255,0.30);

    max-width: 280px;
}

[data-testid="stFileUploader"] section {
    padding: 0rem !important;
}

[data-testid="stFileUploaderDropzone"] {
    min-height: 50px !important;
    padding: 0.2rem !important;
}

[data-testid="stFileUploaderDropzone"] div {
    padding: 0px !important;
}

[data-testid="stFileUploaderDropzoneInstructions"] {
    display: none !important;
}

/* ---------- Cards ---------- */

.metric-card {
    background:#0D2548;
    padding:20px;
    border-radius:15px;
    border:1px solid #2C4D75;
    color:white;
    text-align:center;
}

/* Hide Deploy Button */
[data-testid="stToolbar"] {
    display: none;
}

/* Hide Streamlit Header */
header[data-testid="stHeader"] {
    display: none;
}

# /* Hide Hamburger Menu */
# #MainMenu {
#     visibility: hidden;
# }

/* Hide Footer */
footer {
    visibility: hidden;
}

/* Remove Top Gap */
.block-container {
    padding-top: 0rem !important;
    margin-top: 0rem !important;
    max-width: 98%;
}

/* Upload Button Styling */

[data-testid="stFileUploader"] button {

    background-color: #58D3FF !important;

    color: #02152D !important;

    font-weight: 700 !important;

    border: none !important;

    border-radius: 10px !important;

    padding: 8px 18px !important;
}

[data-testid="stFileUploader"] button:hover {
    background-color: #7DE0FF !important;
    color: #02152D !important;
}

[data-testid="stFileUploader"] small {
    color: #AFC4DE !important;
}

/* Executive Metric Cards */

[data-testid="stMetric"] {

    background: rgba(8,41,83,0.70);

    backdrop-filter: blur(12px);

    padding: 20px;

    border-radius: 15px;

    border: 1px solid rgba(88,211,255,0.25);
}

[data-testid="stMetricLabel"] {
    color: #58D3FF !important;
    font-size: 12px !important;
    font-weight: 600 !important;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-size: 24px !important;
    font-weight: 700 !important;
}

[data-testid="stMetricDelta"] {
    color: #00D084 !important;
}

/* Smaller Enterprise Font Sizes */

p,
span,
label {
    font-size: 13px !important;
}

</style>
""", unsafe_allow_html=True)


# st.markdown("""
# <div style="
# background:rgba(13,37,72,0.60);
# backdrop-filter:blur(12px);
# padding:3px;
# border-radius:12px;
# margin-bottom:8px;
# border:1px solid rgba(88,211,255,0.25);
# text-align:center;
# ">

# <div style="
# font-size:12px;
# color:#58D3FF;
# letter-spacing:5px;
# font-weight:700;
# margin-bottom:2px;
# ">
# நேர்காணல்-Copilot-AI
# </div>

# <div style="
# color:white;
# font-size:15px;
# font-weight:700;
# line-height:1.0;
# margin-bottom:5px;
# text-shadow:0 0 20px rgba(88,211,255,0.5);
# ">
# 🤖 நேர்காணல்-Copilot-AI
# </div>

# <div style="
# color:#58D3FF;
# font-size:13px;
# font-weight:600;
# margin-bottom:4px;
# ">
# Enterprise Recruitment Intelligence Platform
# </div>

# <div style="
# color:#B5C8DF;
# font-size:12px;
# ">
# AI Resume Screening • AI Voice Interview • Executive Insights
# </div>

# </div>
# """, unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(
        [
            "📄 Resume Intelligence",
            "🎤 AI Interview",
            "📊 Executive Insights"
        ]
    )

# with tab1:

#     st.markdown("""
# <div style="
#     background:rgba(8,41,83,0.65);
#     backdrop-filter:blur(12px);
#     padding:25px;
#     border-radius:18px;
#     border:1px solid rgba(88,211,255,0.25);
#     margin-bottom:20px;
# ">

#     <div style="
#         color:#58D3FF;
#         font-size:13px;
#         font-weight:700;
#         letter-spacing:2px;
#     ">
#         TALENTCOPILOTAI
#     </div>

#     <div style="
#         color:white;
#         font-size:32px;
#         font-weight:700;
#         margin-top:6px;
#     ">
#         Candidate Intelligence Platform
#     </div>

#     <div style="
#         color:#B5C8DF;
#         font-size:15px;
#         margin-top:8px;
#     ">
#         AI-Powered Resume Screening, Interview Intelligence and Executive Hiring Insights
#     </div>

# </div>
# """, unsafe_allow_html=True)

    
    # Upload Resume Header

# st.markdown("""
# <div style="
# margin-bottom:2px;
# ">
# <span style="
# color:#58D3FF;
# font-size:14px;
# font-weight:600;
# ">
# 📄 Upload Resume
# </span>
# </div>
# """, unsafe_allow_html=True)


# Upload Resume

left_col, right_col = st.columns([1, 2])

with left_col:

    st.markdown("""
    <div style="
    margin-bottom:2px;
    ">
    <span style="
    color:#58D3FF;
    font-size:14px;
    font-weight:600;
    ">
    📄 Upload Resume
    </span>
    </div>
    """, unsafe_allow_html=True)

    uploaded_resume = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"],
        label_visibility="collapsed"
    )

    if uploaded_resume:
        st.success(
            f"✅ {uploaded_resume.name}"
        )

with right_col:

    job_description = st.text_area(
        "📋 Paste Job Description",
        height=80
    )


# Analyze Button

st.markdown("<br>", unsafe_allow_html=True)

analyse_clicked = st.button(
    "🚀 Analyze Candidate",
    use_container_width=True,
    type="primary"
)

if analyse_clicked:

        # st.write("DEBUG: Button clicked")

        st.session_state.analysis_complete = False

        if uploaded_resume and job_description:

            analysis = analyse_candidate(
                uploaded_resume,
                job_description
            )

            resume_text = analysis["resume_text"]

            score = analysis["score"]

            matched_skills = analysis["matched_skills"]

            missing_skills = analysis["missing_skills"]

            recommendation = analysis["recommendation"]

            if score >= 85:
                banner_color = "#00D084"

            elif score >= 70:
                banner_color = "#F5A623"

            else:
                banner_color = "#E53935"

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
            st.session_state["analysis_complete"] = True

            total_skills = (
                len(matched_skills)
                + len(missing_skills)
            )

            st.markdown("""
            <div style="
            background:#082953;
            padding:20px;
            border-radius:15px;
            border:1px solid #1E4E7A;
            margin-bottom:20px;
            ">
            <h2 style="
            color:#58D3FF;
            margin-bottom:10px;
            ">
            👤 Candidate Analysis Dashboard
            </h2>
            </div>
            """,
            unsafe_allow_html=True)

            info1, info2, info3 = st.columns(3)

            with info1:
                st.metric(
                    "Technical Fit",
                    f"{score}%"
                )

            with info2:
                st.metric(
                    "Matched Skills",
                    len(matched_skills)
                )

            with info3:
                st.metric(
                    "Skill Gaps",
                    len(missing_skills)
                )

            dash1, dash2, dash3, dash4 = st.columns(4)

            with dash1:
                st.metric(
                    "Skills Identified",
                    total_skills
                )

            with dash2:
                st.metric(
                    "Matched",
                    len(matched_skills)
                )

            with dash3:
                st.metric(
                    "Missing",
                    len(missing_skills)
                )

            with dash4:
                st.metric(
                    "Resume Status",
                    "Analysed"
                )

            st.markdown(f"""
            <div style="
            background:{banner_color};
            padding:15px;
            border-radius:12px;
            text-align:center;
            margin-bottom:20px;
            ">
            <h2 style="color:white;">
            🏆 {recommendation}
            </h2>
            </div>
            """,
            unsafe_allow_html=True)

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Match Score",
                    f"{score}%"
                )

            st.progress(score / 100)

            with col2:
                st.metric(
                    "Recommendation",
                    recommendation
                )

            st.markdown("---")
            # st.header("📊 Executive Candidate Scorecard")\

            st.markdown("""
            <h2 style="
            color:white;
            font-size:28px;
            margin-top:20px;
            ">
            📊 Executive Candidate Scorecard
            </h2>
            """, unsafe_allow_html=True)

            score_col1, score_col2 = st.columns(2)

            with score_col1:
                st.metric("Match Score", f"{score}%")
                st.metric("Matched Skills", len(matched_skills))

            with score_col2:
                st.metric("Missing Skills", len(missing_skills))
                st.metric("Recommendation", recommendation)
            
            st.subheader("✅ Matched Skills")

            skills_html = " ".join(
                [
                    f"<span style='background:#0D2548;border:1px solid #58D3FF;color:white;padding:8px 14px;border-radius:20px;font-weight:600;margin:4px;display:inline-block;'>✅ {skill.title()}</span>"
                    for skill in matched_skills
                ]
            )

            st.markdown(skills_html, unsafe_allow_html=True)                                
            
            st.subheader("❌ Missing Skills")

            gaps_html = " ".join(
                [
                    f"<span style='background:#102B4F;border:1px solid #FFA500;color:white;padding:8px 14px;border-radius:20px;font-weight:600;margin:4px;display:inline-block;'>⚠️ {skill.title()}</span>"
                    for skill in missing_skills
                ]
            )

            st.markdown(gaps_html, unsafe_allow_html=True)

            if st.session_state.get("analysis_complete"):
    
                questions = st.session_state["questions"]
                score = st.session_state["score"]
                matched_skills = st.session_state["matched_skills"]
                missing_skills = st.session_state["missing_skills"]
                recommendation = st.session_state["recommendation"]
                resume_text = st.session_state["resume_text"]

            
            st.subheader("🎤 AI Interview Questions")

            st.markdown("""
            <div style="
            background:#082953;
            padding:20px;
            border-radius:15px;
            border:1px solid #1E4E7A;
            ">
            """, unsafe_allow_html=True)

            for i, question in enumerate(questions, start=1):
                st.markdown(
                    f"""
                    <div style="
                    color:#FFFFFF;
                    font-size:13px;
                    margin-bottom:6px;
                    line-height:1.3;
                    ">
                    {i}. {question}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("---")                            

            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("---")

            st.subheader("📊 Executive Candidate Scorecard")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "🎯 Match Score",
                    f"{score}%"
                )

            with col2:
                st.metric(
                    "✅ Skills",
                    len(matched_skills)
                )

            with col3:
                st.metric(
                    "⚠️ Missing",
                    len(missing_skills)
                )

            with col4:
                st.metric(
                    "🏆 Rating",
                    recommendation
                )

            st.subheader("📝 Executive Summary")

            if score >= 85:
                st.success(
                    "Candidate demonstrates strong alignment with the job requirements and is recommended for advanced interview rounds."
                )

            elif score >= 70:
                st.warning(
                    "Candidate shows potential but should be further assessed during technical interviews."
                )

            else:
                st.error(
                    "Candidate currently lacks several key skills required for this role."
                )

            st.subheader("🎯 Hiring Decision")

            if score >= 85:
                st.success(
                    "✅ Proceed to Final Interview Round"
                )

            elif score >= 70:
                st.warning(
                    "🟡 Proceed to Technical Assessment"
                )

            else:
                st.error(
                    "❌ Screen Out Candidate"
                )

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

    st.markdown("""
    <h2 style="
    color:white;
    margin-bottom:5px;
    ">
    🎤 Structured AI Interview
    </h2>

    <p style="
    color:#9FC1E1;
    ">
    Resume-driven interview questions and voice assessment.
    </p>
    """, unsafe_allow_html=True)

    if "questions" in st.session_state:

        render_voice_interview(
            st.session_state["questions"]
        )

    else:

        st.info(
            "Analyse a candidate first to generate interview questions."
        )


with tab3:

    st.header("📊 Executive Insights")

    if not st.session_state.get(
        "analysis_complete"
    ):
        st.info(
            "Analyse a candidate first."
        )

    else:

        score = (
            st.session_state["score"]
        )

        matched_skills = (
            st.session_state["matched_skills"]
        )

        missing_skills = (
            st.session_state["missing_skills"]
        )

        recommendation = (
            st.session_state["recommendation"]
        )

        hero_colour = "#00D084"

        if score < 85:
            hero_colour = "#F5A623"

        if score < 70:
            hero_colour = "#E53935"

        st.markdown(
            f"""
            <div style="
                background:{hero_colour};
                padding:30px;
                border-radius:20px;
                text-align:center;
                margin-bottom:25px;
                box-shadow:0 0 25px rgba(0,0,0,0.25);
            ">

                <div style="
                    color:white;
                    font-size:18px;
                    font-weight:600;
                ">
                    Candidate Assessment
                </div>

                <div style="
                    color:white;
                    font-size:64px;
                    font-weight:800;
                    line-height:1;
                    margin-top:10px;
                ">
                    {score}%
                </div>

                <div style="
                    color:white;
                    font-size:22px;
                    font-weight:700;
                    margin-top:10px;
                ">
                    {recommendation}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Match Score",
                f"{score}%"
            )

        with col2:
            st.metric(
                "Matched Skills",
                len(matched_skills)
            )

        with col3:
            st.metric(
                "Skill Gaps",
                len(missing_skills)
            )

        with col4:
            st.metric(
                "Recommendation",
                recommendation
            )

        st.progress(
            score / 100
        )

        st.subheader(
            "📋 Executive Summary"
        )

        if score >= 85:

            st.success(
                "Candidate demonstrates strong alignment with the job requirements."
            )

        elif score >= 70:

            st.warning(
                "Candidate has good potential and should proceed to technical evaluation."
            )

        else:

            st.error(
                "Candidate currently lacks several key skills required for the role."
            )

        st.subheader(
            "✅ Matched Skills"
        )

        for skill in matched_skills:

            st.success(
                f"✅ {skill}"
            )

        st.subheader(
            "⚠️ Missing Skills"
        )

        for skill in missing_skills:

            st.warning(
                f"⚠️ {skill}"
            )