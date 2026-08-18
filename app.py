
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

st.markdown("""
<style>

/* ---------- Fonts ---------- */

html, body, [class*="css"] {
    font-family: "Sky Text", "Inter", "Segoe UI", sans-serif;
}

/* ---------- Main Background ---------- */

.stApp {
    background-color: #02152D;
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
    color: #58D3FF;
    font-size: 18px;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    border-bottom: 3px solid #58D3FF;
}

/* ---------- Buttons ---------- */

.stButton button {
    background-color: #58D3FF;
    color: #02152D;
    border-radius: 10px;
    font-weight: bold;
}

/* ---------- Input Boxes ---------- */

.stTextInput input,
.stTextArea textarea {
    background-color: #0D2548;
    color: white;
}

/* ---------- Upload Box ---------- */

[data-testid="stFileUploader"] {
    background-color: #0D2548;
    border-radius: 12px;
    padding: 20px;
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

/* Hide Hamburger Menu */
#MainMenu {
    visibility: hidden;
}

/* Hide Footer */
footer {
    visibility: hidden;
}

/* Remove Top Gap */
.block-container {
    padding-top: 0.5rem;
}

/* Upload Button Styling */

[data-testid="stFileUploader"] button {
    background-color: #58D3FF !important;
    color: #02152D !important;
    font-weight: 600 !important;
    border: none !important;
}

[data-testid="stFileUploader"] button:hover {
    background-color: #7DE0FF !important;
    color: #02152D !important;
}

[data-testid="stFileUploader"] small {
    color: #AFC4DE !important;
}

# /* KPI Metrics */

# [data-testid="stMetricValue"] {
#     color: #FFFFFF !important;
#     font-weight: 700 !important;
# }

# [data-testid="stMetricLabel"] {
#     color: #58D3FF !important;
#     font-size: 16px !important;
# }

# /* Enterprise Metric Cards */

# [data-testid="stMetric"] {
#     background: #082953;
#     padding: 20px;
#     border-radius: 15px;
#     border: 1px solid #1E4E7A;
# }

# [data-testid="stMetricValue"] {
#     color: #FFFFFF !important;
#     font-size: 40px !important;
#     font-weight: 700 !important;
# }

# [data-testid="stMetricLabel"] {
#     color: #58D3FF !important;
#     font-size: 16px !important;
# }

/* Executive Metric Cards */

[data-testid="stMetric"] {
    background: #082953;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #1E4E7A;
}

[data-testid="stMetricLabel"] {
    color: #58D3FF !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-size: 38px !important;
    font-weight: 700 !important;
}

[data-testid="stMetricDelta"] {
    color: #00D084 !important;
}

</style>
""", unsafe_allow_html=True)

# st.markdown("""
# <style>

# @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

# html, body, [class*="css"] {
#     font-family: 'Poppins', sans-serif;
# }

# .main-header {
#     background: linear-gradient(
#         90deg,
#         #FF6A2B,
#         #FF3D72,
#         #FF00B8
#     );
#     padding: 25px;
#     border-radius: 15px;
#     text-align: center;
#     color: white;
# }

# </style>
# """, unsafe_allow_html=True)



# st.title("🤖 TalentCopilot AI")

# st.markdown("""
# <div class="main-header">
#     <h1>🤖 TalentCopilot AI</h1>
#     <p>AI Powered Resume Screening & Interview Assistant</p>
# </div>
# """, unsafe_allow_html=True)

# st.markdown("""
# <div style="
# background:#062247;
# padding:20px 30px;
# border-radius:20px;
# margin-bottom:20px;
# border:1px solid #1E4E7A;
# ">

# <h1 style="
# color:white;
# font-size:36px;
# margin-bottom:10px;
# ">
# TalentCopilot AI
# </h1>

# <p style="
# color:#58D3FF;
# font-size:18px;
# font-weight:600;
# margin-bottom:10px;
# ">
# Enterprise Recruitment Intelligence Platform
# </p>

# <p style="
# color:#AFC4DE;
# font-size:14px;
# ">
# AI Resume Screening • AI Voice Interview • Executive Insights
# </p>

# </div>
# """, unsafe_allow_html=True)

st.markdown("""
<div style="
background:#062247;
padding:15px 30px;
border-radius:18px;
margin-bottom:15px;
border:1px solid #1E4E7A;
">

<div style="
font-size:12px;
color:#58D3FF;
letter-spacing:3px;
font-weight:700;
margin-bottom:8px;
">
TALENTCOPILOTAI
</div>

<h1 style="
color:white;
font-size:30px;
margin:0;
">
TalentCopilot AI
</h1>

<p style="
color:#58D3FF;
font-size:16px;
font-weight:600;
margin-top:5px;
margin-bottom:5px;
">
Enterprise Recruitment Intelligence Platform
</p>

<p style="
color:#AFC4DE;
font-size:14px;
margin:0;
">
AI Resume Screening • AI Voice Interview • Executive Insights
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

tab1, tab2, tab3 = st.tabs(
    [
        "📄 Resume Intelligence",
        "🎤 AI Interview",
        "📊 Executive Insights"
    ]
)

with tab1:

    st.header("📄 Resume Intelligence")

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

            col1, col2, col3, col4 = st.columns(4)

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

            # st.subheader("💪 Candidate Strengths")

            # for skill in matched_skills:
            #     st.success(skill)

            # st.subheader("💪 Candidate Strengths")

            # strengths_html = " ".join(
            #     [
            #         f"<span style='background:#E3F2FD;color:#1565C0;padding:8px 14px;border-radius:20px;font-weight:600;margin:4px;display:inline-block;'>💪 {skill.title()}</span>"
            #         for skill in matched_skills
            #     ]
            # )

            # st.markdown(strengths_html, unsafe_allow_html=True)

            # st.subheader("⚠️ Skill Gaps")

            # for skill in missing_skills:
            #     st.warning(skill)

            # st.subheader("🎤 AI Interview Questions")
            # for i, question in enumerate(questions, start=1):
            #     st.write(f"{i}. {question}")

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
                    font-size:18px;
                    margin-bottom:15px;
                    ">
                    {i}. {question}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

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

    st.header("🎤 AI Interview")

    st.info(
        "Interview Question Generator Coming Soon"
    )


with tab3:

    st.header("📊 Executive Scorecard")

    st.info(
        "Candidate Evaluation Dashboard Coming Soon"
    )