import streamlit as st
import requests

st.set_page_config(page_title="AI Tutor MCP", page_icon="📚")
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
                f"http://localhost:8000/mcp/ai_tutor",
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
