from utils.llm import llm

def cleanup_prescription(raw_text):

    prompt = f"""
    You are a medical prescription cleaner.

    Correct OCR mistakes carefully.
    Expand medical abbreviations.
    Preserve medicine names.

    Prescription:
    {raw_text}

    Return cleaned prescription only.
    """

    response = llm.invoke(prompt)
    return response.content