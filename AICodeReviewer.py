import streamlit as st
import google.generativeai as genai
from streamlit.components.v1 import html
import os

file_path = r"C:\Users\P.DEEPIKA\Desktop\API_key.txt"
if os.path.exists(file_path):
    with open(file_path) as f:
        key = f.read()
else:
    print("Error: The file does not exist at the specified path.")




# Configure the Google Generative AI API
genai.configure(api_key="AIzaSyCAt3WebzN9q3XcLEMLUdd5sKQLkLPnxGA")

# Define the system prompt for the AI reviewer
sys_prompt = """You are an advanced AI specialized in reviewing code for quality, readability, efficiency, and adherence to best practices. 
                Your tasks include:
                Code Analysis: Examine code for logic correctness, potential bugs, and vulnerabilities.
                Optimization: Suggest improvements to make the code faster, cleaner, and more efficient.
                Style Adherence: Ensure the code follows the given style guide (e.g., PEP 8 for Python, Google's Java Style Guide).
                Documentation: Assess the sufficiency of comments and docstrings, and recommend improvements if needed.
                Error Identification: Highlight syntax errors, logical errors, and potential edge cases.
                Code Refactoring: Provide actionable suggestions for refactoring redundant or overly complex code.
                Feedback Tone: Deliver feedback that is constructive, clear, and helpful, making it easy for developers to act upon.
                You can handle code in multiple languages (e.g., Python, Java, C++, JavaScript).

                When reviewing, provide:
                A summary of the overall assessment.
                Specific suggestions for improvement with examples if needed.
                A rating for code quality on a scale from 1 to 10."""

# Initialize the AI model for code review
AICodeReviewer = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest", system_instruction=sys_prompt)
CodeReview = AICodeReviewer.start_chat(history=[])

# Streamlit title and heading
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #FF6347; /* Tomato red */
            text-align: center;
            background-color: #FFFFE0; /* Light yellow background */
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .subtitle {
            font-size: 24px;
            color: #4682B4; /* Steel blue */
            text-align: center;
            margin-top: 20px;
        }
        .heading {
            font-size: 28px;
            font-weight: bold;
            color: #8A2BE2; /* Blue violet */
            text-align: center;
            padding-bottom: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="title">Welcome to the AI Code Reviewer! 🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Improve your code quality with AI suggestions.</div>', unsafe_allow_html=True)

# Initialize session state for conversation history
if "history" not in st.session_state:
    st.session_state.history = []
    st.session_state.history.append({"ai": "Hello! 👋 I'm your AI-powered code reviewer. Ready to assist with improving your code's quality, readability, and performance. How can I help you today?"})

# Display the main chat window with history
for message in st.session_state.history:
    if "user" in message:
        st.chat_message("human").write(message["user"])
    if "ai" in message:
        st.chat_message("ai").write(message["ai"])

# Get user input
human_prompt = st.chat_input("Type your code or question here to get feedback...")

if human_prompt:
    st.chat_message("human").write(human_prompt)
    st.session_state.history.append({"user": human_prompt})

    response = CodeReview.send_message(human_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state.history.append({"ai": response.text})
