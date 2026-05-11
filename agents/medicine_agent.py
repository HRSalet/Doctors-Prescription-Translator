from utils.llm import llm

def extract_medicines(cleaned_text):

    prompt = f"""
    Extract:
    1. Medicine names
    2. Dosage
    3. Timing
    4. Duration

    Return JSON format.

    Text:
    {cleaned_text}
    """

    response = llm.invoke(prompt)
    return response.content