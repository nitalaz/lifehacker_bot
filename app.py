import streamlit as st

st.set_page_config(page_title="My Chatbot", page_icon="🤖")

st.title("🤖 My Streamlit Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to generate bot response (NO API)
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi there! 👋"
    elif "how are you" in user_input:
        return "I'm just code, but I'm doing great! 😄"
    elif "bye" in user_input:
        return "Goodbye! Have a great day! 👋"
    else:
        return "That's interesting! Tell me more."

# Display previous messages
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

    # Generate response (no API)
    response = get_bot_response(prompt)

    # Save assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)
