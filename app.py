import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="數據工作室 | Data Studio", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 粒子動畫背景
particles_html = """<!DOCTYPE html>
<html>
<head>
<style>
    * { margin: 0; padding: 0; }
    body { background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%); }
    #particles-js { position: fixed; width: 100%; height: 100%; top: 0; left: 0; z-index: 1; }
</style>
</head>
<body>
    <div id="particles-js"></div>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS("particles-js", {
            "particles": {
                "number": {"value": 280, "density": {"enable": true, "value_area": 800}},
                "color": {"value": "#ffffff"},
                "shape": {"type": "circle"},
                "opacity": {"value": 0.6, "random": false},
                "size": {"value": 2.5, "random": true},
                "line_linked": {"enable": true, "distance": 130, "color": "#83c9ff", "opacity": 0.28, "width": 1.5},
                "move": {"enable": true, "speed": 0.25, "direction": "none", "random": false, "straight": false, "out_mode": "out", "bounce": true}
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {"enable": true, "mode": "grab"},
                    "onclick": {"enable": true, "mode": "repulse"}
                },
                "modes": {
                    "grab": {"distance": 140, "line_linked": {"opacity": 1}},
                    "repulse": {"distance": 220, "duration": 0.5}
                }
            },
            "retina_detect": true
        });
    </script>
</body>
</html>
"""

components.html(particles_html, height=1000, scrolling=False)

# CSS 樣式
st.markdown("""
<style>
    .stApp { background: transparent !important; }
    .main { background: transparent !important; }
    .block-container { background: transparent !important; z-index: 100 !important; }
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stToolbar"] { background: transparent !important; }
    [data-testid="stSidebarContent"] { display: none !important; }
    
    h1, h2, h3, p, span, label, div { color: #ffffff !important; }
    
    .gradient-title {
        font-size: 70px;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(to right, #FFABAB, #83C9FF, #0068C9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 80px 0 50px 0;
        letter-spacing: 2px;
        filter: drop-shadow(0 0 30px rgba(131, 201, 255, 0.6));
    }
    
    .case-container {
        display: flex;
        justify-content: center;
        margin: 80px 0;
    }
    
    .case-card {
        position: relative;
        width: 280px;
        height: 280px;
        border-radius: 25px;
        overflow: hidden;
        box-shadow: 0 0 60px rgba(131, 201, 255, 0.4);
        cursor: pointer;
        transition: all 0.4s ease;
    }
    
    .case-card:hover {
        transform: scale(1.1) translateY(-15px);
        box-shadow: 0 0 80px rgba(131, 201, 255, 0.8);
    }
    
    .case-card img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: filter 0.3s ease;
    }
    
    .overlay-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 28px;
        font-weight: bold;
        color: white;
        opacity: 0;
        transition: opacity 0.3s ease;
        text-shadow: 0 2px 15px rgba(0,0,0,0.9);
        z-index: 20;
    }
    
    .case-card:hover .overlay-text { opacity: 1; }
    .case-card:hover img { filter: brightness(0.3) blur(3px); }
    
    .contact-container {
        background: rgba(10, 14, 39, 0.4) !important;
        backdrop-filter: blur(30px);
        padding: 60px;
        border-radius: 30px;
        border: 2px solid rgba(131, 201, 255, 0.2);
        margin: 100px auto 60px auto;
        max-width: 1000px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    
    .contact-container h2 {
        color: white !important;
        margin-bottom: 40px;
        font-size: 28px;
    }
    
    input[type="text"], input[type="email"], textarea {
        padding: 15px 20px !important;
        border-radius: 12px !important;
        border: 1px solid rgba(131, 201, 255, 0.3) !important;
        background: rgba(255, 255, 255, 0.08) !important;
        color: white !important;
        font-size: 15px !important;
        transition: all 0.3s ease !important;
    }
    
    input[type="text"]:focus, input[type="email"]:focus, textarea:focus {
        background: rgba(255, 255, 255, 0.15) !important;
        border-color: rgba(131, 201, 255, 0.8) !important;
        box-shadow: 0 0 20px rgba(131, 201, 255, 0.4) !important;
        outline: none !important;
    }
    
    input::placeholder, textarea::placeholder { color: rgba(255, 255, 255, 0.5) !important; }
    
    .submit-btn {
        width: 100%;
        padding: 18px !important;
        margin-top: 30px;
        border-radius: 12px !important;
        border: none !important;
        background: linear-gradient(135deg, #0068C9, #0054a8) !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 6px 20px rgba(0, 104, 201, 0.6) !important;
    }
    
    .submit-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(0, 104, 201, 0.8) !important;
    }
</style>
""", unsafe_allow_html=True)

# 內容
st.markdown('<div class="gradient-title">數據工作室</div>', unsafe_allow_html=True)

case_url = "https://marketing-objectives-managementdashboard-mlxu3hfgu6pzpysxirvjm.streamlit.app/"
demo_img = "https://github.com/s942509/Aurora_back/blob/main/demo_img.png?raw=true"

case_html = f"""
<div class="case-container">
    <a href="{case_url}" target="_blank" style="text-decoration: none;">
        <div class="case-card">
            <img src="{demo_img}" alt="參考案例">
            <div class="overlay-text">參考案例</div>
        </div>
    </a>
</div>
"""
st.markdown(case_html, unsafe_allow_html=True)

st.markdown('<div class="contact-container">', unsafe_allow_html=True)
st.markdown("### 聯絡我們")

form_html = """
<form action="https://formsubmit.co/s942509@gmail.com" method="POST">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
        <input type="text" name="統一編號" placeholder="*統一編號" required>
        <input type="text" name="公司名稱" placeholder="*公司名稱" required>
        <input type="text" name="部門" placeholder="*部門" required>
        <input type="text" name="職稱" placeholder="*職稱" required>
        <input type="text" name="名字" placeholder="*名字" required>
        <input type="text" name="姓氏" placeholder="*姓氏" required>
    </div>
    <input type="email" name="email" placeholder="*Email" required style="width: 100%; margin-bottom: 20px;">
    <textarea name="message" placeholder="備註 (選填)" rows="5" style="width: 100%; margin-bottom: 20px;"></textarea>
    <button type="submit" class="submit-btn">提交</button>
</form>
"""

st.markdown(form_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
