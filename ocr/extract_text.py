import easyocr

reader = easyocr.Reader(['en'])

def extract_text(image_path):
    results = reader.readtext(image_path)
    text = " ".join([res[1] for res in results])
    return text