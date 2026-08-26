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
    resume_text,
    job_description
):

    resume_questions = []

    jd_questions = []

    gap_questions = []

    behavioural_questions = []

    resume_text = resume_text.lower()

    job_description = job_description.lower()

    if "kubernetes" in job_description:
        jd_questions.append(
            "This role requires Kubernetes expertise. Describe the most complex Kubernetes environment you have supported."
        )

    if "aws" in job_description:
        jd_questions.append(
            "AWS is an important requirement for this role. Describe a production AWS workload you supported."
        )

    if "vmware" in job_description:
        jd_questions.append(
            "This role requires VMware experience. Describe a VMware migration or upgrade project you performed."
        )

    if "terraform" in job_description:
        jd_questions.append(
            "Terraform is required for this position. Explain how you design reusable Terraform modules."
        )

    if "production" in resume_text:
        resume_questions.append(
            "Your resume mentions production support. Describe a critical production incident you handled and how you resolved it."
        )

    if "migration" in resume_text:
        resume_questions.append(
            "Tell us about a migration project you worked on. What challenges did you face?"
        )

    if "automation" in resume_text:
        resume_questions.append(
            "Describe the most impactful automation solution you developed."
        )

    if (
        "lead" in resume_text
        or "manager" in resume_text
        or "team lead" in resume_text
        or "project lead" in resume_text
    ):
        resume_questions.append(
            "Your resume indicates leadership experience. Describe a technical decision you made that significantly benefited your team or organisation."
        )

    if "vmware" in resume_text:
        resume_questions.append(
            "Your resume mentions VMware. Describe the largest VMware environment you managed."
    )

    if "terraform" in resume_text:
        resume_questions.append(
            "Your resume mentions Terraform. Explain the most reusable Terraform module you developed and how it was used."
        )

    if "aws" in resume_text:
        resume_questions.append(
            "Your resume mentions AWS. Describe the most complex AWS workload you supported and the challenges you encountered."
        )

    if "python" in resume_text:
        resume_questions.append(
            "Your resume references Python. Describe an automation solution you developed that delivered measurable business value."
        )

    if "kubernetes" in resume_text:
        resume_questions.append(
            "Your resume mentions Kubernetes. Describe the most critical Kubernetes outage you handled and how you resolved it."
        )

    if "linux" in resume_text:
        resume_questions.append(
            "Your resume references Linux administration. Describe the most difficult Linux issue you diagnosed and fixed."
        )

    if "docker" in resume_text:
        resume_questions.append(
            "Your resume mentions Docker. Describe a containerisation project that improved deployment efficiency."
        )

    if "jenkins" in resume_text:
        resume_questions.append(
            "Your resume references Jenkins. Describe a CI/CD pipeline you designed or improved."
        )

    for skill in matched_skills[:2]:

        if skill in QUESTION_BANK:

            resume_questions.append(
                random.choice(
                    QUESTION_BANK[skill]
                )
            )

    for skill in missing_skills[:1]:

        gap_questions.append(
            f"{skill} appears to be required for this role but was not identified in your resume. How would you approach gaining competency in this area?"
    )

    behavioural_questions = [
        "Describe a challenging technical problem you solved.",
        "Tell us about a project you are most proud of."
    ]
    
    
    questions = (
        jd_questions[:2]
        + resume_questions[:3]
        + gap_questions[:1]
        + behavioural_questions[:2]
    )

    questions = list(dict.fromkeys(questions))

    return questions