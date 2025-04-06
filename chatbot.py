import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

st.title("🤖 シンプルなAIチャットボット")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 過去のメッセージを表示
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザー入力を取得
if user_input := st.chat_input("メッセージを入力してください"):
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # OpenAI API（最新版）を呼び出し
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state["messages"]
        )
        assistant_response = response.choices[0].message.content
        message_placeholder.markdown(assistant_response)

    # AIの応答を記録
    st.session_state["messages"].append({"role": "assistant", "content": assistant_response})
