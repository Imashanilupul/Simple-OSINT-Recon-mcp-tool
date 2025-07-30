import streamlit as st
import requests
from config import MCP_SERVER_HOST, MCP_SERVER_PORT, MODEL_ID, UI_TITLE

st.set_page_config(page_title=UI_TITLE, page_icon="📚")
st.title("📚 AI Tutor")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("Ask a question:", placeholder="e.g., What is backpropagation?", key="input")

# Show chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Process user message
if user_input:
    # Append user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Thinking..."):
        try:
            res = requests.post(
                f"http://{MCP_SERVER_HOST}:{MCP_SERVER_PORT}/mcp/{MODEL_ID}",
                json={"prompt": user_input}
            )
            if res.status_code == 200:
                answer = res.json().get("output", "⚠️ No response received.")
            else:
                answer = f"❌ Server error ({res.status_code})"
        except Exception as e:
            answer = f"❌ Connection error: {str(e)}"

    # Append and display assistant response
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
