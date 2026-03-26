import streamlit as st
from openai import OpenAI

# 🔑 Put your OpenAI API key here
client = OpenAI(api_key="YOUR_API_KEY_HERE")

st.set_page_config(page_title="Smart Chatbot", page_icon="🤖")

st.title("🤖 Smart Life Hacker Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to generate AI response
def get_bot_response():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )
    return response.choices[0].message.content

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Type your message here...")

if prompt:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    response = get_bot_response()

    # Save bot response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)
