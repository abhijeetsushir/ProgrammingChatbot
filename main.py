import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables. Please set it in .env file")

def ask_groq(prompt, history=[]):
    messages = history + [{"role": "user", "content": prompt}]
    url = "https://api.groq.com/openai/v1/chat/completions"  # Use correct Groq endpoint

    response = requests.post(
        url,
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": "llama3-70b-8192",  # Groq's model name
            "messages": messages,
            "temperature": 0.5
        }
    )
    return response.json()["choices"][0]["message"]["content"]

# Test the API
if __name__ == "__main__":
    try:
        test_prompt = "Hello, how are you?"
        print("Testing Groq API...")
        response = ask_groq(test_prompt)
        print("\nResponse from Groq API:")
        print(response)
        print("\nAPI is working correctly!")
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
