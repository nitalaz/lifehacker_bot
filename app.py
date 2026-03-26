import streamlit as st
import random

st.set_page_config(page_title="Life Hack Bot", page_icon="💡")

st.title("💡 Life Hack Chatbot")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# LIFE HACK DATABASE (longer sentences now)
life_hacks = {
    "study": [
        "Use the Pomodoro technique by studying for 25 minutes and then taking a 5-minute break, which helps you stay focused without getting too tired.",
        "Try teaching what you learn to someone else, because explaining things helps you understand and remember them much better.",
        "Study in a quiet and distraction-free place so your brain can fully focus on what you're learning.",
        "Write your notes by hand instead of typing, since this helps improve memory and understanding.",
        "Test yourself regularly instead of just rereading notes, because active recall is much more effective.",
        "Use flashcards to memorize important information, especially for definitions and key concepts.",
        "Start with the hardest subject first so you use your energy when your brain is most focused.",
        "Take short breaks while studying to avoid burnout and keep your concentration strong.",
        "Listen to music without lyrics while studying, as it can help you stay focused without distractions.",
        "Review your notes before going to sleep, since your brain processes information better overnight."
    ],

    "sleep": [
        "Avoid using screens at least one hour before bed, because the blue light can make it harder for your brain to fall asleep.",
        "Try to go to sleep at the same time every night so your body builds a consistent sleep routine.",
        "Keep your room dark and cool, as this creates the perfect environment for better sleep.",
        "Avoid drinking caffeine in the evening since it can keep you awake longer than you expect.",
        "Try relaxing music or white noise to help your mind calm down before sleeping.",
        "Use your bed only for sleep so your brain connects it with rest and relaxation.",
        "Wake up at the same time every day to build a strong and healthy sleep schedule.",
        "Get sunlight in the morning because it helps reset your body clock naturally.",
        "Exercise during the day since physical activity can improve your sleep quality at night.",
        "Avoid heavy meals before bed so your body can relax instead of focusing on digestion."
    ],

    "productivity": [
        "Make a simple to-do list every morning so you know exactly what you need to focus on during the day.",
        "Start with the hardest task first so the rest of your day feels easier and less stressful.",
        "Remove distractions like your phone when working so you can stay fully focused.",
        "Break big tasks into smaller steps to make them feel easier and less overwhelming.",
        "Set deadlines for your tasks so you stay motivated and avoid procrastination.",
        "Focus on one task at a time instead of multitasking, which actually reduces efficiency.",
        "Use timers to stay on track and manage your time more effectively.",
        "Keep your workspace clean and organized to improve focus and productivity.",
        "Reward yourself after finishing tasks to stay motivated and consistent.",
        "Plan your day the night before so you can start your morning with a clear goal."
    ],

    "health": [
        "Drink more water throughout the day because staying hydrated improves your energy and focus.",
        "Try to walk at least 30 minutes daily to keep your body active and healthy.",
        "Eat more fruits and vegetables since they provide important nutrients your body needs.",
        "Stretch every morning to improve flexibility and reduce muscle stiffness.",
        "Don’t skip breakfast because it gives you energy to start your day properly.",
        "Exercise regularly to improve both your physical and mental health.",
        "Take deep breaths when you feel stressed, as it helps calm your mind quickly.",
        "Limit sugary drinks because too much sugar can affect your energy levels.",
        "Wash your hands often to stay clean and avoid getting sick.",
        "Stand up and move every hour, especially if you sit for long periods."
    ],

    "cleaning": [
        "Clean as you go instead of leaving everything for later, so mess doesn’t build up.",
        "Set a timer for 10 minutes and clean quickly, which makes it feel easier and faster.",
        "Do small cleaning tasks daily so your space always stays manageable.",
        "Keep your cleaning supplies in one place so you don’t waste time looking for them.",
        "Make your bed every morning to instantly make your room look cleaner.",
        "Use baking soda for tough stains since it’s simple and effective.",
        "Declutter one area at a time so you don’t feel overwhelmed.",
        "Do laundry regularly to avoid piles of clothes building up.",
        "Wipe surfaces daily to keep your space fresh and clean.",
        "Organize before cleaning so everything has its proper place."
    ],

    "money": [
        "Save a small amount of money every week, because even small savings add up over time.",
        "Track your spending so you understand where your money is going.",
        "Avoid impulse buying by thinking carefully before making a purchase.",
        "Set a budget to control your spending and reach your financial goals.",
        "Compare prices before buying anything to make sure you get the best deal.",
        "Use discounts and coupons whenever possible to save money.",
        "Cook at home more often instead of eating out, which saves a lot of money.",
        "Set clear financial goals so you stay motivated to save.",
        "Avoid unnecessary subscriptions that slowly drain your money.",
        "Buy only what you truly need instead of wasting money on extras."
    ],

    "social": [
        "Listen more than you talk because people appreciate feeling heard and understood.",
        "Make eye contact when speaking to show confidence and respect.",
        "Smile when talking to others since it makes you seem more friendly and approachable.",
        "Remember people’s names because it makes interactions more personal.",
        "Be kind and respectful in conversations to build better relationships.",
        "Ask questions to show genuine interest in what others are saying.",
        "Stay positive during conversations to create a good atmosphere.",
        "Avoid interrupting others so they feel respected.",
        "Be confident but still polite in how you speak.",
        "Practice good manners in all situations."
    ],

    "technology": [
        "Use keyboard shortcuts to save time and work more efficiently.",
        "Organize your files into folders so everything is easy to find.",
        "Back up important data regularly to avoid losing it.",
        "Keep your software updated for better performance and security.",
        "Use strong passwords to protect your accounts.",
        "Limit screen time to avoid distractions and eye strain.",
        "Turn off unnecessary notifications so you can focus better.",
        "Use dark mode at night to reduce eye strain.",
        "Clean your device storage regularly to keep it running smoothly.",
        "Learn basic tech skills to improve your productivity."
    ],

    "motivation": [
        "Start small and just begin, because taking the first step is always the hardest part.",
        "Set clear goals so you know exactly what you’re working towards.",
        "Track your progress to stay motivated and see how far you’ve come.",
        "Celebrate small wins because they help build confidence and momentum.",
        "Stay consistent even if progress feels slow at first.",
        "Visualize your success to stay focused and motivated.",
        "Surround yourself with positive people who support your goals.",
        "Take breaks when needed so you don’t burn out.",
        "Don’t compare yourself to others because everyone moves at their own pace.",
        "Keep going even when it feels difficult, because persistence pays off."
    ],

    "school": [
        "Pay attention in class so you understand the material the first time.",
        "Ask questions whenever you feel confused to avoid falling behind.",
        "Review your notes daily to keep information fresh in your mind.",
        "Stay organized so you can easily find your work and materials.",
        "Do your homework on time to avoid stress later.",
        "Participate in discussions to improve understanding.",
        "Use a planner to keep track of assignments and deadlines.",
        "Study a little every day instead of cramming last minute.",
        "Avoid procrastination by starting tasks early.",
        "Prepare for tests in advance so you feel confident."
    ]
}
