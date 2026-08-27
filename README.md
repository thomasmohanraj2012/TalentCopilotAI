# 🤖 TalentCopilotAI

TalentCopilotAI is an AI-powered recruitment intelligence platform designed to streamline candidate screening, technical interviewing and hiring decision support.

The platform combines resume analysis, job description matching, AI-generated interview questions, voice-based interviews and candidate assessment into a single enterprise-ready experience.

---

## 🎯 Key Features

### 📄 Resume Intelligence

- Upload candidate resumes in PDF or DOCX format
- Extract and analyse resume content
- Identify technical skills and competencies
- Compare candidate profile against job requirements
- Calculate candidate-job match score

---

### 🎯 Job Description Matching

TalentCopilotAI analyses both:

- Candidate Resume
- Job Description

to identify:

✅ Matched Skills

⚠ Missing Skills

📊 Match Percentage

📋 Hiring Recommendation

---

### 🎤 AI Interview Generator

The platform dynamically generates interview questions based on:

- Resume content
- Job description requirements
- Technical skills identified
- Skill gaps detected

Question categories include:

- Kubernetes
- AWS
- VMware
- Linux
- Terraform
- Infrastructure as Code
- CI/CD
- Automation
- Leadership
- Behavioural Assessment

---

### 🎙 Voice Interview Module

Candidates can:

- Listen to interview questions
- Record responses using voice
- Automatically convert speech to text
- Review and edit transcripts
- Save responses for assessment

---

### 📊 Interview Assessment

After interview completion, TalentCopilotAI automatically:

- Captures candidate responses
- Calculates interview scores
- Measures response quality
- Generates hiring insights
- Produces recruiter-friendly interview summaries

---

### 📈 Executive Insights

Provides hiring managers and recruiters with:

- Resume Match Scores
- Skills Analysis
- Interview Assessments
- Hiring Recommendations
- Candidate Evaluation Dashboards

---

## 🏗 Solution Architecture

```text
TalentCopilotAI
│
├── Resume Intelligence
│   ├── Resume Parser
│   ├── Skill Extraction
│   └── JD Matching
│
├── Interview Intelligence
│   ├── Question Generation
│   ├── Voice Interview
│   ├── Transcript Capture
│   └── Assessment Engine
│
├── Scoring Engine
│
└── Executive Insights
```

---

## 🛠 Technology Stack

### Frontend

- Streamlit
- HTML/CSS
- Responsive Enterprise UI

### Backend

- Python

### AI Components

- Resume Parsing
- Skill Categorisation
- JD Matching
- Interview Intelligence
- Candidate Assessment

### Voice Technologies

- Speech-to-Text
- Browser Speech Synthesis API

---

## 📂 Project Structure

```text
TalentCopilotAI/
│
├── app.py
│
├── engines/
│   ├── resume_engine.py
│   ├── interview_engine.py
│   ├── scoring_engine.py
│   └── insights_engine.py
│
├── utils/
│   ├── resume_parser.py
│   ├── jd_matcher.py
│   ├── evaluation_engine.py
│   ├── interview_engine.py
│   ├── voice_interview.py
│   └── answer_evaluator.py
│
└── requirements.txt
```

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/thomasmohanraj2012/TalentCopilotAI.git
```

### Navigate to Project

```bash
cd TalentCopilotAI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🧪 Sample Workflow

### Step 1

Upload Candidate Resume

### Step 2

Paste Job Description

### Step 3

Generate Candidate Analysis

### Step 4

Review:

- Match Score
- Matched Skills
- Missing Skills

### Step 5

Generate AI Interview Questions

### Step 6

Conduct Voice Interview

### Step 7

View Candidate Assessment Summary

---

## 🎯 Future Roadmap

- Large Language Model Integration
- Enterprise LLM Gateway Support
- AI Answer Evaluation
- Candidate Ranking
- Advanced Hiring Insights
- Interview Analytics
- Recruiter Copilot
- Multi-Role Interview Templates

---

## 👨‍💻 Author

**Thomas Mohanraj**

DevOps Manager | AI Enthusiast | Platform Engineer

Creator of:

- TalentCopilotAI
- Kubernetes Lab in a Box

GitHub:

https://github.com/thomasmohanraj2012

---

## 📜 License

This project is intended for learning, innovation and enterprise recruitment workflow experimentation.


