# TECH_SKILLS = [
#     "kubernetes",
#     "docker",
#     "jenkins",
#     "terraform",
#     "ansible",
#     "python",
#     "linux",
#     "aws",
#     "azure",
#     "gcp",
#     "git",
#     "github",
#     "prometheus",
#     "grafana",
#     "helm",
#     "argocd",
#     "streamlit",
#     "llm",
#     "ollama",
#     "kafka",
# ]

SKILL_CATEGORIES = {

    "Kubernetes": [
        "kubernetes",
        "rancher",
        "eks",
        "aks",
        "gke",
        "openshift"
    ],

    "Infrastructure as Code": [
        "terraform",
        "ansible",
        "puppet",
        "chef",
        "helm"
    ],

    "CI/CD": [
        "jenkins",
        "gitlab",
        "github",
        "github actions",
        "azure devops"
    ],

    "Cloud": [
        "aws",
        "azure",
        "gcp"
    ],

    "Linux": [
        "linux",
        "ubuntu",
        "redhat",
        "rhel",
        "centos"
    ],

    "Virtualization": [
        "vmware",
        "vsphere",
        "kvm",
        "openstack"
    ],

    "Observability": [
        "prometheus",
        "grafana",
        "splunk",
        "elk",
        "datadog"
    ],

    "Networking": [
        "dns",
        "ingress",
        "load balancer",
        "cni"
    ],

    "Secrets Management": [
        "vault",
        "hashicorp vault"
    ],

    "Automation": [
        "python",
        "powershell"
    ]
}

def extract_categories(text):

    text = text.lower()

    found_categories = []

    for category, keywords in SKILL_CATEGORIES.items():

        for keyword in keywords:

            if keyword in text:

                found_categories.append(category)
                break

    return found_categories


def calculate_match(resume_text, jd_text):

    resume_text = resume_text.lower()
    jd_text = jd_text.lower()
    
    resume_categories = extract_categories(
    resume_text
    )

    jd_categories = extract_categories(
        jd_text
    )

    matched_skills = []

    missing_skills = []

    for category in jd_categories:

        if category in resume_categories:

            matched_skills.append(category)

        else:

            missing_skills.append(category)

    if len(jd_categories) == 0:

        return 0, [], []

    score = (
        len(matched_skills)
        / len(jd_categories)
    ) * 100

    return (
        round(score, 2),
        matched_skills,
        missing_skills
    )