import streamlit as st
import streamlit.components.v1 as components

# 設定頁面為寬螢幕，並盡可能隱藏 Streamlit 預設元素
st.set_page_config(page_title="Background Only", layout="wide", initial_sidebar_state="collapsed")

def pure_matrix_aurora():
    # 注入 CSS 強制隱藏所有 Streamlit 文字、選單和邊距
    # 並實作 Canvas 繪製數位極光緞帶
    html_code = """
    <style>
        /* 隱藏所有 Streamlit 介面元素 */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp {background: transparent;}
        [data-testid="stHeader"] {background: rgba(0,0,0,0);}
        
        body {
            margin: 0;
            padding: 0;
            background-color: #050505; /* 宇宙底色 */
            overflow: hidden;
        }

        /* 1. 星空背景層 */
        #star-field {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle at center, #1B2735 0%, #050505 100%);
            z-index: -2;
        }

        .star {
            position: absolute;
            background: white;
            border-radius: 50%;
            opacity: 0.3;
            animation: twinkle var(--d) infinite;
        }
        @keyframes twinkle { 0%, 100% {opacity: 0.3;} 50% {opacity: 0.8;} }

        /* 2. 數位極光層 */
        #aurora-canvas {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            z-index: -1;
            /* 讓極光更有發光感 */
            filter: blur(0.5px) contrast(1.2) drop-shadow(0 0 15px #00ff41);
        }
    </style>

    <div id="star-field"></div>
    <canvas id="aurora-canvas"></canvas>

    <script>
        // 生成星星
        const stars = document.getElementById('star-field');
        for (let i = 0; i < 200; i++) {
            const s = document.createElement('div');
            s.className = 'star';
            const size = Math.random() * 2;
            s.style.width = size + 'px';
            s.style.height = size + 'px';
            s.style.top = Math.random() * 100 + '%';
            s.style.left = Math.random() * 100 + '%';
            s.style.setProperty('--d', (Math.random() * 4 + 2) + 's');
            stars.appendChild(s);
        }

        // 矩陣極光緞帶
        const canvas = document.getElementById('aurora-canvas');
        const ctx = canvas.getContext('2d');
        let w = canvas.width = window.innerWidth;
        let h = canvas.height = window.innerHeight;

        const chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ";
        const fontSize = 14;
        const columns = Math.floor(w / fontSize);
        const drops = new Array(columns).fill(0);
        let time = 0;

        function draw() {
            // 背景微透明覆蓋，保留字元軌跡
            ctx.fillStyle = "rgba(5, 5, 5, 0.15)";
            ctx.fillRect(0, 0, w, h);

            time += 0.015;

            for (let i = 0; i < drops.length; i++) {
                // 利用正弦波控制極光下緣，形成「緞帶」感
                // baseHeight 為緞帶基準高度，waveHeight 為起伏幅度
                const baseHeight = h * 0.1; 
                const waveHeight = h * 0.25;
                const limit = baseHeight + Math.sin(i * 0.08 + time) * waveHeight + Math.cos(i * 0.03 + time * 0.5) * 50;

                if (drops[i] * fontSize < limit) {
                    const text = chars[Math.floor(Math.random() * chars.length)];
                    
                    // 字首設為白色高亮，其餘為矩陣綠
                    ctx.fillStyle = (Math.random() > 0.9) ? "#fff" : "#00ff41";
                    ctx.font = fontSize + "px monospace";
                    ctx.fillText(text, i * fontSize, drops[i] * fontSize);

                    if (Math.random() > 0.97) drops[i] = 0;
                } else {
                    // 超過緞帶邊界就重置
                    drops[i] = 0;
                }
                drops[i]++;
            }
        }

        setInterval(draw, 35);
        window.addEventListener('resize', () => {
            w = canvas.width = window.innerWidth;
            h = canvas.height = window.innerHeight;
        });
    </script>
    """
    components.html(html_code, height=1000) # 給予足夠高度覆蓋全螢幕

pure_matrix_aurora()
