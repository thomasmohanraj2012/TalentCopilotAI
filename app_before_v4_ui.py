
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
    padding-top: 0.1rem;
    max-width: 98%;
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


st.markdown("""
<div style="
background:rgba(13,37,72,0.60);
backdrop-filter:blur(12px);
padding:3px;
border-radius:20px;
margin-bottom:20px;
border:1px solid rgba(88,211,255,0.25);
text-align:center;
">

<div style="
font-size:12px;
color:#58D3FF;
letter-spacing:5px;
font-weight:700;
margin-bottom:2px;
">
நேர்காணல்-Copilot-AI
</div>

<div style="
color:white;
font-size:16px;
font-weight:700;
line-height:1.0;
margin-bottom:5px;
text-shadow:0 0 20px rgba(88,211,255,0.5);
">
🤖 நேர்காணல்-Copilot-AI
</div>

<div style="
color:#58D3FF;
font-size:13px;
font-weight:600;
margin-bottom:4px;
">
Enterprise Recruitment Intelligence Platform
</div>

<div style="
color:#B5C8DF;
font-size:12px;
">
AI Resume Screening • AI Voice Interview • Executive Insights
</div>

</div>
""", unsafe_allow_html=True)

# st.markdown("""
# <div style="
# background:rgba(13,37,72,0.45);
# backdrop-filter:blur(12px);
# border:1px solid rgba(88,211,255,0.35);
# border-radius:20px;
# padding:20px;
# margin-top:15px;
# margin-bottom:20px;
# ">
# </div>
# """, unsafe_allow_html=True)

# hero_left, hero_right = st.columns([2,1])

# with hero_left:

#     st.markdown("""
#     <div style="
#     background:rgba(13,37,72,0.65);
#     padding:12px;
#     border-radius:20px;
#     border:1px solid rgba(88,211,255,0.35);
#     ">
    
#     <div style="
#     color:#58D3FF;
#     font-size:14px;
#     letter-spacing:2px;
#     ">
#     AI-Powered Talent Intelligence
#     </div>

#     <h1 style="
#     color:white;
#     font-size:58px;
#     font-weight:700;
#     margin-top:10px;
#     margin-bottom:15px;
#     ">
#     AI-Powered Talent Intelligence
#     </h1>

#     <div style="
#     width:120px;
#     height:4px;
#     background:#58D3FF;
#     border-radius:10px;
#     margin-top:10px;
#     margin-bottom:15px;
#     "></div>

#     <p style="
#     color:#B5C8DF;
#     font-size:18px;
#     line-height:1.6;
#     ">
#     Resume Screening, AI Voice Interview,
#     Candidate Evaluation and Executive Hiring Insights.
#     </p>

#     </div>
#     """, unsafe_allow_html=True)

#     st.button(
#     "🚀 Start Candidate Analysis",
#     use_container_width=False
#     )

# with hero_right:

#     st.markdown("""
#     <div style="
#     text-align:center;
#     margin-top:0px;
#     ">
    
#     <div style="
#     font-size:50px;
#     filter: drop-shadow(
#         0px 0px 25px rgba(88,211,255,0.5)
#     );
#     ">
#     🧠
#     </div>

#     </div>
#     """, unsafe_allow_html=True)

# st.markdown(
#     """
#     <h3 style="
#     text-align:center;
#     color:#58D3FF;
#     margin-top:10px;
#     ">
#     Recruitment Workflow
#     </h3>
#     """,
#     unsafe_allow_html=True
#     )

# wf1, wf2, wf3 = st.columns(3)

# with wf1:
#         st.markdown("""
#         <div style="
#         background:rgba(13,37,72,0.6);
#         border:1px solid rgba(88,211,255,0.25);
#         border-radius:16px;
#         padding:20px;
#         text-align:center;
#         color:white;
#         font-weight:600;
#         ">
#         📄<br><br>
#         Resume Intelligence
#         </div>
#         """, unsafe_allow_html=True)

# with wf2:        
#         st.markdown("""
#         <div style="
#         background:rgba(13,37,72,0.6);
#         border:1px solid rgba(88,211,255,0.25);
#         border-radius:16px;
#         padding:20px;
#         text-align:center;
#         color:white;
#         font-weight:600;
#         ">
#         📄<br><br>
#         AI Interview
#         </div>
#         """, unsafe_allow_html=True)

# with wf3:        
#         st.markdown("""
#         <div style="
#         background:rgba(13,37,72,0.6);
#         border:1px solid rgba(88,211,255,0.25);
#         border-radius:16px;
#         padding:20px;
#         text-align:center;
#         color:white;
#         font-weight:600;
#         ">
#         📄<br><br>
#         Executive Insights
#         </div>
#         """, unsafe_allow_html=True)

# st.markdown("""
# <div style="
# background:rgba(13,37,72,0.75);
# border:1px solid rgba(88,211,255,0.25);
# border-radius:15px;
# padding:15px;
# margin-bottom:15px;
# ">

# <h2 style="
# color:white;
# margin:0;
# font-size:24px;
# ">
# 🧠 TalentCopilotAI
# </h2>

# <p style="
# color:#58D3FF;
# margin:5px 0 0 0;
# font-size:14px;
# ">
# Resume Intelligence • AI Interview • Executive Insights
# </p>

# </div>
# """, unsafe_allow_html=True)


tab1, tab2, tab3 = st.tabs(
        [
            "📄 Resume Intelligence",
            "🎤 AI Interview",
            "📊 Executive Insights"
        ]
    )


st.markdown("""
<h2 style="
color:white;
margin-bottom:0px;
">
Candidate Evaluation
</h2>

<p style="
color:#9FC1E1;
margin-top:0px;
margin-bottom:5px;
font-size:15px;
">
Upload a resume and compare it against the job description.
</p>
""", unsafe_allow_html=True)

left_col, right_col = st.columns([5, 1])

with left_col:

    job_description = st.text_area(
        "📋 Paste Job Description",
        height=220
    )

    with right_col:

        st.markdown("""
        <div style="
        background:rgba(13,37,72,0.60);
        backdrop-filter:blur(12px);
        border:1px solid rgba(88,211,255,0.25);
        border-radius:20px;
        padding:8px;
        text-align:center;
        margin-top:0px;
        ">
        <h4 style="color:#58D3FF;">
        📄 Upload Resume
        </h4>
        </div>
        """, unsafe_allow_html=True)

        uploaded_resume = st.file_uploader(
            "Upload Resume",
            type=["pdf", "docx"],
            label_visibility="collapsed"
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

    if "questions" in st.session_state:

        render_voice_interview(
            st.session_state["questions"]
        )

    else:

        st.info(
            "Analyse a candidate first to generate interview questions."
        )


with tab3:

    st.header("📊 Executive Scorecard")

    st.info(
        "Candidate Evaluation Dashboard Coming Soon"
    )