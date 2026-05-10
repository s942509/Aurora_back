import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="數據工作室 | Data Studio", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 隱藏所有 Streamlit UI 元素和邊框
st.markdown("""
<style>
    /* 基本重置 */
    * { box-sizing: border-box; }
    html, body { 
        margin: 0 !important; 
        padding: 0 !important; 
        width: 100% !important;
        height: 100% !important;
        background: transparent !important;
    }
    
    /* 隱藏 Streamlit 的所有 UI 元素 */
    [data-testid="stHeaderActionItems"] { display: none !important; }
    [data-testid="stHeader"] { display: none !important; }
    [data-testid="stToolbar"] { display: none !important; }
    [data-testid="stSidebarContent"] { display: none !important; }
    
    /* 隱藏所有 Streamlit 容器 */
    .main { 
        background: transparent !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .stApp { 
        background: transparent !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .block-container { 
        background: transparent !important;
        max-width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
    }
    
    /* 隱藏所有邊框和邊距 */
    [data-testid="stDecoratedObject"] {
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* iframe 容器 */
    iframe { 
        border: none !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 100% !important;
    }
    
    /* 隱藏所有滾動條 - 除了瀏覽器自己的 */
    .main::-webkit-scrollbar { width: 0 !important; }
    .block-container::-webkit-scrollbar { width: 0 !important; }
    .stApp::-webkit-scrollbar { width: 0 !important; }
    
    /* 隱藏 markdown 背景 */
    [data-testid="stMarkdownContainer"] { 
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Streamlit 的內部滾動條 */
    div[data-testid="stMainBlockContainer"] {
        overflow: hidden !important;
    }
</style>
""", unsafe_allow_html=True)

html_content = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>數據工作室</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        html, body {
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            overflow-x: hidden;
        }
        
        #particles-js {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: 0;
        }
        
        .content {
            position: relative;
            z-index: 10;
            width: 100%;
            min-height: 100vh;
        }
        
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
        }
        
        .case-card:hover .overlay-text { opacity: 1; }
        .case-card:hover img { filter: brightness(0.3) blur(3px); }
        
        .contact-container {
            background: rgba(10, 14, 39, 0.4);
            backdrop-filter: blur(30px);
            padding: 60px;
            border-radius: 30px;
            border: 2px solid rgba(131, 201, 255, 0.2);
            margin: 100px auto 60px auto;
            max-width: 1000px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }
        
        .contact-container h2 {
            color: white;
            margin-bottom: 40px;
            font-size: 28px;
        }
        
        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 20px;
        }
        
        input[type="text"], 
        input[type="email"], 
        textarea {
            padding: 15px 20px;
            border-radius: 12px;
            border: 1px solid rgba(131, 201, 255, 0.3);
            background: rgba(255, 255, 255, 0.08);
            color: white;
            font-size: 15px;
            transition: all 0.3s ease;
            font-family: inherit;
        }
        
        input[type="text"]:focus, 
        input[type="email"]:focus, 
        textarea:focus {
            background: rgba(255, 255, 255, 0.15);
            border-color: rgba(131, 201, 255, 0.8);
            box-shadow: 0 0 20px rgba(131, 201, 255, 0.4);
            outline: none;
        }
        
        input::placeholder, 
        textarea::placeholder { 
            color: rgba(255, 255, 255, 0.5); 
        }
        
        .submit-btn {
            width: 100%;
            padding: 18px;
            margin-top: 30px;
            border-radius: 12px;
            border: none;
            background: linear-gradient(135deg, #0068C9, #0054a8);
            color: white;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 6px 20px rgba(0, 104, 201, 0.6);
        }
        
        .submit-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(0, 104, 201, 0.8);
        }
        
        @media (max-width: 768px) {
            .gradient-title { font-size: 48px; }
            .form-grid { grid-template-columns: 1fr; }
            .contact-container { padding: 30px; }
        }
    </style>
</head>
<body>
    <div id="particles-js"></div>
    
    <div class="content">
        <div class="gradient-title">數據工作室</div>
        
        <div class="case-container">
            <a href="https://marketing-objectives-managementdashboard-mlxu3hfgu6pzpysxirvjm.streamlit.app/" target="_blank" style="text-decoration: none;">
                <div class="case-card">
                    <img src="https://github.com/s942509/Aurora_back/blob/main/demo_img.png?raw=true" alt="參考案例">
                    <div class="overlay-text">參考案例</div>
                </div>
            </a>
        </div>
        
        <div class="contact-container">
            <h2>聯絡我們</h2>
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
                <textarea name="message" placeholder="備註 (選填)" rows="5" style="width: 100%; margin-bottom: 20px;"></textarea>
                <button type="submit" class="submit-btn">提交</button>
            </form>
        </div>
        <br><br>
    </div>
    
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS("particles-js", {
            "particles": {
                "number": {
                    "value": 280,
                    "density": {
                        "enable": true,
                        "value_area": 800
                    }
                },
                "color": {
                    "value": "#ffffff"
                },
                "shape": {
                    "type": "circle"
                },
                "opacity": {
                    "value": 0.6,
                    "random": false,
                    "anim": {
                        "enable": false,
                        "speed": 1,
                        "opacity_min": 0.1,
                        "sync": false
                    }
                },
                "size": {
                    "value": 2.5,
                    "random": true,
                    "anim": {
                        "enable": false,
                        "speed": 40,
                        "size_min": 0.1,
                        "sync": false
                    }
                },
                "line_linked": {
                    "enable": true,
                    "distance": 130,
                    "color": "#83c9ff",
                    "opacity": 0.28,
                    "width": 1.5
                },
                "move": {
                    "enable": true,
                    "speed": 0.25,
                    "direction": "none",
                    "random": false,
                    "straight": false,
                    "out_mode": "out",
                    "bounce": true,
                    "attract": {
                        "enable": false,
                        "rotateX": 600,
                        "rotateY": 1200
                    }
                }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {
                        "enable": true,
                        "mode": "grab"
                    },
                    "onclick": {
                        "enable": true,
                        "mode": "repulse"
                    },
                    "resize": true
                },
                "modes": {
                    "grab": {
                        "distance": 140,
                        "line_linked": {
                            "opacity": 1
                        }
                    },
                    "bubble": {
                        "distance": 400,
                        "size": 40,
                        "duration": 2,
                        "opacity": 8,
                        "speed": 3
                    },
                    "repulse": {
                        "distance": 220,
                        "duration": 0.5
                    },
                    "push": {
                        "particles_nb": 4
                    },
                    "remove": {
                        "particles_nb": 2
                    }
                }
            },
            "retina_detect": true
        });
    </script>
</body>
</html>
"""

components.html(html_content, height=1200, scrolling=True)
