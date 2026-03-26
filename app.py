import streamlit as st
import random

st.set_page_config(page_title="Life Hack Bot", page_icon="💡")
st.title("💡 Life Hack Chatbot")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# LIFE HACK DATABASE (longer sentences)
life_hacks = {
    "study": [
        "Use the Pomodoro technique by studying for 25 minutes and then taking a 5-minute break, which helps you stay focused without getting too tired.",
        "Try teaching what you learn to someone else, because explaining things helps you understand and remember them much better.",
        "Study in a quiet and distraction-free place so your brain can fully focus on what you're learning."
    ],
    "sleep": [
        "Avoid using screens at least one hour before bed, because the blue light can make it harder for your brain to fall asleep.",
        "Keep your room dark and cool, as this creates the perfect environment for better sleep."
    ],
    "productivity": [
        "Make a simple to-do list every morning so you know exactly what you need to focus on during the day.",
        "Start with the hardest task first so the rest of your day feels easier and less stressful."
    ],
    "motivation": [
        "Start small and just begin, because taking the first step is always the hardest part.",
        "Celebrate small wins because they help build confidence and momentum."
    ]
    # You can add the rest of the categories here as before
}

# Function to build longer responses
def build_response(category, tip):
    intros = [
        "Here’s a useful life hack:",
        "You should try this:",
        "This might help you:",
        "A really good tip is:",
    ]

    explanations = [
        "This works because small habits repeated daily can create big results over time.",
        "Doing this regularly can seriously improve your daily routine.",
        "It may seem simple, but it actually improves your focus and efficiency a lot."
    ]

    bonus = [
        "Try combining this with other good habits for even better results.",
        "Start small and build it into your routine.",
        "Even doing this a few times a week helps."
    ]

    return f"{random.choice(intros)}\n\n👉 {tip}\n\n💡 {random.choice(explanations)}\n\n✅ {random.choice(bonus)}"

# Response function
def get_bot_response(user_input):
    text = user_input.lower()

    # Check if it’s math
    try:
        # Evaluate basic math expressions
        math_answer = eval(user_input, {"__builtins__": None}, {})
        return f"The answer to `{user_input}` is: {math_answer}"
    except:
        pass

    # Life hack matching
    for category in life_hacks:
        if category in text:
            tip = random.choice(life_hacks[category])
            return build_response(category, tip)

    if "tired" in text or "sleepy" in text:
        tip = random.choice(life_hacks.get("sleep", []))
        return build_response("sleep", tip)

    if "focus" in text:
        tip = random.choice(life_hacks.get("productivity", []))
        return build_response("productivity", tip)

    if "lazy" in text:
        tip = random.choice(life_hacks.get("motivation", []))
        return build_response("motivation", tip)

    if "study" in text or "exam" in text:
        tip = random.choice(life_hacks.get("study", []))
        return build_response("study", tip)

    return "I can give useful life hacks about study, sleep, productivity, motivation, and more. You can also ask me simple math questions like `2+2` or `12*5`."

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask me for a life hack or math question...")
if prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response
    response = get_bot_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
        
