from utils.resume_parser import extract_resume_text
from utils.jd_matcher import calculate_match
from utils.evaluation_engine import evaluate_candidate


def analyse_candidate(uploaded_resume, job_description):

    resume_text = extract_resume_text(
        uploaded_resume
    )

    score, matched_skills, missing_skills = calculate_match(
        resume_text,
        job_description
    )

    recommendation = evaluate_candidate(
        score
    )

    return {
        "resume_text": resume_text,
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommendation": recommendation
    }