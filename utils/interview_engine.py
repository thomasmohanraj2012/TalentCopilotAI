def generate_questions(matched_skills, missing_skills):

    questions = []

    for skill in matched_skills[:5]:
        questions.append(
            f"Can you explain your experience with {skill}?"
        )

    for skill in missing_skills[:3]:
        questions.append(
            f"Have you worked with {skill}? If not, how would you learn it?"
        )

    questions.extend(
        [
            "Describe a challenging technical problem you solved.",
            "How do you handle production incidents?",
            "Tell us about a project you are most proud of."
        ]
    )

    return questions