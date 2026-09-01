# from engines.resume_engine import analyse_candidate
# from utils.voice_interview import render_voice_interview
# from utils.resume_parser import extract_resume_text
# from utils.jd_matcher import calculate_match
# from utils.evaluation_engine import evaluate_candidate
# from utils.interview_engine import generate_questions
# import streamlit as st

# st.set_page_config(
#     page_title="TalentCopilot AI",
#     page_icon="🤖",
#     layout="wide"
# )

# st.markdown(
#     """
#     <style>
#         [data-testid="stHeader"] {
#             display:none;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.markdown(
#     """
#     # TALENTCOPILOTAI

#     ## 🤖 Comcast - திறன்

#     AI Resume Screening • Interview Intelligence • Executive Hiring Insights
#     """
# )

# st.info(
#     "🚀 Recruitment Intelligence Platform for Resume Analysis, Structured Interviews and Executive Hiring Insights"
# )

# if "analysis_complete" not in st.session_state:
#     st.session_state.analysis_complete = False

# st.markdown("""
# <style>

# /* ---------- Fonts ---------- */

# html, body, [class*="css"] {
#     font-family:
#     'Segoe UI',
#     'Inter',
#     sans-serif;
#     }

# /* ---------- Main Background ---------- */

# .stApp {

#     background:

#     radial-gradient(
#         circle at top right,
#         rgba(88,211,255,0.15),
#         transparent 30%
#     ),

#     radial-gradient(
#         circle at bottom left,
#         rgba(17,77,142,0.35),
#         transparent 40%
#     ),

#     linear-gradient(
#         135deg,
#         #02152D,
#         #082953,
#         #123B70
#     );

#     color: white;
# }

# section.main > div {
#     padding-top: 0rem !important;
# }

# /* ---------- Headers ---------- */

# h1,h2,h3,h4,h5 {
#     color: white !important;
# }

# /* ---------- Text ---------- */

# # p, span, label {
# #     color: #D7E3F4 !important;
# # }

# /* ---------- Tabs ---------- */

# .stTabs [data-baseweb="tab"] {

#     color: #BFD9F5 !important;

#     font-size: 15px !important;

#     font-weight: 700;

#     height: 45px;

#     border-radius: 12px;

#     padding-left: 20px;

#     padding-right: 20px;

#     background: rgba(255,255,255,0.03);
# }

# .stTabs [aria-selected="true"] {

#     background: rgba(88,211,255,0.15) !important;

#     color: white !important;

#     border-radius: 10px;

#     border-bottom: none !important;
# }

# /* ---------- Buttons ---------- */

# .stButton button {
#     background-color: #58D3FF;
#     color: #02152D;
#     border-radius: 10px;
#     font-weight: bold;
# }

# /* ---------- Input Boxes ---------- */

# # .stTextArea textarea {

# #     background-color: #0D2548 !important;

# #     color: #FFFFFF !important;

# #     font-size: 14px !important;

# #     border: 1px solid #58D3FF !important;
# # }

# .stTextArea textarea {

#     background-color: rgba(13,37,72,0.85) !important;

#     color: white !important;

#     border-radius: 10px !important;

#     border: 1px solid rgba(88,211,255,0.30) !important;
# }

# .stTextArea textarea::placeholder {

#     color: #AFC4DE !important;

#     opacity: 1 !important;
# }

# /* ---------- Upload Box ---------- */

# [data-testid="stFileUploader"] {

#     background-color: rgba(13,37,72,0.85);

#     border-radius: 12px;

#     padding: 6px;

#     border: 1px solid rgba(88,211,255,0.30);

#     max-width: 280px;
# }

# [data-testid="stFileUploader"] section {
#     padding: 0rem !important;
# }

# [data-testid="stFileUploaderDropzone"] {
#     min-height: 50px !important;
#     padding: 0.2rem !important;
# }

# [data-testid="stFileUploaderDropzone"] div {
#     padding: 0px !important;
# }

# [data-testid="stFileUploaderDropzoneInstructions"] {
#     display: none !important;
# }

# /* ---------- Cards ---------- */

# .metric-card {
#     background:#0D2548;
#     padding:20px;
#     border-radius:15px;
#     border:1px solid #2C4D75;
#     color:white;
#     text-align:center;
# }

# /* Hide Deploy Button */
# [data-testid="stToolbar"] {
#     display: none;
# }

# /* Hide Streamlit Header */
# header[data-testid="stHeader"] {
#     display: none;
# }

# # /* Hide Hamburger Menu */
# # #MainMenu {
# #     visibility: hidden;
# # }

# /* Hide Footer */
# footer {
#     visibility: hidden;
# }

# /* Remove Top Gap */
# .block-container {
#     padding-top: 0rem !important;
#     margin-top: 0rem !important;
#     max-width: 98%;
# }

# /* Upload Button Styling */

# [data-testid="stFileUploader"] button {

#     background-color: #58D3FF !important;

#     color: #02152D !important;

#     font-weight: 700 !important;

#     border: none !important;

#     border-radius: 10px !important;

#     padding: 8px 18px !important;
# }

# [data-testid="stFileUploader"] button:hover {
#     background-color: #7DE0FF !important;
#     color: #02152D !important;
# }

# [data-testid="stFileUploader"] small {
#     color: #AFC4DE !important;
# }

# /* Executive Metric Cards */

# [data-testid="stMetric"] {

#     background: rgba(8,41,83,0.70);

#     backdrop-filter: blur(12px);

#     padding: 20px;

#     border-radius: 15px;

#     border: 1px solid rgba(88,211,255,0.25);
# }

# [data-testid="stMetricLabel"] {
#     color: #58D3FF !important;
#     font-size: 12px !important;
#     font-weight: 600 !important;
# }

# [data-testid="stMetricValue"] {
#     color: #FFFFFF !important;
#     font-size: 24px !important;
#     font-weight: 700 !important;
# }

# [data-testid="stMetricDelta"] {
#     color: #00D084 !important;
# }

# /* Smaller Enterprise Font Sizes */

# p,
# span,
# label {
#     font-size: 13px !important;
# }

# </style>
# """, unsafe_allow_html=True)

# # # -------------------------------------------------
# # # TALENTCOPILOTAI EXECUTIVE UI OVERRIDES
# # # -------------------------------------------------

# # st.markdown(
# #     """
# #     <style>

# #     /* ---------- Executive Colour System ---------- */

# #     :root {
# #         --tc-bg: #*4F7FA;
# #         --tc-surface: #FFFF*F;
# #         --tc-surface-soft: #EAF*F8;
# #         --tc-navy: #102A43;
# #   *     --tc-blue: #0B5CAB;
# #         -*tc-cyan: #36C5F0;
# #         --tc-tea*: #00A3A3;
# #         --tc-text: #243*53;
# #         --tc-muted: #627D98;
# #  *      --tc-success: #16865C;
# #      *  --tc-warning: #B7791F;
# #         -*tc-danger: #C23B4A;
# #         --tc-border: #D7E2EA;
# #     }

# #     /* ---------- Application Background ---------- */

# #     .stApp {
# #         background*
# #             radial-gradient(
# #     *           circle at top right,
# #   *             rgba(54, 197, 240, 0.*0),
# #                 transparent 28*
# #             ),
# #             linear*gradient(
# #                 180deg,
# # *               #F8FAFC 0%,
# #                 #EEF4F8 100%
# #             ) !important;

# #         color: var(--tc-text) !important;
# #     }

# #     .block-container {
# #         max-width: 1200px !important;
# #         padding-top: 0.65rem !important;
# #         padding-bottom: 2rem !important;
# #     }

# #     /* ---------- General Text ---------- */

# #     h1,
# #     h2,
# #     h3,
# #     h4,
# #     h5 {
# #         color: var(--tc-navy) !important;
# #         font-family: "Aptos Display", "Segoe UI", sans-serif !important;
# #     }

# #     p,
# #     span,
# #     label {
# #         color: var(--tc-text);
# #     }

# #     /* ---------- Navigation Tabs ---------- */

# #     .stTabs [data-baseweb="tab-list"] {
# #         background: var(--tc-surface);
# #         border: 1px solid var(--tc-border);
# #         border-radius: 14px;
# #         padding: 5px;
# #         gap: 5px;
# #         box-shadow: 0 5px 18px rgba(16, 42, 67, 0.08);
# #     }

# #     .stTabs [data-baseweb="tab"] {
# #         background: transparent !important;
# #         color: var(--tc-muted) !important;
# #         border-radius: 10px !important;
# #         height: 42px !important;
# #         padding-left: 18px !important;
# #         padding-right: 18px !important;
# #         font-size: 14px !important;
# #         font-weight: 650 !important;
# #     }

# #     .stTabs [aria-selected="true"] {
# #         background: var(--tc-blue) !important;
# #         color: #FFFFFF !important;
# #     }

# #     /* ---------- Primary Buttons ---------- */

# #     .stButton button {
# #         min-height: 42px;
# #         background: linear-gradient(
# #             135deg,
# #             var(--tc-blue),
# #             #0877BE
# #         ) !important;
# #         color: #FFFFFF !important;
# #         border: none !important;
# #         border-radius: 10px !important;
# #         font-weight: 700 !important;
# #         box-shadow: 0 6px 15px rgba(11, 92, 171, 0.20);
# #         transition:
# #             transform 0.15s ease,
# #             box-shadow 0.15s ease;
# #     }

# #     .stButton button:hover {
# #         transform: translateY(-1px);
# #         box-shadow: 0 9px 20px rgba(11, 92, 171, 0.28);
# #     }

# #     /* ---------- Job Description ---------- */

# #     .stTextArea textarea {
# #         background: var(--tc-surface) !important;
# #         color: var(--tc-navy) !important;
# #         border: 1px solid var(--tc-border) !important;
# #         border-radius: 12px !important;
# #         font-size: 14px !important;
# #         box-shadow: 0 4px 12px rgba(16, 42, 67, 0.05);
# #     }

# #     .stTextArea textarea:focus {
# #         border-color: var(--tc-blue) !important;
# #         box-shadow: 0 0 0 2px rgba(11, 92, 171, 0.12) !important;
# #     }

# #     .stTextArea textarea::placeholder {
# #         color: #829AB1 !important;
# #     }

# #     /* ---------- Resume Uploader ---------- */

# #     [data-testid="stFileUploader"] {
# #         max-width: none !important;
# #         background: var(--tc-surface) !important;
# #         border: 1px solid var(--tc-border) !important;
# #         border-radius: 12px !important;
# #         padding: 6px !important;
# #         box-shadow: 0 4px 12px rgba(16, 42, 67, 0.05);
# #     }

# #     [data-testid="stFileUploaderDropzone"] {
# #         min-height: 72px !important;
# #         background: var(--tc-surface-soft) !important;
# #         border: 1px dashed #9FBFD6 !important;
# #         border-radius: 9px !important;
# #     }

# #     [data-testid="stFileUploader"] button {
# #         background: var(--tc-blue) !important;
# #         color: #FFFFFF !important;
# #         border-radius: 8px !important;
# #         padding: 7px 14px !important;
# #         font-weight: 700 !important;
# #     }

# #     /* ---------- Metric Cards ---------- */

# #     [data-testid="stMetric"] {
# #         min-height: 108px;
# #         background: var(--tc-surface) !important;
# #         border: 1px solid var(--tc-border) !important;
# #         border-radius: 14px !important;
# #         padding: 17px !important;
# #         box-shadow: 0 7px 20px rgba(16, 42, 67, 0.07);
# #     }

# #     [data-testid="stMetricLabel"] {
# #         color: var(--tc-muted) !important;
# #         font-size: 11px !important;
# #         font-weight: 750 !important;
# #         letter-spacing: 0.6px;
# #         text-transform: uppercase;
# #     }

# #     [data-testid="stMetricValue"] {
# #         color: var(--tc-navy) !important;
# #         font-size: 27px !important;
# #         font-weight: 800 !important;
# #     }

# #     /* ---------- Progress Bar ---------- */

# #     [data-testid="stProgress"] > div > div {
# #         background: linear-gradient(
# #             90deg,
# #             var(--tc-blue),
# #             var(--tc-cyan)
# #         ) !important;
# #     }

# #     /* ---------- Expanders ---------- */

# #     [data-testid="stExpander"] {
# #         background: var(--tc-surface);
# #         border: 1px solid var(--tc-border);
# #         border-radius: 12px;
# #         box-shadow: 0 4px 12px rgba(16, 42, 67, 0.05);
# #     }

# #     /* ---------- Alerts ---------- */

# #     [data-testid="stAlert"] {
# #         border-radius: 11px !important;
# #     }

# #     </style>
# #     """,
# #     unsafe_allow_html=True
# # )


# # st.markdown("""
# # <div style="
# # background:rgba(13,37,72,0.60);
# # backdrop-filter:blur(12px);
# # padding:3px;
# # border-radius:12px;
# # margin-bottom:8px;
# # border:1px solid rgba(88,211,255,0.25);
# # text-align:center;
# # ">

# # <div style="
# # font-size:12px;
# # color:#58D3FF;
# # letter-spacing:5px;
# # font-weight:700;
# # margin-bottom:2px;
# # ">
# # நேர்காணல்-Copilot-AI
# # </div>

# # <div style="
# # color:white;
# # font-size:15px;
# # font-weight:700;
# # line-height:1.0;
# # margin-bottom:5px;
# # text-shadow:0 0 20px rgba(88,211,255,0.5);
# # ">
# # 🤖 நேர்காணல்-Copilot-AI
# # </div>

# # <div style="
# # color:#58D3FF;
# # font-size:13px;
# # font-weight:600;
# # margin-bottom:4px;
# # ">
# # Enterprise Recruitment Intelligence Platform
# # </div>

# # <div style="
# # color:#B5C8DF;
# # font-size:12px;
# # ">
# # AI Resume Screening • AI Voice Interview • Executive Insights
# # </div>

# # </div>
# # """, unsafe_allow_html=True)



# tab1, tab2, tab3 = st.tabs(
#         [
#             "📄 Resume Intelligence",
#             "🎤 AI Interview",
#             "📊 Executive Insights"
#         ]
#     )

# # Upload Resume

# left_col, right_col = st.columns([1, 2])

# with left_col:

#     st.markdown("""
#     <div style="
#     margin-bottom:2px;
#     ">
#     <span style="
#     color:#58D3FF;
#     font-size:14px;
#     font-weight:600;
#     ">
#     📄 Upload Resume
#     </span>
#     </div>
#     """, unsafe_allow_html=True)

#     uploaded_resume = st.file_uploader(
#         "Upload Resume",
#         type=["pdf", "docx"],
#         label_visibility="collapsed"
#     )

#     if uploaded_resume:
#         st.success(
#             f"✅ {uploaded_resume.name}"
#         )

# with right_col:

#     job_description = st.text_area(
#         "📋 Paste Job Description",
#         height=80
#     )


# # Analyze Button

# st.markdown("<br>", unsafe_allow_html=True)

# analyse_clicked = st.button(
#     "🚀 Analyze Candidate",
#     use_container_width=True,
#     type="primary"
# )

# if analyse_clicked:

#         # st.write("DEBUG: Button clicked")

#         st.session_state.analysis_complete = False

#         if uploaded_resume and job_description:

#             analysis = analyse_candidate(
#                 uploaded_resume,
#                 job_description
#             )

#             resume_text = analysis["resume_text"]

#             score = analysis["score"]

#             matched_skills = analysis["matched_skills"]

#             missing_skills = analysis["missing_skills"]

#             recommendation = analysis["recommendation"]

#             if score >= 85:
#                 banner_color = "#00D084"
#                 banner_text = "Strong Match"

#             elif score >= 70:
#                 banner_color = "#F5A623"
#                 banner_text = "Moderate Match"

#             else:
#                 banner_color = "#E53935"
#                 banner_text = "Needs Validation"

#             questions = generate_questions(
#                 matched_skills,
#                 missing_skills,
#                 resume_text,
#                 job_description
#             )
            
#             st.session_state["questions"] = questions
#             st.session_state["score"] = score
#             st.session_state["matched_skills"] = matched_skills
#             st.session_state["missing_skills"] = missing_skills
#             st.session_state["recommendation"] = recommendation
#             st.session_state["resume_text"] = resume_text
#             st.session_state["analysis_complete"] = True

#             total_skills = (
#                 len(matched_skills)
#                 + len(missing_skills)
#             )

#             st.markdown("""
#             <div style="
#             padding:10px 0px;
#             margin-bottom:15px;
#             ">

#             <div style="
#             color:#58D3FF;
#             font-size:12px;
#             font-weight:700;
#             letter-spacing:2px;
#             ">
#             CANDIDATE INTELLIGENCE
#             </div>

#             <div style="
#             color:white;
#             font-size:28px;
#             font-weight:800;
#             margin-top:4px;
#             ">
#             Candidate Fit Overview
#             </div>

#             <div style="
#             color:#BFD9F5;
#             font-size:14px;
#             margin-top:6px;
#             ">
#             Resume alignment and validation areas identified from the uploaded candidate profile.
#             </div>

#             </div>
#             """, unsafe_allow_html=True)

#             st.markdown(
#                 f"""
#                 <div style="
#                     background:linear-gradient(
#                         135deg,
#                         #082953,
#                         #0B5CAB
#                     );

#                     border-radius:20px;

#                     padding:35px;

#                     text-align:center;

#                     margin-bottom:25px;

#                     box-shadow:0px 10px 25px rgba(0,0,0,.30);
#                 ">

#                     <div style="
#                         color:#58D3FF;

#                         font-size:12px;

#                         font-weight:700;

#                         letter-spacing:2px;
#                     ">
#                         CANDIDATE ASSESSMENT
#                     </div>

#                     <div style="
#                         color:white;

#                         font-size:72px;

#                         font-weight:800;

#                         margin-top:10px;
#                     ">
#                         {score}%
#                     </div>

#                     <div style="
#                         color:white;

#                         font-size:24px;

#                         font-weight:700;

#                         margin-top:10px;
#                     ">
#                         {recommendation}
#                     </div>

#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#             # info1, info2, info3 = st.columns(3)

#             m1, m2, m3, m4 = st.columns(4)

#             with m1:
#                 st.metric(
#                     "Match Score",
#                     f"{score}%"
#                 )

#             with m2:
#                 st.metric(
#                     "Matched Skills",
#                     len(matched_skills)
#                 )

#             with m3:
#                 st.metric(
#                     "Skill Gaps",
#                     len(missing_skills)
#                 )

#             with m4:
#                 st.metric(
#                     "Recommendation",
#                     recommendation
#                 )

#             # with info1:
#             #     st.metric(
#             #         "Technical Fit",
#             #         f"{score}%"
#             #     )

#             # with info2:
#             #     st.metric(
#             #         "Matched Skills",
#             #         len(matched_skills)
#             #     )

#             # with info3:
#             #     st.metric(
#             #         "Skill Gaps",
#             #         len(missing_skills)
#             #     )

            
#             st.markdown(
#                 f"""
#                 <div style="
#                     background:rgba(8,41,83,0.65);
#                     border-left:5px solid {banner_color};
#                     padding:18px;
#                     border-radius:12px;
#                     margin-top:15px;
#                     margin-bottom:20px;
#                 ">

#                     <div style="
#                         color:{banner_color};
#                         font-size:11px;
#                         font-weight:700;
#                         letter-spacing:2px;
#                     ">
#                         CANDIDATE ASSESSMENT
#                     </div>

#                     <div style="
#                         color:white;
#                         font-size:22px;
#                         font-weight:800;
#                         margin-top:6px;
#                     ">
#                         {banner_text}
#                     </div>

#                     <div style="
#                         color:#BFD9F5;
#                         margin-top:6px;
#                         font-size:13px;
#                     ">
#                         {recommendation}
#                     </div>

#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#             # col1, col2, col3, col4 = st.columns(4)

#             # with col1:
#             #     st.metric(
#             #         "Match Score",
#             #         f"{score}%"
#             #     )

#             st.progress(score / 100)

#             # with col2:
#             #     st.metric(
#             #         "Recommendation",
#             #         recommendation
#             #     )

#             st.markdown("---")
#             # st.header("📊 Executive Candidate Scorecard")\

#             # st.markdown("""
#             # <h2 style="
#             # color:white;
#             # font-size:28px;
#             # margin-top:20px;
#             # ">
#             # 📊 Executive Candidate Scorecard
#             # </h2>
#             # """, unsafe_allow_html=True)

#             # score_col1, score_col2 = st.columns(2)

#             # with score_col1:
#             #     st.metric("Match Score", f"{score}%")
#             #     st.metric("Matched Skills", len(matched_skills))

#             # with score_col2:
#             #     st.metric("Missing Skills", len(missing_skills))
#             #     st.metric("Recommendation", recommendation)
            
#             st.subheader("✅ Matched Skills")

#             skills_html = " ".join(
#                 [
#                     f"<span style='background:#0D2548;border:1px solid #58D3FF;color:white;padding:8px 14px;border-radius:20px;font-weight:600;margin:4px;display:inline-block;'>✅ {skill.title()}</span>"
#                     for skill in matched_skills
#                 ]
#             )

#             st.markdown(skills_html, unsafe_allow_html=True)                                
            
#             st.subheader("❌ Missing Skills")

#             gaps_html = " ".join(
#                 [
#                     f"<span style='background:#102B4F;border:1px solid #FFA500;color:white;padding:8px 14px;border-radius:20px;font-weight:600;margin:4px;display:inline-block;'>⚠️ {skill.title()}</span>"
#                     for skill in missing_skills
#                 ]
#             )

#             st.markdown(gaps_html, unsafe_allow_html=True)

#             if st.session_state.get("analysis_complete"):
    
#                 questions = st.session_state["questions"]
#                 score = st.session_state["score"]
#                 matched_skills = st.session_state["matched_skills"]
#                 missing_skills = st.session_state["missing_skills"]
#                 recommendation = st.session_state["recommendation"]
#                 resume_text = st.session_state["resume_text"]

            
#             st.subheader("🎤 AI Interview Questions")

#             # st.markdown("""
#             # <div style="
#             # background:#082953;
#             # padding:20px;
#             # border-radius:15px;
#             # border:1px solid #1E4E7A;
#             # ">
#             # """, unsafe_allow_html=True)

#             # for i, question in enumerate(questions, start=1):
#             #     st.markdown(
#             #         f"""
#             #         <div style="
#             #         color:#FFFFFF;
#             #         font-size:13px;
#             #         margin-bottom:6px;
#             #         line-height:1.3;
#             #         ">
#             #         {i}. {question}
#             #         </div>
#             #         """,
#             #         unsafe_allow_html=True
#             #     )

#             st.subheader("🎤 Recommended Interview Questions")

#             st.code(repr(questions[0]))

#             st.subheader("🎤 Recommended Interview Questions")

#             st.write(questions)

#         for i, question in enumerate(questions, start=1):

#             st.markdown(
#                 f"""
#                 <div style="
#                     background:rgba(8,41,83,0.72);
#                     border:1px solid rgba(88,211,255,0.20);
#                     border-left:4px solid #58D3FF;
#                     border-radius:12px;
#                     padding:14px;
#                     margin-bottom:10px;
#                 ">

#                     <div style="
#                         color:#58D3FF;
#                         font-size:12px;
#                         font-weight:700;
#                         margin-bottom:6px;
#                     ">
#                         QUESTION {i}
#                     </div>

#                     <div style="
#                         color:#FFFFFF;
#                         font-size:15px;
#                         line-height:1.5;
#                     ">
#                         {question}
#                     </div>

#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#             st.markdown("</div>", unsafe_allow_html=True)

#             st.markdown("---")                            

#             # st.markdown("</div>", unsafe_allow_html=True)

#             # st.markdown("---")

#             # st.subheader("📊 Executive Candidate Scorecard")

#             # col1, col2, col3, col4 = st.columns(4)

#             # with col1:
#             #     st.metric(
#             #         "🎯 Match Score",
#             #         f"{score}%"
#             #     )

#             # with col2:
#             #     st.metric(
#             #         "✅ Skills",
#             #         len(matched_skills)
#             #     )

#             # with col3:
#             #     st.metric(
#             #         "⚠️ Missing",
#             #         len(missing_skills)
#             #     )

#             # with col4:
#             #     st.metric(
#             #         "🏆 Rating",
#             #         recommendation
#             #     )


#             # st.subheader("📝 Executive Summary")

#             # if score >= 85:
#             #     st.success(
#             #         "Candidate demonstrates strong alignment with the job requirements and is recommended for advanced interview rounds."
#             #     )

#             # elif score >= 70:
#             #     st.warning(
#             #         "Candidate shows potential but should be further assessed during technical interviews."
#             #     )

#             # else:
#             #     st.error(
#             #         "Candidate currently lacks several key skills required for this role."
#             #     )

#             # st.subheader("🎯 Hiring Decision")

#             # if score >= 85:
#             #     st.success(
#             #         "✅ Proceed to Final Interview Round"
#             #     )

#             # elif score >= 70:
#             #     st.warning(
#             #         "🟡 Proceed to Technical Assessment"
#             #     )

#             # else:
#             #     st.error(
#             #         "❌ Screen Out Candidate"
#             #     )

#             with st.expander(
#                 "📄 View Extracted Resume Evidence"
#             ):
#                 st.write(
#                     resume_text[:5000]
#                 )

#         else:
#             st.warning(
#                 "Upload Resume and Job Description"
#             )


# with tab2:

#     st.markdown("""
#     <h2 style="
#     color:white;
#     margin-bottom:5px;
#     ">
#     🎤 Structured AI Interview
#     </h2>

#     <p style="
#     color:#9FC1E1;
#     ">
#     Resume-driven interview questions and voice assessment.
#     </p>
#     """, unsafe_allow_html=True)

#     if "questions" in st.session_state:

#         render_voice_interview(
#             st.session_state["questions"]
#         )

#     else:

#         st.info(
#             "Analyse a candidate first to generate interview questions."
#         )


# with tab3:

#     st.header("📊 Executive Insights")

#     if not st.session_state.get(
#         "analysis_complete"
#     ):
#         st.info(
#             "Analyse a candidate first."
#         )

#     else:

#         score = (
#             st.session_state["score"]
#         )

#         matched_skills = (
#             st.session_state["matched_skills"]
#         )

#         missing_skills = (
#             st.session_state["missing_skills"]
#         )

#         recommendation = (
#             st.session_state["recommendation"]
#         )

#         hero_colour = "#00D084"

#         if score < 85:
#             hero_colour = "#F5A623"

#         if score < 70:
#             hero_colour = "#E53935"

#         st.markdown(
#             f"""
#             <div style="
#                 background:{hero_colour};
#                 padding:30px;
#                 border-radius:20px;
#                 text-align:center;
#                 margin-bottom:25px;
#                 box-shadow:0 0 25px rgba(0,0,0,0.25);
#             ">

#                 <div style="
#                     color:white;
#                     font-size:18px;
#                     font-weight:600;
#                 ">
#                     Candidate Assessment
#                 </div>

#                 <div style="
#                     color:white;
#                     font-size:64px;
#                     font-weight:800;
#                     line-height:1;
#                     margin-top:10px;
#                 ">
#                     {score}%
#                 </div>

#                 <div style="
#                     color:white;
#                     font-size:22px;
#                     font-weight:700;
#                     margin-top:10px;
#                 ">
#                     {recommendation}
#                 </div>

#             </div>
#             """,
#             unsafe_allow_html=True
#         )


#         col1, col2, col3, col4 = st.columns(4)

#         with col1:
#             st.metric(
#                 "Match Score",
#                 f"{score}%"
#             )

#         with col2:
#             st.metric(
#                 "Matched Skills",
#                 len(matched_skills)
#             )

#         with col3:
#             st.metric(
#                 "Skill Gaps",
#                 len(missing_skills)
#             )

#         with col4:
#             st.metric(
#                 "Recommendation",
#                 recommendation
#             )

#         st.progress(
#             score / 100
#         )

#         st.subheader(
#             "📋 Executive Summary"
#         )

#         if score >= 85:

#             st.success(
#                 "Candidate demonstrates strong alignment with the job requirements."
#             )

#         elif score >= 70:

#             st.warning(
#                 "Candidate has good potential and should proceed to technical evaluation."
#             )

#         else:

#             st.error(
#                 "Candidate currently lacks several key skills required for the role."
#             )

#         st.subheader(
#             "✅ Matched Skills"
#         )

#         for skill in matched_skills:

#             st.success(
#                 f"✅ {skill}"
#             )

#         st.subheader(
#             "⚠️ Missing Skills"
#         )

#         for skill in missing_skills:

#             st.warning(
#                 f"⚠️ {skill}"
#             )


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
    Render HTML safely without Markdown indentation issues.
    """
    st.markdown(
        dedent(content).strip(),
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
        font-size: 31px;
        font-weight: 800;
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
            🤖 Comcast - திறன்
        </div>

        <div class="tc-hero-subtitle">
            AI Resume Screening • Interview Intelligence •
            Executive Hiring Insights
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