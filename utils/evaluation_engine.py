def evaluate_candidate(score):

    if score >= 85:
        recommendation = "Strong Candidate ✅"

    elif score >= 70:
        recommendation = "Good Candidate 👍"

    elif score >= 50:
        recommendation = "Moderate Match ⚠️"

    else:
        recommendation = "Not Recommended ❌"

    return recommendation