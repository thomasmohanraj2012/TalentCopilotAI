def evaluate_answer(answer):
    """
    Deterministic response-length scoring.

    Returns a tuple: (score, feedback)
    """

    answer = answer.strip()

    word_count = len(answer.split())

    if word_count >= 100:
        return 9, "Detailed, well-explained response."

    elif word_count >= 50:
        return 7, "Good level of detail."

    elif word_count >= 20:
        return 5, "Reasonable answer, could use more detail."

    return 3, "Answer is quite brief — consider elaborating."


def evaluate_answer_score(answer):
    """
    Convenience helper that returns only the numeric score,
    for places that don't need the feedback text.
    """

    score, _ = evaluate_answer(answer)
    return score