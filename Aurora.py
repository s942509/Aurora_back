import streamlit as st
import streamlit.components.v1 as components

# 設定頁面資訊
st.set_page_config(page_title="GSS Matrix Aurora", layout="wide")

def matrix_aurora_bg():
    # 這裡結合了 CSS (背景星空) 與 JavaScript (Canvas 數位極光)
    matrix_code = """
    <style>
        /* 全局背景：浩瀚星空 */
        body {
            margin: 0;
            background-color: #050505;
            overflow: hidden;
        }
        
        #star-container {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
            z-index: -2;
        }

        /* 簡單的星星閃爍效果 */
        .star {
            position: absolute;
            background: white;
            border-radius: 50%;
            opacity: 0.5;
            animation: twinkle var(--duration) infinite;
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 1; }
        }

        #aurora-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            filter: drop-shadow(0 0 10px #00ff41);
        }

        /* 讓 Streamlit 的內容浮在背景上 */
        .stApp {
            background: transparent;
        }
        
        h1, p {
            color: #00ff41 !important;
            text-shadow: 0 0 10px rgba(0, 255, 65, 0.5);
        }
    </style>

    <div id="star-container"></div>
    <canvas id="aurora-canvas"></canvas>

    <script>
        // 1. 生成星星背景
        const starContainer = document.getElementById('star-container');
        for (let i = 0; i < 150; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            const size = Math.random() * 2 + 'px';
            star.style.width = size;
            star.style.height = size;
            star.style.top = Math.random() * 100 + '%';
            star.style.left = Math.random() * 100 + '%';
            star.style.setProperty('--duration', (Math.random() * 3 + 2) + 's');
            starContainer.appendChild(star);
        }

        // 2. Matrix 極光緞帶邏輯
        const canvas = document.getElementById('aurora-canvas');
        const ctx = canvas.getContext('2d');

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ";
        const fontSize = 16;
        const columns = canvas.width / fontSize;
        const drops = [];

        // 初始化每一列的下墜起始點
        for (let x = 0; x < columns; x++) {
            drops[x] = 1;
        }

        let time = 0;

        function draw() {
            // 這裡用半透明黑色覆蓋，產生字元拖尾效果
            ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            time += 0.02;

            for (let i = 0; i < drops.length; i++) {
                // 計算「極光緞帶」的波浪邊界 (利用 Sine Wave)
                // 只在頂部區域活動，h 控制緞帶下緣高度
                const wave = Math.sin(i * 0.05 + time) * 100 + 150;
                
                if (drops[i] * fontSize < wave) {
                    const text = characters.charAt(Math.floor(Math.random() * characters.length));
                    
                    // 越接近緞帶邊緣顏色越亮
                    ctx.fillStyle = "#00ff41";
                    ctx.font = fontSize + "px monospace";
                    ctx.fillText(text, i * fontSize, drops[i] * fontSize);

                    // 隨機重置，讓它有不規則的緞帶感
                    if (Math.random() > 0.95) {
                        drops[i] = 0;
                    }
                }
                
                drops[i]++;
                
                // 如果掉出波浪範圍太遠就重置到頂部
                if (drops[i] * fontSize > wave + 50) {
                    drops[i] = 0;
                }
            }
        }

        setInterval(draw, 33);

        window.onresize = () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        };
    </script>
    """
    components.html(matrix_code, height=0) # height=0 因為我們是用 fixed 定位在 body

# 執行背景功能
matrix_aurora_bg()

# Streamlit 頁面內容
st.title("GSS Solutions Day 2026")
st.subheader("精準解題，持續演進")

with st.container():
    st.write("---")
    st.markdown("""
    ### 數位轉型 x AI 自動化
    這是一個結合 **Streamlit** 與 **Matrix 視覺特效** 的官網原型。
    透過後端 Python 強大的運算能力，我們可以將自動化數據與極致的視覺體驗結合。
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("🚀 **自動化報表**已就緒")
    with col2:
        st.success("🤖 **AI 模型**運行中")

st.button("立即報名")