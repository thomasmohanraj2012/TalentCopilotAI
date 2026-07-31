def generate_questions(matched_skills, missing_skills):

    question_bank = {

        "kubernetes": [
            "Explain Kubernetes architecture.",
            "What is a Pod?",
            "How do you troubleshoot CrashLoopBackOff?",
            "Explain ConfigMaps and Secrets.",
            "How do you perform rolling updates?"
        ],

        "docker": [
            "What is Docker?",
            "How do you optimise Docker images?",
            "Difference between Docker and Kubernetes?",
            "What is a Docker volume?"
        ],

        "jenkins": [
            "Explain your CI/CD pipeline.",
            "How do you secure Jenkins?",
            "What Jenkins plugins have you used?"
        ],

        "terraform": [
            "What is Terraform state?",
            "How do you manage remote state?",
            "Explain Terraform modules."
        ],

        "python": [
            "Describe a Python automation you wrote.",
            "How do you handle exceptions in Python?",
            "Explain Python virtual environments."
        ],

        "aws": [
            "Which AWS services have you used?",
            "Explain IAM best practices.",
            "How would you secure an EC2 workload?"
        ],

        "linux": [
            "How do you troubleshoot high CPU usage?",
            "Explain Linux file permissions.",
            "What commands do you use daily?"
        ],

        "git": [
            "Describe your Git workflow.",
            "How do you resolve merge conflicts?",
            "What is Git rebase?"
        ],

        "prometheus": [
            "How does Prometheus collect metrics?",
            "Explain Prometheus exporters."
        ],

        "grafana": [
            "How do you create Grafana dashboards?",
            "What metrics do you typically visualise?"
        ]
    }

    questions = []

    # Ask deeper questions on strengths
    for skill in matched_skills:
        if skill in question_bank:
            questions.extend(question_bank[skill][:2])

    # Ask validation questions on missing skills
    for skill in missing_skills:
        questions.append(
            f"Rate your experience with {skill} and explain a project where you used it."
        )

    return questions[:10]