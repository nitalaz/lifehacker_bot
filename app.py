import streamlit as st

st.set_page_config(page_title="My Chatbot", page_icon="🤖")

st.title("🤖 My Streamlit Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Type your message here...")

if prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Simple bot response (for now)
    response = f"You said: {prompt}"

    # Save bot message
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
