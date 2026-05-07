import streamlit as st

# 1. 頁面設定
st.set_page_config(page_title="Aurora Background", layout="wide")

# 2. 注入極光 CSS
st.markdown(
    """
    <style>
    /* 強制將 Streamlit 所有的容器設為透明 */
    .stApp, .stMain, .main, .block-container {
        background: transparent !important;
    }

    /* 真正的底色層 */
    body {
        background-color: #020617 !important; /* 極深藍黑底 */
        margin: 0;
        padding: 0;
    }

    /* 極光容器 */
    .aurora-wrapper {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -1; /* 放在最底層 */
        overflow: hidden;
        background: #020617;
    }

    /* 極光光暈 */
    .aurora-element {
        position: absolute;
        width: 150%;
        height: 150%;
        top: -25%;
        left: -25%;
        background-image: 
            radial-gradient(circle at 10% 10%, rgba(0, 150, 136, 0.5) 0%, transparent 40%),
            radial-gradient(circle at 90% 10%, rgba(0, 188, 212, 0.4) 0%, transparent 40%),
            radial-gradient(circle at 50% 90%, rgba(103, 58, 183, 0.4) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(0, 105, 92, 0.3) 0%, transparent 40%);
        filter: blur(100px); /* 深度模糊營造柔和感 */
        opacity: 0.8;
        animation: aurora-animate 25s infinite alternate linear;
    }

    /* 雜訊質感 (Noise) - 讓效果更像影片中的細緻質感 */
    .aurora-wrapper::after {
        content: "";
        position: absolute;
        inset: 0;
        background-image: url("https://grainy-gradients.vercel.app/noise.svg");
        opacity: 0.2;
        mix-blend-mode: overlay;
        pointer-events: none;
    }

    @keyframes aurora-animate {
        0% { transform: rotate(0deg) translate(0, 0) scale(1); }
        33% { transform: rotate(2deg) translate(2%, 4%) scale(1.1); }
        66% { transform: rotate(-2deg) translate(-2%, 2%) scale(0.9); }
        100% { transform: rotate(0deg) translate(0, 0) scale(1); }
    }
    
    /* 隱藏 Streamlit 的裝飾線 */
    header, footer { visibility: hidden !important; }
    </style>

    <div class="aurora-wrapper">
        <div class="aurora-element"></div>
    </div>
    """,
    unsafe_allow_html=True
)

# 測試用：放一個完全透明的內容
st.write("")
