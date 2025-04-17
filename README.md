# Programmer's AI Assistant

A real-time AI chatbot that helps programmers quickly find syntax references, understand code, and get conceptual guidance across multiple programming languages.

## Features

- Real-time chat interface
- Context-aware conversations
- Personalized sessions with user name
- Support for multiple programming languages
- Fast and responsive web interface
- Powered by Groq's Llama 3.3 70B model

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Running Locally

To run the application locally:
```bash
streamlit run app.py
```

## Deployment

This application can be deployed on Streamlit Cloud:

1. Create a Streamlit Cloud account
2. Connect your GitHub repository
3. Set the following environment variables in Streamlit Cloud:
   - `GROQ_API_KEY`: Your Groq API key

## Usage

1. Enter your name when prompted
2. Start asking programming-related questions
3. The AI will maintain context throughout the conversation
4. Get help with:
   - Syntax references
   - Code understanding
   - Conceptual guidance
   - Multi-step problem solving

## Supported Languages

- Python
- JavaScript
- And more! 