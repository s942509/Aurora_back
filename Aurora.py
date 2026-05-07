import streamlit as st
import streamlit.components.v1 as components

# 設定頁面為寬螢幕，並隱藏所有預設元素
st.set_page_config(page_title="Data Wave Matrix", layout="wide", initial_sidebar_state="collapsed")

def data_wave_matrix():
    html_code = """
    <style>
        /* 徹底隱藏 Streamlit 介面 */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp {background: transparent;}
        
        body {
            margin: 0;
            padding: 0;
            background-color: #05070a; /* 深邃底色 */
            overflow: hidden;
        }

        #wave-canvas {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            z-index: -1;
        }
    </style>

    <canvas id="wave-canvas"></canvas>

    <script>
        const canvas = document.getElementById('wave-canvas');
        const ctx = canvas.getContext('2d');
        let w = canvas.width = window.innerWidth;
        let h = canvas.height = window.innerHeight;

        const chars = "01$#&@%*<>?/!{}[]";
        const spacing = 25; // 點陣間距
        const cols = Math.floor(w / spacing) + 1;
        const rows = Math.floor(h / spacing) + 1;
        
        let time = 0;

        function draw() {
            // 清除背景
            ctx.fillStyle = "#05070a";
            ctx.fillRect(0, 0, w, h);

            time += 0.05;

            for (let i = 0; i < cols; i++) {
                for (let j = 0; j < rows; j++) {
                    const x = i * spacing;
                    const y = j * spacing;

                    // 波浪演算法：結合 X 與 Y 座標產生斜向波浪
                    // dist 決定波浪的傳遞感
                    const dist = (i + j) * 0.2;
                    const wave = Math.sin(dist - time);
                    
                    // 根據波浪強度決定亮度與大小
                    // wave 的範圍是 -1 ~ 1，我們將其映射到 0 ~ 1
                    const intensity = (wave + 1) / 2;
                    
                    const char = chars[Math.floor(Math.random() * chars.length)];
                    
                    // 設定字體大小隨波浪縮放
                    const size = 10 + (intensity * 8);
                    ctx.font = size + "px monospace";
                    
                    // 設定顏色：從深藍到亮白色的漸變感
                    // 基礎顏色為科技藍 #00d4ff
                    const r = Math.floor(0 + (255 * intensity * 0.8));
                    const g = Math.floor(212 * intensity);
                    const b = Math.floor(255);
                    
                    ctx.fillStyle = `rgba(${r}, ${g}, ${b}, ${0.1 + intensity * 0.9})`;
                    ctx.textAlign = "center";
                    ctx.textBaseline = "middle";
                    
                    // 繪製字元
                    ctx.fillText(char, x, y);
                }
            }
            requestAnimationFrame(draw);
        }

        draw();

        window.addEventListener('resize', () => {
            w = canvas.width = window.innerWidth;
            h = canvas.height = window.innerHeight;
        });
    </script>
    """
    # 這裡將 height 設為全螢幕高度，確保畫布完整呈現
    components.html(html_code, height=2000)

data_wave_matrix()
