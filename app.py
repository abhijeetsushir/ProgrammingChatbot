import streamlit as st
from main import ask_groq
import json
import os

# Set page config
st.set_page_config(
    page_title="Programmer's AI Assistant",
    page_icon="💻",
    layout="wide"
)

# Initialize session state for chat history and user info
if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# Sidebar for user information
with st.sidebar:
    st.title("👨‍💻 Programmer's AI Assistant")
    st.write("---")
    
    # Get user's name
    if not st.session_state.user_name:
        user_name = st.text_input("What's your name?")
        if user_name:
            st.session_state.user_name = user_name
            st.success(f"Welcome, {user_name}!")
    else:
        st.write(f"Welcome back, {st.session_state.user_name}!")
    
    st.write("---")
    st.write("### About")
    st.write("This AI assistant helps you with:")
    st.write("- Syntax references")
    st.write("- Code understanding")
    st.write("- Conceptual guidance")
    st.write("- Multi-step problem solving")
    st.write("---")
    st.write("### Supported Languages")
    st.write("Python, JavaScript, and more!")

# Main chat interface
st.title("💬 Programmer's Chat Assistant")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything about programming..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Prepare context for the AI
    context = f"User's name: {st.session_state.user_name}\nPrevious conversation:\n"
    for msg in st.session_state.messages[-5:]:  # Include last 5 messages for context
        context += f"{msg['role']}: {msg['content']}\n"
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = ask_groq(prompt, st.session_state.messages)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"An error occurred: {str(e)}") 