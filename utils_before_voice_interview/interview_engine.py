# def generate_questions(matched_skills, missing_skills):

#     questions = []

#     for skill in matched_skills[:5]:
#         questions.append(
#             f"Can you explain your experience with {skill}?"
#         )

#     for skill in missing_skills[:3]:
#         questions.append(
#             f"Have you worked with {skill}? If not, how would you learn it?"
#         )

#     questions.extend(
#         [
#             "Describe a challenging technical problem you solved.",
#             "How do you handle production incidents?",
#             "Tell us about a project you are most proud of."
#         ]
#     )

#     return questions

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

def generate_questions(matched_skills, missing_skills):

    questions = []

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