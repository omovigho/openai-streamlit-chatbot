# AI Conversational Chatbot using OpenAI API with Streamlit UI, Chat History Logging, and File Saving

import openai
import os
import streamlit as st
import json
from datetime import datetime

# Set your OpenAI API key here from environmental variable
openai.api_key = os.getenv("OPENAI_API_KEY")  # or directly assign the key for local use


def chat_with_openai(prompt, chat_history=[]):
    messages = chat_history + [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # you can also use "gpt-4" if you have access
        messages=messages,
        max_tokens=150,
        temperature=0.7
    )

    reply = response.choices[0].message.content
    chat_history.append({"role": "user", "content": prompt})
    chat_history.append({"role": "assistant", "content": reply})
    return reply, chat_history


def save_chat_log(history, filename="chat_history.json"):
    with open(filename, "w") as f:
        json.dump(history, f, indent=4)


# Streamlit UI
st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🤖 AI Conversational Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="input")
submit = st.button("Send")

if submit and user_input:
    reply, st.session_state.chat_history = chat_with_openai(user_input, st.session_state.chat_history)
    st.write(f"**AI:** {reply}")

    # Display full chat history
    st.subheader("Chat History")
    for msg in st.session_state.chat_history:
        role = "You" if msg["role"] == "user" else "AI"
        st.write(f"**{role}:** {msg['content']}")

    # Save chat history
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_chat_log(st.session_state.chat_history, f"chat_{timestamp}.json")

st.caption("Powered by OpenAI")
