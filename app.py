import streamlit as st
import random

st.set_page_config(page_title="Life Hacker Chatbot", page_icon="🤖")

st.title("🤖 Life Hacker Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Smarter response function
def get_bot_response(user_input):
    text = user_input.lower()

    # Greetings
    if any(word in text for word in ["hi", "hello", "hey"]):
        return random.choice([
            "Hey! 👋 What can I help you with?",
            "Hi there! 😊",
            "Hello! Ask me anything!"
        ])

    # How are you
    elif "how are you" in text:
        return random.choice([
            "I'm doing great 😄 How about you?",
            "All good here! Ready to help 💪"
        ])

    # Name
    elif "your name" in text:
        return "I'm your life hacker bot 😎"

    # Study tips
    elif any(word in text for word in ["study", "homework", "exam"]):
        return random.choice([
            "Try the Pomodoro technique: 25 min study + 5 min break 📚",
            "Turn off distractions and focus on one task at a time.",
            "Practice active recall instead of just rereading notes!"
        ])

    # Sleep
    elif "sleep" in text:
        return random.choice([
            "Try to get 7–9 hours of sleep 😴",
            "Avoid screens before bed for better sleep.",
            "Keep a consistent sleep schedule!"
        ])

    # Motivation
    elif any(word in text for word in ["motivate", "lazy", "tired"]):
        return random.choice([
            "Start small — even 5 minutes helps 💪",
            "Discipline beats motivation 🔥",
            "Just begin. You’ll feel better once you start."
        ])

    # Productivity
    elif any(word in text for word in ["productive", "focus", "time"]):
        return random.choice([
            "Make a to-do list and prioritize tasks ✅",
            "Remove distractions (phone, notifications)",
            "Work in short focused bursts!"
        ])

    # Goodbye
    elif any(word in text for word in ["bye", "goodbye"]):
        return "Goodbye! 👋 Come back anytime!"

    # Fallback (better than before)
    else:
        return random.choice([
            "Hmm, can you explain that a bit more?",
            "I’m still learning — tell me more!",
            "Interesting… what do you mean exactly?",
            "I’m not sure yet, but I’d love to learn more!"
        ])

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

    # Generate response
    response = get_bot_response(prompt)

    # Save bot response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)
        
