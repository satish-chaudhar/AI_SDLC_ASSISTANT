import streamlit as st
import requests

st.title("GenAI SDLC Architect Assistant")

phase = st.selectbox("Select SDLC Phase", ["Requirements", "Design", "Development", "Testing", "Deployment"])

uploaded_file = st.file_uploader("Upload SDLC Document (PDF)", type=["pdf"])
if uploaded_file:
    with open(f"documents/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.read())
    res = requests.post("http://localhost:8000/upload/", files={"file": uploaded_file})
    st.success("Document Uploaded & Embedded")

query = st.text_input("Ask your SDLC question:")
if st.button("Ask"):
    # Add your retrieval + LLM call here in next step
    st.info("Coming soon: LLM answer will appear here.")
