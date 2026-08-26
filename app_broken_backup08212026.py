
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

if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete = False

st.markdown("""
<style>

/* ---------- Fonts ---------- */

html, body, [class*="css"] {
    font-family: "Sky Text", "Inter", "Segoe UI", sans-serif;
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


# with right_col:

#     st.markdown("""
#     <div style="
#     background:rgba(13,37,72,0.60);
#     backdrop-filter:blur(12px);
#     border:1px solid rgba(88,211,255,0.25);
#     border-radius:20px;
#     padding:15px;
#     text-align:center;
#     margin-top:120px;
#     ">

# <div style="
# font-size:12px;
# color:#58D3FF;
# letter-spacing:5px;
# font-weight:700;
# margin-bottom:2px;
# ">
# திறமை-COPILOTAI
# </div>

# <div style="
# color:white;
# font-size:48px;
# font-weight:700;
# line-height:1.0;
# margin-bottom:5px;
# text-shadow:0 0 20px rgba(88,211,255,0.5);
# ">
# 🤖 திறமை-Copilot AI
# </div>

# <div style="
# color:#58D3FF;
# font-size:16px;
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

    left_col, right_col = st.columns([3, 1])

    with left_col:

        st.markdown("""
        <h2 style="
        color:white;
        margin-bottom:10px;
        ">
        🚀 AI-Powered Talent Intelligence
        </h2>
        """, unsafe_allow_html=True)

        job_description = st.text_area(
            "Paste Job Description",
            height=120
        )  

    if uploaded_resume:
        st.success(
            f"Resume Uploaded: {uploaded_resume.name}"
        )

    if st.button("Analyze Candidate"):
        st.session_state.analysis_complete = False

        if uploaded_resume and job_description:

            resume_text = extract_resume_text(
                uploaded_resume
            )

            score, matched_skills, missing_skills = calculate_match(
                resume_text,
                job_description
            )

            recommendation = evaluate_candidate(score)

            if score >= 85:
                banner_color = "#00D084"

            elif score >= 70:
                banner_color = "#F5A623"

            else:
                banner_color = "#E53935"

            questions = generate_questions(
                matched_skills,
                missing_skills
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

            st.write("Analysis State:",
                st.session_state.get("analysis_complete"))

            st.write("Questions:",
                len(st.session_state.get("questions", [])))

            render_voice_interview(questions)        

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