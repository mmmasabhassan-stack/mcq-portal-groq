import streamlit as st
from mcq_generator import generate_mcqs

st.set_page_config(page_title="MCQ Generator", layout="centered")

st.title("📘 MCQ Generator using Groq API")

topic = st.text_input("Enter Topic:")
difficulty = st.selectbox("Select Difficulty Level:", ["Easy", "Medium", "Hard"])
count = st.number_input("Number of MCQs:", min_value=1, max_value=50, value=5)

if st.button("Generate MCQs"):
    if not topic.strip():
        st.error("Please enter a topic!")
    else:
        st.info("Generating MCQs... please wait...")
        mcqs = generate_mcqs(topic, difficulty, count)
        st.success("Done! Your MCQs are below:")

        st.write(mcqs)

        st.download_button("Download MCQs", mcqs, file_name="mcqs.txt")