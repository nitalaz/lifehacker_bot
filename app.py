import streamlit as st
import random

st.set_page_config(page_title="Life Hack Bot", page_icon="💡")

st.title("💡 Life Hack Chatbot")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# LIFE HACK DATABASE (100+ ideas grouped)
life_hacks = {
    "study": [
        "Use the Pomodoro technique: 25 min focus + 5 min break.",
        "Teach what you learn to someone else.",
        "Study in a quiet, distraction-free place.",
        "Write notes by hand to remember better.",
        "Test yourself instead of rereading notes.",
        "Use flashcards for memorization.",
        "Study the hardest subject first.",
        "Take short breaks to stay focused.",
        "Use music without lyrics to concentrate.",
        "Review notes before sleeping."
    ],

    "sleep": [
        "Avoid screens 1 hour before bed.",
        "Go to sleep at the same time every night.",
        "Keep your room dark and cool.",
        "Don’t drink caffeine before bed.",
        "Try relaxing music or white noise.",
        "Use your bed only for sleep.",
        "Wake up at the same time daily.",
        "Get sunlight in the morning.",
        "Exercise during the day for better sleep.",
        "Avoid heavy meals before bed."
    ],

    "productivity": [
        "Make a to-do list every morning.",
        "Start with the hardest task first.",
        "Remove distractions like your phone.",
        "Break big tasks into small steps.",
        "Set deadlines for everything.",
        "Focus on one task at a time.",
        "Use timers to stay on track.",
        "Clean your workspace.",
        "Reward yourself after finishing tasks.",
        "Plan your day the night before."
    ],

    "health": [
        "Drink more water throughout the day.",
        "Walk at least 30 minutes daily.",
        "Eat more fruits and vegetables.",
        "Stretch every morning.",
        "Don’t skip breakfast.",
        "Exercise regularly.",
        "Take deep breaths to reduce stress.",
        "Limit sugary drinks.",
        "Wash your hands often.",
        "Stand up and move every hour."
    ],

    "cleaning": [
        "Clean as you go to avoid mess buildup.",
        "Set a timer for 10 minutes to clean quickly.",
        "Do small cleaning tasks daily.",
        "Keep supplies in one place.",
        "Make your bed every morning.",
        "Use baking soda for tough stains.",
        "Declutter one area at a time.",
        "Do laundry regularly.",
        "Wipe surfaces daily.",
        "Organize before cleaning."
    ],

    "money": [
        "Save a small amount every week.",
        "Track your spending.",
        "Avoid impulse buying.",
        "Set a budget.",
        "Compare prices before buying.",
        "Use discounts and coupons.",
        "Cook at home instead of eating out.",
        "Set financial goals.",
        "Avoid unnecessary subscriptions.",
        "Buy only what you need."
    ],

    "social": [
        "Listen more than you talk.",
        "Make eye contact when speaking.",
        "Smile to appear friendly.",
        "Remember people’s names.",
        "Be kind and respectful.",
        "Ask questions to show interest.",
        "Stay positive in conversations.",
        "Avoid interrupting others.",
        "Be confident but polite.",
        "Practice good manners."
    ],

    "technology": [
        "Use keyboard shortcuts to save time.",
        "Organize your files into folders.",
        "Back up important data.",
        "Keep your software updated.",
        "Use strong passwords.",
        "Limit screen time.",
        "Turn off unnecessary notifications.",
        "Use dark mode at night.",
        "Clean your device storage regularly.",
        "Learn basic tech skills."
    ],

    "motivation": [
        "Start small — just begin.",
        "Set clear goals.",
        "Track your progress.",
        "Celebrate small wins.",
        "Stay consistent.",
        "Visualize success.",
        "Surround yourself with positive people.",
        "Take breaks when needed.",
        "Don’t compare yourself to others.",
        "Keep going even when it’s hard."
    ],

    "school": [
        "Pay attention in class.",
        "Ask questions when confused.",
        "Review notes daily.",
        "Stay organized.",
        "Do homework on time.",
        "Participate in discussions.",
        "Use planners for assignments.",
        "Study a little every day.",
        "Avoid procrastination.",
        "Prepare for tests early."
    ]
}

# Response function
def get_bot_response(user_input):
    text = user_input.lower()

    # Find matching category
    for category in life_hacks:
        if category in text:
            return random.choice(life_hacks[category])

    # Extra smart matching
    if "tired" in text or "sleepy" in text:
        return random.choice(life_hacks["sleep"])

    if "focus" in text:
        return random.choice(life_hacks["productivity"])

    if "lazy" in text:
        return random.choice(life_hacks["motivation"])

    if "study" in text or "exam" in text:
        return random.choice(life_hacks["study"])

    # Fallback
    return "I can give life hacks about study, sleep, money, health, productivity and more! Try asking about one of those 💡"

# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
prompt = st.chat_input("Ask me for a life hack...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_bot_response(prompt)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
