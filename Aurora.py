import streamlit as st

# 頁面配置
st.set_page_config(page_title="Cloth Simulation Test", layout="wide")

# 強制背景變黑並移除邊距
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000 !important;
    }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 1. 定義極光布料容器 */
    .cloth-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        background: #000;
        overflow: hidden;
    }

    /* 2. 布料本體：利用漸層模擬披風顏色 */
    .cloth {
        position: relative;
        width: 120%;
        height: 120%;
        background: linear-gradient(
            217deg, rgba(0,212,255,.8), rgba(0,212,255,0) 70.71%
        ),
        linear-gradient(127deg, rgba(0,255,135,.8), rgba(0,255,135,0) 70.71%),
        linear-gradient(336deg, rgba(157,80,187,.8), rgba(157,80,187,0) 70.71%);
        
        /* 3. 關鍵：使用 SVG 濾鏡來產生布料皺褶感 */
        filter: url(#cloth-filter) blur(4px);
        animation: wind-move 8s infinite alternate ease-in-out;
        opacity: 0.7;
    }

    /* 4. 模擬風吹的動態：輕微的縮放與位移 */
    @keyframes wind-move {
        0% { transform: scale(1) translate(0, 0) rotate(0deg); }
        50% { transform: scale(1.05) translate(-2%, 3%) rotate(1deg); }
        100% { transform: scale(1) translate(2%, -2%) rotate(-1deg); }
    }
    </style>

    <!-- 5. 嵌入 SVG 濾鏡 (這是實現「飄動感」的核心，對應 Blender 的 Cloth 參數) -->
    <svg style="display:none">
        <filter id="cloth-filter">
            <!-- baseFrequency 的數值決定了皺褶的密度 (對應影片中的 Subdivide 20) -->
            <feTurbulence type="fractalNoise" baseFrequency="0.015 0.02" numOctaves="3" seed="2">
                <animate attributeName="baseFrequency" 
                         dur="10s" 
                         values="0.015 0.02; 0.02 0.015; 0.015 0.02" 
                         repeatCount="indefinite" />
            </feTurbulence>
            <feDisplacementMap in="SourceGraphic" scale="120" />
        </filter>
    </svg>

    <div class="cloth-container">
        <div class="cloth"></div>
    </div>
    """,
    unsafe_allow_html=True
)

st.empty()
