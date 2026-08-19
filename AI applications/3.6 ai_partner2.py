import os
import streamlit as st
from openai import OpenAI
from datetime import datetime
import json

st.set_page_config(
    page_title="AI聊天测试页面",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
)

# 生成新的会话
def generate_session():
    return datetime.now().strftime("%Y-%m-%d %H-%M-%S")

# 保存当前会话
def save_session():
    session_data = {
        "current_session": st.session_state.current_session,
        "messages": st.session_state.messages,
    }
    os.makedirs("3.6 sessions", exist_ok=True)
    with open(f"3.6 sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=4)

# 加载所有会话列表
def load_sessions():
    session_list = []
    if os.path.exists(f"3.6 sessions"):
        files = os.listdir("3.6 sessions")
        for file in files:
            if file.endswith(".json"):
                session_list.append(file[0:-5:1])
    session_list.sort(reverse=True)
    return session_list

# 加载指定会话
def load_session(session):
    try:
        if os.path.exists(f"3.6 sessions/{session}.json"):
            with open(f"3.6 sessions/{session}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.current_session = session_data["current_session"]
    except Exception as e:
        st.error(e)

# 删除会话
def delete_session(session):
    try:
        if os.path.exists(f"3.6 sessions/{session}.json"):
            os.remove(f"3.6 sessions/{session}.json")
            if session == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = generate_session()
    except Exception as e:
        st.error(e)


st.title("AI聊天")
system_prompt = "You are a helpful assistant."

# messages用来创建列表，保存历史消息，历史消息是字典类型。
if "messages" not in st.session_state:
    st.session_state.messages = []
if "account" not in st.session_state:
    st.session_state.account = "本地账户"
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session()

client = OpenAI(api_key="123", base_url="https://api.deepseek.com")
# 显示当前会话的历史消息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("请输入问题")
if prompt:
    st.chat_message("user").write(prompt)  # 显示本次发送的消息
    st.session_state.messages.append({"role": "user", "content": prompt})
    stream = client.responses.create(
        model="deepseek-v4-flash",
        instructions=system_prompt,
        input=st.session_state.messages,
        stream=True
    )
    full_response = ""
    # 创建接收聊天框，placeholder表示占位符，用来更新内容
    assistant_box = st.chat_message("assistant")
    placeholder = assistant_box.empty()

    for event in stream:
        if event.type == "response.output_text.delta":
            full_response += event.delta
            placeholder.markdown(full_response + "▌")
    placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    save_session()


# 设置侧边栏
with st.sidebar:
    st.subheader("历史记录")
    if st.button("新建会话", width="stretch"):
        # 保存旧会话
        if st.session_state.messages:
            save_session()
        # 创建新的空会话，但不保存文件
        st.session_state.messages = []
        st.session_state.current_session = generate_session()
        st.rerun()

    # 历史会话
    st.text("历史会话")
    session_list = load_sessions()
    for session in session_list:
        col1,col2 = st.columns([3.5,1.5])
        with col1:
            if st.button(session, width="stretch", type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            if st.button("删除", width="stretch", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()

    st.divider()
    st.write(f"账户：{st.session_state.account}")