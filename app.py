import streamlit as st
import openai
from sdlc_prompts import generate_architecture_prompt

openai.api_key = "your-api-here"

st.set_page_config(page_title="GenAI SDLC Architect Assistant", layout="wide")

st.title("🧠 GenAI SDLC Architect Assistant")

project_description = st.text_area("📄 Enter your Project Requirements", height=300)

if st.button("Generate SDLC Architecture Plan"):
    with st.spinner("Thinking..."):
        prompt = generate_architecture_prompt(project_description)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        result = response.choices[0].message["content"]
        st.markdown("### ✅ SDLC Architecture Suggestion")
        st.markdown(result)
