TECH_SKILLS = [
    "kubernetes",
    "docker",
    "jenkins",
    "terraform",
    "ansible",
    "python",
    "linux",
    "aws",
    "azure",
    "gcp",
    "git",
    "github",
    "prometheus",
    "grafana",
    "helm",
    "argocd",
    "streamlit",
    "llm",
    "ollama",
    "kafka",
]

def calculate_match(resume_text, jd_text):

    resume_text = resume_text.lower()
    jd_text = jd_text.lower()

    jd_skills = []

    for skill in TECH_SKILLS:
        if skill in jd_text:
            jd_skills.append(skill)

    matched_skills = []

    for skill in jd_skills:
        if skill in resume_text:
            matched_skills.append(skill)

    if len(jd_skills) == 0:
        return 0, [], []

    score = (
        len(matched_skills)
        / len(jd_skills)
    ) * 100

    missing_skills = list(
        set(jd_skills) -
        set(matched_skills)
    )

    return (
        round(score, 2),
        matched_skills,
        missing_skills
    )