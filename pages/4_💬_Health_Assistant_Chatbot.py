import streamlit as st
from openai import OpenAI

# -----------------------------
# 1️⃣ App Configuration
# -----------------------------
st.set_page_config(page_title = "💬 Health Assistant", page_icon = "💬")
# Page title
st.markdown(
    """
    <h2 style="text-align: center; color: #4a4a4a;">Health Assistant Chatbot 💬</h2>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# 2️⃣ Load API Key from Secrets
# -----------------------------
# The key must be stored in .streamlit/secrets.toml
if "OPENAI_API_KEY" not in st.secrets:
    st.error("❌ API key not found. Please add it to .streamlit/secrets.toml")
    st.stop()

# Initialize the OpenAI client with your secret key
client = OpenAI(api_key = st.secrets["OPENAI_API_KEY"])

# -----------------------------
# 3️⃣ System Prompt (Healthcare Professional Role)
# -----------------------------
SYSTEM_PROMPT = """
You are a knowledgeable and empathetic healthcare service professional assistant. Your role is to:

- Provide general health information and lifestyle recommendations
- Answer questions about heart health, cardiovascular risk factors, and preventive care
- Offer evidence-based wellness advice on diet, exercise, stress management, and healthy habits
- Be supportive, professional, and easy to understand
- Use clear, jargon-free language while remaining medically accurate

IMPORTANT DISCLAIMERS:
- Always remind users that you are NOT a replacement for professional medical advice, diagnosis, or treatment
- Encourage users to consult with their healthcare provider for personalized medical decisions
- Do not diagnose conditions or prescribe specific treatments
- In emergencies (chest pain, stroke symptoms, etc.), advise users to call emergency services immediately

Your tone should be warm, helpful, and informative while maintaining professional boundaries.
"""

# -----------------------------
# 4️⃣ Sidebar Configuration
# -----------------------------
with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown(
        """
        This health assistant provides general health information and lifestyle guidance.
        """
    )
    st.warning("⚠️ **Disclaimer:** This is NOT medical advice. Always consult your healthcare provider for personalized medical decisions.")

# Model selection and parameters
    model = st.selectbox(
        "Choose a GPT model:",
        ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"],
    )
    temperature = st.slider("Temperature (creativity)", 0.0, 1.0, 0.7, step = 0.05)
    max_tokens = st.slider("Max tokens (response length)", 64, 1500, 500, step = 32)

# -----------------------------
# 5️⃣ Chat History (Memory)
# -----------------------------
# At the start, when there's no chat history, initialize with a greeting
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Hello! I'm your health assistant. I can provide general health information and lifestyle recommendations. How can I help you today?\n\n*Please note: I'm not a replacement for professional medical advice. Always consult your healthcare provider for personalized medical decisions.*"
        }
    ]

# Display existing chat messages
# Keeps the conversation history visible, just like a messaging app
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Clear chat history
# On click, resets the chat messages to initial state
def clear_chat():
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Chat cleared! How can I assist you with your health questions today?\n\n*Remember: This is general information only, not medical advice.*"
        }
    ]
st.sidebar.button("🧹 Clear Chat History", on_click = clear_chat)

# -----------------------------
# 6️⃣ Generate GPT Response
# -----------------------------
# Function to get response from GPT
def generate_response(prompt):
    # Build messages with system prompt + conversation history + new user message
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ] + st.session_state.messages + [
        {"role": "user", "content": prompt}
    ]
    
    stream = client.chat.completions.create(
        model = model,             # Selected GPT model
        messages = messages,       # System prompt + full conversation history
        temperature = temperature, # Creativity of the response
        max_tokens = max_tokens,   # Maximum length of the response
        stream = True
        # NOTE: Enables streaming mode, where the model's output is 
        # sent to you in small chunks as it's generated (so you can display it in real-time) 
    )
    return stream

# -----------------------------
# 7️⃣ Chat Input and Response
# -----------------------------
# User input box
# Only if prompt is not empty, run the following:
if prompt := st.chat_input("Ask me about health, wellness, or heart health..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message on screen
    with st.chat_message("user"):
        st.markdown(prompt)

# If the last message is from user, generate assistant reply
if st.session_state.messages[-1]["role"] == "user":
    # Open chat bubble for assistant
    with st.chat_message("assistant"):
        # Show a "thinking" spinner while waiting for the response
        with st.spinner("Thinking..."):
            # Get the streaming response from GPT
            stream = generate_response(prompt)
            # 
            placeholder = st.empty()
            full_response = ""
            # Build the message token by token
            for chunk in stream:
                # Each chunk represents a part of the response
                if chunk.choices[0].delta.content:
                    # Append new content to the full response
                    full_response += chunk.choices[0].delta.content
                    # Update the placeholder with the current response
                    # The "▌" character acts as a cursor to indicate typing
                    placeholder.markdown(full_response + "▌")
            # Once complete, display the full response without cursor
            placeholder.markdown(full_response)

    # Save assistant message to memory
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )