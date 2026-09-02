"""
Follow-up question generator for TalentCopilotAI.

This module is intentionally provider-agnostic:

    - Today it runs on a deterministic fallback, so the demo
      works with zero external API calls and zero approval
      requirements.

    - Later, once you have access to an approved Comcast LLM
      endpoint (e.g. DevX LLM Gateway), you only need to fill
      in the body of `_call_llm()`. Nothing else in the app
      needs to change.
"""


def _call_llm(prompt):
    """
    Placeholder for an approved LLM call.

    Replace the body of this function with a call to your
    approved Comcast LLM Gateway client, keeping the same
    contract: a prompt string in, a plain text answer out.
    """

    # TODO: Wire this up once LLM Gateway access is approved.
    #
    # from approved_llm_client import chat_completion
    # response = chat_completion(prompt=prompt, max_tokens=100)
    # return response.text.strip()

    return None


def generate_followup_question(
    question,
    answer,
    expected_topics=None
):
    """
    Generate one natural follow-up question based on the
    candidate's answer.

    Falls back to a deterministic template when no LLM is
    configured, so this always returns something usable.
    """

    answer = (answer or "").strip()

    if not answer:
        return None

    expected_topics = expected_topics or []

    prompt = f"""
You are assisting a technical interviewer.
Do not decide whether to hire the candidate.
Generate exactly ONE short, natural follow-up question.

Original question:
{question}

Candidate's answer:
{answer}

Topics an ideal answer might cover:
{", ".join(expected_topics) if expected_topics else "general technical depth"}

Return only the follow-up question text.
"""

    llm_response = _call_llm(prompt)

    if llm_response:
        return llm_response.strip()

    return _fallback_followup(answer, expected_topics)


def _fallback_followup(answer, expected_topics):
    """
    Deterministic fallback used until an approved LLM is wired in.
    """

    lowered = answer.lower()

    missing_topics = [
        topic
        for topic in expected_topics
        if topic.lower() not in lowered
    ]

    if missing_topics:
        return (
            "Can you also walk me through how you approach "
            f"{missing_topics[0]}?"
        )

    if len(answer.split()) < 15:
        return "Could you expand on that with a specific example?"

    return (
        "What was the most challenging part of that, and how "
        "did you resolve it?"
    )