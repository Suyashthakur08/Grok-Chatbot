import streamlit as st
from chatbot import chat_with_llm

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Chat with LLaMA 3 (Groq API)")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", key="input")

if user_input:
    response = chat_with_llm(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

for sender, message in reversed(st.session_state.history):
    st.markdown(f"**{sender}:** {message}")