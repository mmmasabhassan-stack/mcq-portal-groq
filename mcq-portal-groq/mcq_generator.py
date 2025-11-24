import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_mcqs(topic, level, count):
    prompt = f"""
    Generate {count} MCQs on the topic: '{topic}'.
    Difficulty: {level}.
    Format:

    1. Question text
       a) Option A
       b) Option B
       c) Option C
       d) Option D
       Correct answer: a
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",   # Make sure this is a supported model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content