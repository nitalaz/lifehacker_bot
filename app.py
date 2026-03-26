import streamlit as st
import random

st.set_page_config(page_title="Life Hack Bot", page_icon="💡")

st.title("💡 Life Hack Chatbot")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# ===== LIFE HACK DATABASE =====
life_hacks = {
    "study": [
        "Use the Pomodoro technique: 25 min study, 5 min break 📚",
        "Teach what you learn — it helps you remember better.",
        "Study in a clean, quiet space."
    ],
    "sleep": [
        "Avoid screens 30 minutes before bed 😴",
        "Sleep at the same time every night.",
        "Keep your room cool and dark."
    ],
    "focus": [
        "Turn off notifications 🔕",
        "Work in short bursts.",
        "Use a timer to stay on track."
    ],
    "clean": [
        "Clean for 10 minutes daily to avoid mess.",
        "Start with the smallest task first.",
        "Use a checklist to stay organized."
    ],
    "phone": [
        "Put your phone in another room while working 📵",
        "Use grayscale mode to reduce screen addiction.",
        "Delete apps you don’t need."
    ],
    "motivation": [
        "Start small — even 5 minutes helps 💪",
        "Don’t wait to feel motivated — just begin.",
        "Set tiny goals and build up."
    ],
    "food": [
        "Drink water before meals to avoid overeating 💧",
        "Prepare meals ahead of time.",
        "Eat slowly to enjoy your food."
    ],
    "health": [
        "Walk at least 10 minutes a day 🚶",
        "Stretch regularly.",
        "Drink more water."
    ],
    "time": [
        "Make a to-do list every morning 📝",
        "Do the hardest task first.",
        "Limit distractions."
    ],
    "memory": [
        "Repeat information out loud 🧠",
        "Write things down.",
        "Use associations to remember."
    ]
}

# Add more hacks to reach ~100
extra_hacks = [
    "Use cold water to wake up faster 🚿",
    "Set alarms for important tasks ⏰",
    "Break big tasks into smaller steps",
    "Keep your workspace clean",
    "Reward yourself after finishing tasks",
    "Listen to music to stay focused 🎧",
    "Use sticky notes for reminders",
    "Drink water when you feel tired",
    "Take short breaks to stay productive",
    "Plan your day the night before",
    "Use keyboard shortcuts to save time",
    "Keep things in the same place",
    "Wake up at the same time daily",
    "Smile — it improves your mood 😊",
    "Exercise in the morning for energy",
    "Avoid multitasking",
    "Write goals down",
    "Track your habits",
    "Use a calendar",
    "Limit social media time",
]

# ===== RESPONSE FUNCTION =====
def get_bot_response(user_input):
    text = user_input.lower()

    # Search for matching category
    for key in life_hacks:
        if key in text:
            return random.choice(life_hacks[key])

    # Specific questions
    if "how to brush" in text:
        return "Brush for 2 minutes, use toothpaste, and clean all sides of your teeth 🪥"

    if "how to wake up" in text:
        return random.choice([
            "Put your alarm far away so you have to get up ⏰",
            "Drink water right after waking up 💧",
            "Get sunlight early 🌞"
        ])

    if "how to study better" in text:
        return random.choice(life_hacks["study"])

    # Random hack fallback
    return random.choice(extra_hacks)

# ===== DISPLAY CHAT =====
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ===== INPUT =====
prompt = st.chat_input("Ask for a life hack...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_bot_response(prompt)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
        
