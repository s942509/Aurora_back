import streamlit as st

# 1. 基礎頁面設定
st.set_page_config(page_title="Aurora Test", layout="wide")

# 2. 強制覆蓋 Streamlit 預設樣式（確保背景完全填滿且為黑色）
st.markdown(
    """
    <style>
    /* 移除所有預設間距與背景色 */
    .stApp {
        background-color: #000000 !important;
    }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 極光容器 */
    .aurora-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 0;
        overflow: hidden;
        background: #000;
    }

    /* 極光本體 - 混合藍、綠、紫 */
    .aurora-layer {
        position: absolute;
        width: 150%;
        height: 150%;
        top: -25%;
        left: -25%;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(0, 212, 255, 0.4) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(0, 255, 135, 0.4) 0%, transparent 50%),
            radial-gradient(circle at 50% 80%, rgba(157, 80, 187, 0.4) 0%, transparent 50%);
        filter: blur(60px);
        animation: aurora-flow 15s infinite alternate ease-in-out;
    }

    @keyframes aurora-flow {
        0% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(5%, -5%) scale(1.1); }
        100% { transform: translate(-2%, 5%) scale(1); }
    }
    </style>
    
    <div class="aurora-bg">
        <div class="aurora-layer"></div>
    </div>
    """,
    unsafe_allow_html=True
)

# 3. 佔位符（讓頁面產生內容寬度，避免某些環境下被判定為空頁面）
st.empty()
