import random

QUESTION_BANK = {

    "Kubernetes": [
        "Describe a Kubernetes production issue you resolved.",
        "Explain your Kubernetes cluster upgrade strategy.",
        "How do you troubleshoot pod failures in production?"
    ],

    "Infrastructure as Code": [
        "Describe the Terraform or Ansible automation you built.",
        "How do you manage Infrastructure as Code in large environments?",
        "How do you handle version control for infrastructure changes?"
    ],

    "CI/CD": [
        "Explain a CI/CD pipeline you designed.",
        "How do you implement deployment rollback strategies?",
        "Describe your Git workflow and release process."
    ],

    "Linux": [
        "Describe a difficult Linux issue you solved.",
        "How do you troubleshoot high CPU or memory utilisation?",
        "What Linux administration activities do you perform regularly?"
    ],

    "Virtualization": [
        "Describe your VMware administration experience.",
        "How do you troubleshoot VMware performance issues?",
        "Explain a virtual infrastructure migration you performed."
    ],

    "Networking": [
        "Explain DNS resolution troubleshooting.",
        "How do you troubleshoot Kubernetes networking issues?",
        "What networking concepts are important in cloud environments?"
    ],

    "Secrets Management": [
        "How would you secure secrets in Kubernetes?",
        "Describe your experience with Vault or secrets management solutions.",
        "How do you prevent credentials exposure?"
    ],

    "Observability": [
        "How do you use Prometheus and Grafana?",
        "Describe a monitoring platform you built.",
        "How do you approach root cause analysis?"
    ]
}

def generate_questions(
    matched_skills,
    missing_skills,
    resume_text
):

    questions = []

    resume_text = resume_text.lower()

    if "production" in resume_text:
        questions.append(
            "Your resume mentions production support. Describe a critical production incident you handled and how you resolved it."
        )

    if "migration" in resume_text:
        questions.append(
            "Tell us about a migration project you worked on. What challenges did you face?"
        )

    if "automation" in resume_text:
        questions.append(
            "Describe the most impactful automation solution you developed."
        )

    if "lead" in resume_text or "manager" in resume_text:
        questions.append(
            "How do you handle technical leadership and mentoring within your team?"
        )

    for skill in matched_skills[:5]:

        if skill in QUESTION_BANK:

            questions.append(
                random.choice(
                    QUESTION_BANK[skill]
                )
            )

    for skill in missing_skills[:3]:

        questions.append(
            f"You do not list {skill} experience. How would you approach learning it?"
        )

    questions.extend(
        [
            "Describe a challenging technical problem you solved.",
            "How do you handle production incidents?",
            "Tell us about a project you are most proud of."
        ]
    )

    return questions