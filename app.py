import streamlit as st
import random
import re

st.set_page_config(page_title="Smart Chatbot", page_icon="🤖")

st.title("🤖 Smart Life Hacker Chatbot")

# Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = {}

# Smart response function
def get_bot_response(user_input):
    text = user_input.lower()

    # ========= BASIC KNOWLEDGE =========

    if "brush my teeth" in text:
        return "Brush your teeth twice a day for 2 minutes. Use toothpaste, move in circles, and don't forget your tongue! 🪥"

    if "1 liter" in text or "1 litre" in text:
        return "1 liter = 1000 milliliters (ml)."

    if "how much" in text and "liter" in text:
        return "1 liter equals 1000 milliliters (ml)."

    if "what is" in text:
        return "It depends — can you be more specific? 🤔"

    # ========= MATH =========

    try:
        # simple math detection
        if any(op in text for op in ["+", "-", "*", "/"]):
            result = eval(text)
            return f"The answer is {result}"
    except:
        pass

    # ========= MEMORY =========

    if "my name is" in text:
        name = text.split("my name is")[-1].strip()
        st.session_state.memory["name"] = name
        return f"Nice to meet you, {name}! 😊"

    if "what is my name" in text:
        if "name" in st.session_state.memory:
            return f"Your name is {st.session_state.memory['name']}!"
        else:
            return "I don't know your name yet. Tell me!"

    # ========= STUDY / LIFE =========

    if any(word in text for word in ["study", "exam", "homework"]):
        return random.choice([
            "Try studying in 25-minute sessions (Pomodoro method) 📚",
            "Practice active recall — test yourself!",
            "Remove distractions and focus on one task."
        ])

    if "sleep" in text:
        return "Try to get 7–9 hours of sleep and avoid screens before bed 😴"

    if any(word in text for word in ["lazy", "motivation"]):
        return "Start small. Even 5 minutes helps 💪"

    # ========= GREETING =========

    if any(word in text for word in ["hi", "hello", "hey"]):
        return random.choice([
            "Hey! 👋",
            "Hello! 😊",
            "Hi there!"
        ])

    if "bye" in text:
        return "Goodbye! 👋"

    # ========= DEFAULT =========

    return random.choice([
        "I don’t fully understand yet, but I’m learning! 🤔",
        "Can you explain that differently?",
        "That’s new to me — tell me more!",
        "I’m not sure, but I’m getting smarter!"
    ])

# Show chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
prompt = st.chat_input("Type your message here...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_bot_response(prompt)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
        
