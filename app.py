import streamlit as st
import time

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

import streamlit as st
import time

# 1. 初始化状态（记住他有没有点过按钮，避免一刷新就开骂）
if "hack_step" not in st.session_state:
    st.session_state.hack_step = 0

st.write("---")
st.markdown("#### 🎁 这里有一个专属彩蛋，请点击！")

# 2. 第一层诱导：原本的彩蛋按钮
if st.session_state.hack_step == 0:
    if st.button("点我揭秘"):
        st.session_state.hack_step = 1
        st.rerun()

# 3. 第二层陷阱：弹出一个“播放键”
elif st.session_state.hack_step == 1:
    st.info("⚠️ 发现未知加密文件，请点击播放键解密...")
    if st.button("▶️ 点击播放"):
        st.session_state.hack_step = 2
        st.rerun()

# 4. 终极触发：赛博社死现场
elif st.session_state.hack_step == 2:
    # 播放魔性音乐（注意：需要你在本地准备一个 music.mp3 放在同级目录）
    try:
        st.audio("mj.mp3", format="audio/mp3", autoplay=True)
    except Exception:
        st.warning("（音乐没加载出来，脑补一下极其魔性的BGM）")

    # 构建黑客风格的 HTML/CSS
    hack_html = """
    <style>
    .hack-warning {
        background-color: black;
        color: red;
        font-family: 'Courier New', monospace;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        border: 3px dashed red;
        animation: blink 0.5s step-end infinite alternate;
    }
    .scroll-text {
        font-family: 'Courier New', monospace;
        font-size: 30px;
        font-weight: bold;
        background: black;
        color: #00ff00; /* 经典黑客绿 */
    }
    @keyframes blink {
        50% { border-color: transparent; }
    }
    </style>
    """

    # 插入警告大字
    hack_html += "<div class='hack-warning'>🚨 检测到网站被热心网友入侵！完辣！ 🚨</div><br>"

    # 满屏疯狂滚动的“到此一游”（四面八方）
    hack_html += "<marquee class='scroll-text' direction='right' scrollamount='20'>雨忆轻尘 到此一游~！</marquee><br><br>"
    hack_html += "<marquee class='scroll-text' direction='left' scrollamount='15'>雨忆轻尘 到此一游~</marquee><br><br>"
    hack_html += "<marquee class='scroll-text' direction='up' scrollamount='25' style='height: 100px;'>雨忆轻尘 到此一游~</marquee>"
    hack_html += "<marquee class='scroll-text' direction='down' scrollamount='10' style='height: 100px;'>雨忆轻尘 到此一游~</marquee>"

    # 渲染特效
    st.markdown(hack_html, unsafe_allow_html=True)

    # 给他一个“重新做人”的按钮
    if st.button("🔄 重启系统（原谅他吧）"):
        st.session_state.hack_step = 0
        st.rerun()
