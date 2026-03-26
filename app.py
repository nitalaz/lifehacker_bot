import streamlit as st
import random

st.set_page_config(page_title="Life Hack Bot", page_icon="💡")
st.title("💡 Life Hack Chatbot")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==============================
# LIFE HACK DATABASE (100+ hacks)
# ==============================
life_hacks = {
    "study": [
        "Use the Pomodoro technique: study 25 minutes and take a 5-minute break to stay focused without getting burned out.",
        "Teach what you learn to someone else to improve understanding and memory retention.",
        "Study in a quiet, distraction-free environment to maximize concentration.",
        "Write notes by hand as it helps you remember better than typing.",
        "Test yourself instead of just rereading notes to engage active recall.",
        "Use flashcards to memorize important information efficiently.",
        "Study the hardest subject first to use your peak energy effectively.",
        "Take short breaks during study sessions to maintain focus and energy.",
        "Listen to instrumental music while studying to improve concentration.",
        "Review notes before sleeping to strengthen memory consolidation.",
        "Use color-coded notes to organize information visually.",
        "Summarize each chapter in your own words for better understanding.",
        "Set small, achievable goals for each study session to stay motivated.",
        "Practice past exam questions to prepare effectively.",
        "Teach concepts aloud even to an imaginary audience to reinforce learning."
    ],

    "sleep": [
        "Avoid screens at least 1 hour before bed to improve sleep quality.",
        "Keep a consistent sleep schedule to regulate your internal clock.",
        "Make your room dark and cool to create the ideal sleep environment.",
        "Avoid caffeine in the evening to fall asleep easier.",
        "Listen to relaxing music or white noise to help calm your mind.",
        "Use your bed only for sleep to strengthen the sleep association.",
        "Wake up at the same time every day to maintain a healthy rhythm.",
        "Get sunlight in the morning to regulate your circadian rhythm.",
        "Exercise during the day to improve sleep quality at night.",
        "Avoid heavy meals close to bedtime to prevent discomfort while sleeping.",
        "Try gentle stretching or yoga before bed to relax your body.",
        "Write down worries before sleeping to clear your mind.",
        "Limit naps during the day to maintain deep nighttime sleep.",
        "Practice deep breathing or meditation before bed for relaxation.",
        "Use aromatherapy, like lavender, to create a calming sleep environment."
    ],

    "productivity": [
        "Make a daily to-do list to organize your tasks efficiently.",
        "Start with the hardest task first to tackle your day proactively.",
        "Remove distractions like your phone to increase focus.",
        "Break big tasks into smaller steps to make them manageable.",
        "Set deadlines for everything to stay accountable.",
        "Focus on one task at a time to maximize efficiency.",
        "Use timers to structure work sessions and breaks.",
        "Keep your workspace clean to enhance mental clarity.",
        "Reward yourself after finishing tasks to stay motivated.",
        "Plan your day the night before for a head start.",
        "Batch similar tasks together to save time.",
        "Use productivity apps to track progress and reminders.",
        "Prioritize tasks based on importance and urgency.",
        "Limit multitasking as it reduces focus and efficiency.",
        "Review your achievements at the end of the day for motivation."
    ],

    "health": [
        "Drink plenty of water throughout the day to stay hydrated.",
        "Walk at least 30 minutes daily to maintain physical health.",
        "Eat more fruits and vegetables to improve nutrition.",
        "Stretch every morning to improve flexibility and circulation.",
        "Don’t skip breakfast to fuel your body for the day.",
        "Exercise regularly to boost energy and mood.",
        "Take deep breaths to reduce stress and improve focus.",
        "Limit sugary drinks to maintain consistent energy levels.",
        "Wash your hands often to prevent illness.",
        "Stand up and move every hour to improve circulation.",
        "Incorporate strength training to build muscle and metabolism.",
        "Practice mindfulness or meditation to support mental health.",
        "Avoid smoking and excessive alcohol for better overall health.",
        "Take regular breaks during work to reduce physical strain.",
        "Sleep at least 7–8 hours per night to maintain well-being."
    ],

    "money": [
        "Save a small amount of money every week to build long-term savings.",
        "Track your spending to understand where your money goes.",
        "Avoid impulse purchases by planning before buying.",
        "Set a monthly budget to control expenses.",
        "Compare prices before buying to get the best deal.",
        "Use discounts and coupons when possible to save money.",
        "Cook at home more often to reduce eating out costs.",
        "Set financial goals to stay motivated with saving.",
        "Avoid unnecessary subscriptions that drain money.",
        "Buy only what you need instead of excess items.",
        "Invest small amounts to grow your wealth over time.",
        "Keep an emergency fund for unexpected expenses.",
        "Review bank statements to identify unnecessary charges.",
        "Pay off high-interest debts first to save money.",
        "Plan purchases in advance to avoid stress and overspending."
    ],

    "cleaning": [
        "Clean as you go to prevent mess from building up.",
        "Set a timer for 10 minutes and clean quickly to make it manageable.",
        "Do small cleaning tasks daily to stay organized.",
        "Keep cleaning supplies in one place for efficiency.",
        "Make your bed every morning to instantly improve your room’s look.",
        "Use baking soda for tough stains as a natural cleaner.",
        "Declutter one area at a time to avoid overwhelm.",
        "Do laundry regularly to prevent clothing piles.",
        "Wipe surfaces daily to maintain cleanliness.",
        "Organize before cleaning to work smarter, not harder.",
        "Vacuum high-traffic areas often to reduce dust accumulation.",
        "Use storage boxes to keep similar items together.",
        "Clean your kitchen after cooking to prevent buildup.",
        "Disinfect commonly touched surfaces regularly for hygiene.",
        "Create a weekly cleaning schedule for consistency."
    ],

    "social": [
        "Listen more than you talk to understand others better.",
        "Make eye contact to show confidence and attentiveness.",
        "Smile to appear friendly and approachable.",
        "Remember people’s names to create a personal connection.",
        "Be kind and respectful in conversations.",
        "Ask questions to show genuine interest.",
        "Stay positive to create enjoyable interactions.",
        "Avoid interrupting to show consideration.",
        "Be confident but polite in expressing your opinions.",
        "Practice good manners in all situations.",
        "Offer help when someone needs it to build trust.",
        "Send thank-you notes to show appreciation.",
        "Give compliments genuinely to strengthen relationships.",
        "Join clubs or communities to meet new people.",
        "Participate actively in conversations to stay engaged."
    ],

    "technology": [
        "Use keyboard shortcuts to save time while working.",
        "Organize your files into folders for easy access.",
        "Back up important data regularly to prevent loss.",
        "Keep software updated for security and efficiency.",
        "Use strong passwords to protect online accounts.",
        "Limit screen time to prevent eye strain and fatigue.",
        "Turn off unnecessary notifications to reduce distractions.",
        "Use dark mode at night to protect your eyes.",
        "Clean device storage regularly to maintain speed.",
        "Learn basic tech skills to solve common issues.",
        "Use cloud storage to access files anywhere.",
        "Secure your devices with antivirus software.",
        "Enable two-factor authentication for added security.",
        "Regularly clear browser history and cache for performance.",
        "Update device firmware to fix bugs and improve functionality."
    ],

    "motivation": [
        "Start small and just begin, because taking the first step is the hardest.",
        "Set clear goals to know exactly what you’re working towards.",
        "Track progress to stay motivated and see improvement.",
        "Celebrate small wins to boost confidence.",
        "Stay consistent even when progress seems slow.",
        "Visualize success to maintain focus.",
        "Surround yourself with positive people for support.",
        "Take breaks to avoid burnout and maintain energy.",
        "Don’t compare yourself to others; focus on your journey.",
        "Keep going even when it’s difficult; persistence pays off.",
        "Write down your goals to make them tangible.",
        "Reward yourself after achieving milestones.",
        "Remind yourself why you started to stay motivated.",
        "Read inspiring quotes or books to fuel determination.",
        "Reflect on past achievements to gain confidence."
    ]
}

# ====================================
# Function to build longer chatbot replies
# ====================================
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

# ====================================
# Response function (life hacks + math)
# ====================================
def get_bot_response(user_input):
    text = user_input.lower()

    # Check if it’s math
    try:
        math_answer = eval(user_input, {"__builtins__": None}, {})
        return f"The answer to `{user_input}` is: {math_answer}"
    except:
        pass

    # Match life hack categories
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

    return "I can give useful life hacks about study, sleep, productivity, motivation, health, money, cleaning, social, and technology. You can also ask me math questions like `2+2` or `12*5`."

# ===============================
# Display chat messages
# ===============================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask me for a life hack or math question...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_bot_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
        
