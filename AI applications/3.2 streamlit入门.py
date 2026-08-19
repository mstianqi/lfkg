import streamlit as st

# 设置页面布局
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.baidu.com',
        'Report a bug': "https://www.baidu.com",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("大标题")
st.header("一级标题")
st.subheader("二级标题")

st.write("文字测试1")
st.write("文字测试2")
st.logo("resources/五角星.jpeg")
st.image("resources/incomplete.jpg")
st.audio("resources/dongfengpo.mp3")
st.video("resources/夜的钢琴曲五.mp4")

# 表格
student_data = {
    "姓名": ["小明", "小红"],
    "语文": ["80", "70"],
    "数学": ["70", "80"]
}
st.table(student_data)

# 输入框
name = st.text_input("请输入姓名：")
st.write(f"姓名：{name}")

# 单选框
gender = st.radio("请选择性别：", ["男", "女"])