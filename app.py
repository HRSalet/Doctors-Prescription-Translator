import streamlit as st
from ocr.extract_text import extract_text
from graph.workflow import app

st.title("Doctor Prescription Translator")

uploaded = st.file_uploader(
    "Upload Prescription",
    type=["png","jpg","jpeg"]
)

if uploaded:

    with open("temp.png","wb") as f:
        f.write(uploaded.read())
    
    raw_text = extract_text("temp.png")

    st.subheader("Raw OCR Text")
    st.write(raw_text)

    result = app.invoke({
        "raw_text": raw_text
    })

    st.subheader("Cleaned Prescription")
    st.write(result["cleaned_text"])

    st.subheader("Medicine Details")
    st.write(result["medicines"])