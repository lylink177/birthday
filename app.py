import streamlit as st

# 1. 设置网页的基本信息
st.set_page_config(page_title="噶人们你们知道吗", page_icon="🎂", layout="centered")

# 2. 天降气球和雪花特效
st.balloons()
st.snow()

# 3. 标题和开场白
st.title("🎂 致最好的‘10.24’")
st.markdown("### —— 一份赛博感谢")
st.write("---")

# 4. 展示蛋糕照片
try:
    st.image("cake.jpg", caption="今晚的烛光与惊喜", use_container_width=True)
except Exception as e:
    st.warning("⚠️ 哎呀，蛋糕照片没找到！")

st.write("---")

# 5. 走心的文字
st.markdown("""
（此处省略800字）

**谢谢你们的蛋糕，谢谢你们的惊喜！**
""")

st.write("---")

# ================= 新增：赛博跑马灯模块 =================
st.markdown("#### 🎊 难道说？：")

# 你可以在这里随便加减内容，用 | 隔开就行
marquee_text1 = "这不是外挂？ |   行不行啊！老弟！ |   啦啦啦啦啦啦啦啦~ |   mj "
marquee_text2 = "🚀 通透~！ |   💰 这期神了 |   🍗 听雨的声音 一滴滴清晰 wu~ |    ❤️我说搞懂x+y=x+y+z，有没有懂的 ！"

# 第一行跑马灯（红色，速度适中）
st.markdown(
    f"<marquee style='color:red; font-size:18px; font-weight:bold; margin-bottom: 10px;'>{marquee_text1}</marquee>",
    unsafe_allow_html=True)

# 第二行跑马灯（蓝色，反向滚动，速度稍微快点）
st.markdown(
    f"<marquee style='color:blue; font-size:18px; font-weight:bold;' direction='right' scrollamount='5'>{marquee_text2}</marquee>",
    unsafe_allow_html=True)



