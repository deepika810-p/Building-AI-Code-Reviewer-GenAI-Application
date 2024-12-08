# AI Code Reviewer - Streamlit Application

Welcome to the **AI Code Reviewer** application built using **Streamlit** and **Google Generative AI**. This tool allows developers to get real-time feedback on their code's quality, readability, efficiency, and adherence to best practices.

## Features

- **Code Review**: The AI reviews the code for logic correctness, potential bugs, vulnerabilities, and optimization.
- **Optimization Suggestions**: Provides actionable suggestions for improving performance and reducing redundancy.
- **Style Adherence**: Ensures the code follows style guides (e.g., PEP 8 for Python).
- **Documentation Feedback**: Analyzes the sufficiency of comments and docstrings.
- **Error Identification**: Identifies syntax errors, logical errors, and potential edge cases.
- **Refactoring Suggestions**: Offers recommendations for refactoring redundant or overly complex code.
- **Multi-language Support**: The AI can handle code in multiple languages, including Python, Java, C++, and JavaScript.

## Setup

### Prerequisites

- Python 3.7+
- Streamlit
- Google Generative AI API key

### Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/ai-code-reviewer.git
    cd ai-code-reviewer
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Obtain an API key from **Google Generative AI** and place it in the `API/keys/` folder with the filename `API_key.txt`.

4. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

    This will open the application in your default web browser.

## Code Overview

### 1. **API Key Configuration**:
   The Google Generative AI API key is read from the file `API_key.txt` to authenticate and connect to the AI service.

### 2. **System Prompt**:
   A system prompt is defined for the AI model, instructing it to review code for specific aspects, such as readability, efficiency, documentation, and error handling.

### 3. **Streamlit Interface**:
   The Streamlit application provides an interactive interface for users to input their code and receive feedback from the AI in real-time.

### 4. **Conversation History**:
   The session state is used to maintain a chat history, ensuring that past interactions with the AI are preserved across user inputs.

### 5. **Code Review**:
   The AI model reviews the code input by the user and returns feedback, including suggestions for improvement.

## Usage

1. Enter your code in the input box.
2. The AI will analyze the code and provide feedback, including:
   - Code analysis and error identification.
   - Suggestions for optimization and style adherence.
   - Feedback on documentation and code readability.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. We welcome improvements, bug fixes, and suggestions!

## Acknowledgments

- Thanks to **Streamlit** for providing a simple way to build interactive applications.
- Thanks to **Google Generative AI** for providing the AI model that powers the code review functionality.
