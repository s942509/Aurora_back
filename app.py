import streamlit as st

# --- 步驟 1：基礎設定 ---
st.set_page_config(
    page_title="數據工作室 | Data Studio", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 步驟 2：全局 CSS - 星空背景 ---
st.markdown("""
<style>
    /* 重置所有邊距 */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* HTML 和 Body 背景 */
    html, body {
        background: #0a0e27 !important;
    }
    
    /* Streamlit 主容器背景 - 星空圖片 */
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?w=1920&h=1080&fit=crop') !important;
        background-attachment: fixed !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
    }
    
    .main {
        background: transparent !important;
    }
    
    .block-container {
        background: transparent !important;
    }
    
    [data-testid="stHeader"] {
        background: transparent !important;
    }
    
    [data-testid="stToolbar"] {
        background: transparent !important;
    }
    
    /* 隱藏側邊欄 */
    [data-testid="stSidebarContent"] {
        display: none !important;
    }
    
    /* 背景深色覆蓋層 - 提高文字可讀性 */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.4);
        pointer-events: none;
        z-index: 0;
    }
    
    /* 所有文字顏色 */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #ffffff !important;
    }
    
    /* 漸層大標題 */
    .gradient-title {
        font-size: 70px;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(to right, #FFABAB, #83C9FF, #0068C9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 50px 0;
        letter-spacing: 2px;
        position: relative;
        z-index: 1;
        text-shadow: 0 0 20px rgba(131, 201, 255, 0.3);
    }
    
    /* 案例卡片容器 */
    .case-container {
        display: flex;
        justify-content: center;
        margin: 50px 0;
        position: relative;
        z-index: 1;
    }
    
    .case-card {
        position: relative;
        width: 250px;
        height: 250px;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    .case-card:hover {
        transform: scale(1.08) translateY(-10px);
        box-shadow: 0 15px 40px rgba(131, 201, 255, 0.4);
    }
    
    .case-card img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        transition: filter 0.3s ease;
    }
    
    .overlay-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 24px;
        font-weight: bold;
        color: white;
        opacity: 0;
        transition: opacity 0.3s ease;
        text-shadow: 0 2px 10px rgba(0,0,0,0.8);
        z-index: 10;
    }
    
    .case-card:hover .overlay-text {
        opacity: 1;
    }
    
    .case-card:hover img {
        filter: brightness(0.4) blur(3px);
    }
    
    /* 聯絡表單區塊 */
    .contact-container {
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(20px);
        padding: 50px;
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin: 60px auto;
        max-width: 900px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        position: relative;
        z-index: 1;
    }
    
    .contact-container h2 {
        color: white !important;
        margin-bottom: 30px;
    }
    
    /* 表單輸入框 */
    .form-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        margin-bottom: 20px;
    }
    
    input[type="text"],
    input[type="email"],
    textarea {
        padding: 14px 18px !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        background: rgba(255, 255, 255, 0.12) !important;
        color: white !important;
        font-size: 14px !important;
        transition: all 0.3s ease;
    }
    
    input[type="text"]:focus,
    input[type="email"]:focus,
    textarea:focus {
        background: rgba(255, 255, 255, 0.18) !important;
        border-color: rgba(131, 201, 255, 0.5) !important;
        box-shadow: 0 0 15px rgba(131, 201, 255, 0.2) !important;
        outline: none;
    }
    
    input::placeholder,
    textarea::placeholder {
        color: rgba(255, 255, 255, 0.6) !important;
    }
    
    /* 提交按鈕 */
    .submit-btn {
        width: 100%;
        padding: 16px !important;
        margin-top: 20px;
        border-radius: 10px !important;
        border: none !important;
        background: linear-gradient(135deg, #0068C9, #0054a8) !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        cursor: pointer !important;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 104, 201, 0.3);
    }
    
    .submit-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(0, 104, 201, 0.5);
    }
    
    .submit-btn:active {
        transform: translateY(0);
    }
</style>
""", unsafe_allow_html=True)

# --- 步驟 3：頁面內容 ---

# 標題
st.markdown('<div class="gradient-title">數據工作室</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 案例卡片
case_url = "https://marketing-objectives-managementdashboard-mlxu3hfgu6pzpysxirvjm.streamlit.app/"
demo_img = "https://github.com/s942509/Aurora_back/blob/main/demo_img.png?raw=true"

case_html = f"""
<div class="case-container">
    <a href="{case_url}" target="_blank" style="text-decoration: none;">
        <div class="case-card">
            <img src="{demo_img}" alt="參考案例" loading="lazy">
            <div class="overlay-text">參考案例</div>
        </div>
    </a>
</div>
"""
st.markdown(case_html, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 聯絡表單
st.markdown('<div class="contact-container">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])
with col1:
    st.write("")
with col2:
    st.markdown("### 聯絡我們")

# 表單 HTML
form_html = """
<form action="https://formsubmit.co/s942509@gmail.com" method="POST">
    <div class="form-grid">
        <input type="text" name="統一編號" placeholder="*統一編號" required>
        <input type="text" name="公司名稱" placeholder="*公司名稱" required>
        <input type="text" name="部門" placeholder="*部門" required>
        <input type="text" name="職稱" placeholder="*職稱" required>
        <input type="text" name="名字" placeholder="*名字" required>
        <input type="text" name="姓氏" placeholder="*姓氏" required>
    </div>
    <input type="email" name="email" placeholder="*Email" required style="width: 100%; margin-bottom: 20px;">
    <textarea name="message" placeholder="備註 (選填)" rows="4" style="width: 100%; margin-bottom: 20px;"></textarea>
    <button type="submit" class="submit-btn">提交</button>
</form>
"""

st.markdown(form_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
