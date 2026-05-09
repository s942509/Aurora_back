import streamlit as st
import streamlit.components.v1 as components

# --- 步驟 1：基礎設定 ---
st.set_page_config(page_title="數據工作室 | Data Studio", layout="wide")

# --- 步驟 2：Globe.gl 宇宙背景腳本 ---
# 我們使用 Globe.gl 的背景繪製能力，但「不渲染地球」，只渲染星空並讓它旋轉
starfield_js = """
<div id="globeViz"></div>
<script src="//unpkg.com/globe.gl"></script>
<script>
    const world = Globe()
      (document.getElementById('globeViz'))
      .backgroundColor('rgba(0,0,0,0)') // 背景透明
      .showGlobe(false) // 隱藏地球
      .showAtmosphere(false) // 隱藏大氣層
      .backgroundImageUrl('//unpkg.com/three-globe/example/img/night-sky.png');

    // 開啟自動旋轉，產生星空流動感
    world.controls().autoRotate = true;
    world.controls().autoRotateSpeed = 0.3; 
</script>
<style> 
    body { margin: 0; background: #000; overflow: hidden; } 
    #globeViz { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; }
</style>
"""

# 注入背景
components.html(starfield_js, height=0)

# --- 步驟 3：CSS 樣式設計 (確保透明與文字樣式) ---
st.markdown("""
<style>
    /* 強制透明層級 */
    .stApp, .main, .block-container, [data-testid="stHeader"] {
        background: transparent !important;
    }

    h1, h2, h3, p, span, label, div {
        color: white !important;
    }

    /* 漸層大標題 */
    .gradient-title {
        font-size: 70px;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(to right, #FFABAB, #83C9FF, #0068C9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 50px 0;
    }

    /* 縮圖卡片設定 */
    .case-container {
        display: flex;
        justify-content: center;
        margin-bottom: 50px;
    }
    .case-card {
        position: relative;
        width:10%; /* 這裡調整縮圖大小 */
        border-radius: 15px;
        overflow: hidden;
        transition: 0.4s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        cursor: pointer;
    }
    .case-card:hover {
        transform: scale(1.05);
        box-shadow: 0 0 30px 10px rgba(131, 201, 255, 0.6);
    }
    .case-card img {
        width: 100%;
        display: block;
        transition: 0.3s;
    }
    .overlay-text {
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        font-size: 22px; /* 這裡調整「參考案例」字體大小 */
        font-weight: bold;
        opacity: 0;
        transition: 0.3s;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.9);
    }
    .case-card:hover .overlay-text {
        opacity: 1;
    }
    .case-card:hover img {
        filter: brightness(0.3) blur(2px);
    }

    /* 聯絡區塊 */
    .contact-container {
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(15px);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 50px auto;
        max-width: 800px;
    }
</style>
""", unsafe_allow_html=True)

# --- 步驟 4：內容渲染 ---

st.markdown('<div class="gradient-title">數據工作室</div>', unsafe_allow_html=True)

# 案例圖片與連結
case_url = "https://marketing-objectives-managementdashboard-mlxu3hfgu6pzpysxirvjm.streamlit.app/"
demo_img = "https://github.com/s942509/Aurora_back/blob/main/demo_img.png?raw=true"

case_html = f"""
<div class="case-container">
    <a href="{case_url}" target="_blank">
        <div class="case-card">
            <img src="{demo_img}">
            <div class="overlay-text">參考案例</div>
        </div>
    </a>
</div>
"""
st.markdown(case_html, unsafe_allow_html=True)

# 聯絡表單
st.markdown('<div class="contact-container">', unsafe_allow_html=True)
st.subheader("聯絡我們")
form_html = """
<form action="https://formsubmit.co/s942509@gmail.com" method="POST">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
        <input type="text" name="統一編號" placeholder="*統一編號" required style="padding:12px; border-radius:5px; border:none; background:rgba(255,255,255,0.15); color:white;">
        <input type="text" name="公司名稱" placeholder="*公司名稱" required style="padding:12px; border-radius:5px; border:none; background:rgba(255,255,255,0.15); color:white;">
        <input type="text" name="部門" placeholder="*部門" required style="padding:12px; border-radius:5px; border:none; background:rgba(255,255,255,0.15); color:white;">
        <input type="text" name="職稱" placeholder="*職稱" required style="padding:12px; border-radius:5px; border:none; background:rgba(255,255,255,0.15); color:white;">
        <input type="text" name="名字" placeholder="*名字" required style="padding:12px; border-radius:5px; border:none; background:rgba(255,255,255,0.15); color:white;">
        <input type="text" name="姓氏" placeholder="*姓氏" required style="padding:12px; border-radius:5px; border:none; background:rgba(255,255,255,0.15); color:white;">
    </div>
    <button type="submit" style="width:100%; margin-top:20px; padding:15px; border-radius:5px; border:none; background:#0068C9; color:white; font-size:18px; font-weight:bold; cursor:pointer;">Submit</button>
</form>
"""
st.markdown(form_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
