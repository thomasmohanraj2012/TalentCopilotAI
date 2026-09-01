def evaluate_answer(answer):

    answer = answer.strip()

    word_count = len(answer.split())

    if word_count >= 100:
        return 9

    elif word_count >= 50:
        return 7

    elif word_count >= 20:
        return 5

    return 3