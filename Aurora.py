import streamlit as st
import streamlit.components.v1 as components

# 設定頁面配置
st.set_page_config(page_title="Aurora Background Test", layout="wide")

# 定義 Aurora 背景的 CSS 與 HTML
# 這裡使用了 CSS 動畫來模擬影片中的 Aurora 效果，包含藍、綠、紫的漸層流動
aurora_css = """
<style>
    :root {
        --bg-color: #000000;
        --aurora-1: #00d4ff; /* 藍色 */
        --aurora-2: #00ff87; /* 綠色 */
        --aurora-3: #9d50bb; /* 紫色 */
    }

    .aurora-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-color: var(--bg-color);
        overflow: hidden;
        z-index: -1;
    }

    .aurora-blur {
        position: absolute;
        width: 200%;
        height: 200%;
        top: -50%;
        left: -50%;
        background-image: 
            radial-gradient(circle at 20% 30%, var(--aurora-1) 0%, transparent 40%),
            radial-gradient(circle at 80% 70%, var(--aurora-2) 0%, transparent 40%),
            radial-gradient(circle at 50% 50%, var(--aurora-3) 0%, transparent 50%);
        filter: blur(80px);
        opacity: 0.5;
        animation: aurora-move 20s infinite alternate ease-in-out;
    }

    @keyframes aurora-move {
        0% { transform: translate(0, 0) rotate(0deg); }
        50% { transform: translate(-5%, 10%) rotate(5deg); }
        100% { transform: translate(10%, -5%) rotate(-5deg); }
    }

    /* 移除 Streamlit 預設的 padding */
    .main .block-container {
        padding: 0;
    }
</style>

<div class="aurora-container">
    <div class="aurora-blur"></div>
</div>
"""

# 將 CSS/HTML 注入 Streamlit
st.markdown(aurora_css, unsafe_allow_html=True)

# 為了測試，我們加一個簡單的標題（雖然你說不需要文字，但這能幫助確認頁面已載入）
# 如果真的完全不要，可以註解掉下面這行
st.write("")
