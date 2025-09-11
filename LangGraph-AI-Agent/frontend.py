#Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)

import streamlit as st
from agent import system_prompt
from langchain_community.callbacks.fiddler_callback import MODEL_NAME
from langchain_community.embeddings.bookend import API_URL
from openai import responses

st.set_page_config(page_title="LangGraph Agent UI", layout="wide")
st.title("🆓➡️ AI ChatBot Agents 🤖🌐")
st.write("Create and Interact with the AI Agents!😁🖥️")

system_prompt=st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system problem here...")

MODEL_NAME_GROQ= ["llama-3.3-70b-versatile", "deepseek-r1-distill-llama-70b", "qwen/qwen3-32b"]
MODEL_NAME_OPENAI= ["gpt-4o-mini"]

provider=st.radio("Select Provider 🤖 :", ("GROQ", "OPENAI"))

if provider == "GROQ":
    selected_model = st.selectbox("Select GROQ Model:", MODEL_NAME_GROQ)
elif provider == "OPENAI":
    selected_model = st.selectbox("Select OPENAI Model:", MODEL_NAME_OPENAI)

allow_web_search=st.checkbox("Allow Web Search 🌐")

user_query=st.text_area("Enter Your Query: ", height=150, placeholder="Ask me!...")

API_URL="http://127.0.0.1:9999/chat"

if st.button("Ask Agent!  🤖"):
    if user_query.strip():


        # Step2: Connect with backend via URL.
        import requests

        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response=requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response  😁")
                st.markdown(f"**Final Response:** {response}")
