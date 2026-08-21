import streamlit as st
from openai import OpenAI

# # 非流式输出
# st.set_page_config(
#     page_title="AI聊天测试页面",
#     page_icon="🧊",
#     layout="centered",
#     initial_sidebar_state="expanded",  # 侧边栏默认展开
# )
#
# st.title("AI聊天")
# system_prompt = "You are a helpful assistant."
# # messages是session_state的自定义属性，创建为列表，用来保存历史消息，历史消息是字典类型
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# client = OpenAI(api_key="123", base_url="https://api.deepseek.com")
# # 显示当前会话的历史消息。st.chat_message()创建消息容器（对话气泡） .write()在容器中写内容
# for message in st.session_state.messages:
#     st.chat_message(message["role"]).write(message["content"])
#
# prompt = st.chat_input("请输入问题")
# if prompt:
#     st.chat_message("user").write(prompt)  # 显示本次发送的消息
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     response = client.responses.create(
#         model="deepseek-v4-flash",
#         instructions=system_prompt,
#         input=st.session_state.messages,
#         stream=False
#     )
#     st.chat_message("assistant").write(response.output_text)  # 显示本次接收的消息
#     st.session_state.messages.append({"role": "assistant", "content": response.output_text})

# 流式输出
st.set_page_config(
    page_title="AI聊天测试页面",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",  # 侧边栏默认展开
)

st.title("AI聊天")
system_prompt = "You are a helpful assistant."
# messages是session_state的自定义属性，创建为列表，用来保存历史消息，历史消息是字典类型
if "messages" not in st.session_state:
    st.session_state.messages = []
client = OpenAI(api_key="123", base_url="https://api.deepseek.com")
# 显示当前会话的历史消息。st.chat_message()创建消息容器（对话气泡） .write()在容器中写内容
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
    # 创建接收容器assistant_box，placeholder表示占位符，用来更新内容
    assistant_box = st.chat_message("assistant")
    placeholder = assistant_box.empty()

    for event in stream:
        if event.type == "response.output_text.delta":
            full_response += event.delta
            placeholder.markdown(full_response + "▌")
    placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})