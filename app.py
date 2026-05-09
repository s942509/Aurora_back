import streamlit as st
import streamlit.components.v1 as components

# --- 步驟 1：基礎設定 ---
st.set_page_config(page_title="數據工作室 | Data Studio", layout="wide")

# --- 步驟 2：3D 星空粒子腳本 (Three.js) ---
# 這段 JavaScript 會在背景繪製動態星系，並隨游標移動產生視差效果
starfield_js = """
<div id="canvas-container" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
    let scene, camera, renderer, stars, starGeo;
    function init() {
        scene = new THREE.Scene();
        camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);
        camera.position.z = 1;
        camera.rotation.x = Math.PI/2;

        renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.getElementById('canvas-container').appendChild(renderer.domElement);

        starGeo = new THREE.BufferGeometry();
        let starCoords = [];
        for (let i = 0; i < 6000; i++) {
            starCoords.push(Math.random() * 600 - 300);
            starCoords.push(Math.random() * 600 - 300);
            starCoords.push(Math.random() * 600 - 300);
        }
        starGeo.setAttribute('position', new THREE.Float32BufferAttribute(starCoords, 3));
        
        let sprite = new THREE.TextureLoader().load('https://threejs.org/examples/textures/sprites/disc.png');
        let starMaterial = new THREE.PointsMaterial({
            color: 0xaaaaaa,
            size: 0.7,
            map: sprite,
            transparent: true
        });

        stars = new THREE.Points(starGeo, starMaterial);
        scene.add(stars);

        window.addEventListener('resize', onWindowResize, false);
        animate();
    }
    function onWindowResize() {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    }
    function animate() {
        starGeo.attributes.position.array.forEach((val, index) => {
            if (index % 3 === 1) { // 模擬粒子向下移動
                starGeo.attributes.position.array[index] -= 0.2;
                if (starGeo.attributes.position.array[index] < -300) {
                    starGeo.attributes.position.array[index] = 300;
                }
            }
        });
        starGeo.attributes.position.needsUpdate = true;
        stars.rotation.y += 0.002;
        renderer.render(scene, camera);
        requestAnimationFrame(animate);
    }
    init();
</script>
"""

# 注入星空背景
components.html(starfield_js, height=0)

# --- 步驟 3：CSS 樣式設計 (漸層、光暈、半透明表單) ---
st.markdown("""
<style>
    /* 強制將所有 Streamlit 的容器設為透明 */
    .stApp, .main, .block-container, [data-testid="stHeader"] {
        background: transparent !important;
    }

    /* 確保文字與內容在透明背景上清晰可見 */
    h1, h2, h3, p, span, label {
        color: white !important;
    }

    /* 1. 漸層文字與漸出動畫 */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .gradient-title {
        font-size: 70px;
        font-weight: bold;
        text-align: center;
        /* 使用你提供的圖二顏色 */
        background: linear-gradient(to right, #FFABAB, #83C9FF, #0068C9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeIn 2.5s ease-out;
        margin: 80px 0;
    }

    /* 2. 縮小圖與光暈 hover 特效 */
    .case-card {
        position: relative;
        width: 350px;
        margin: 0 auto;
        border-radius: 15px;
        overflow: hidden;
        transition: 0.4s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .case-card:hover {
        transform: scale(1.05);
        box-shadow: 0 0 25px 15px rgba(131, 201, 255, 0.4);
    }
    .overlay-text {
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-size: 22px;
        font-weight: bold;
        opacity: 0;
        transition: 0.3s;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }
    .case-card:hover .overlay-text {
        opacity: 1;
    }
    .case-card:hover img {
        filter: brightness(0.4) blur(2px);
    }

    /* 3. 半透明聯絡區域 */
    .contact-container {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(15px);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 100px auto;
        max-width: 900px;
    }
</style>
""", unsafe_allow_html=True)

# --- 步驟 4：頁面內容渲染 ---

# 漸層大標題
st.markdown('<div class="gradient-title">數據工作室</div>', unsafe_allow_html=True)

# 參考案例區 (點擊跳轉)
case_url = "https://marketing-objectives-managementdashboard-mlxu3hfgu6pzpysxirvjm.streamlit.app/"
# 這裡建議將你的圖片上傳 GitHub 後替換此 URL
demo_img = "https://github.com/s942509/Aurora_back/blob/main/demo_img.png?raw=true"

# 聯絡表單區
st.markdown('<div class="contact-container">', unsafe_allow_html=True)
st.subheader("聯絡我們")
st.write("歡迎與我們聯絡，讓我們一起解決您所面臨的商業挑戰！")

form_html = """
<form action="https://formsubmit.co/s942509@gmail.com" method="POST">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
        <input type="text" name="統一編號" placeholder="*統一編號" required style="padding:10px; border-radius:5px; border:none; background:rgba(255,255,255,0.1); color:white;">
        <input type="text" name="公司名稱" placeholder="*公司名稱" required style="padding:10px; border-radius:5px; border:none; background:rgba(255,255,255,0.1); color:white;">
        <input type="text" name="部門" placeholder="*部門" required style="padding:10px; border-radius:5px; border:none; background:rgba(255,255,255,0.1); color:white;">
        <input type="text" name="職稱" placeholder="*職稱" required style="padding:10px; border-radius:5px; border:none; background:rgba(255,255,255,0.1); color:white;">
        <input type="text" name="名字" placeholder="*名字" required style="padding:10px; border-radius:5px; border:none; background:rgba(255,255,255,0.1); color:white;">
        <input type="text" name="姓氏" placeholder="*姓氏" required style="padding:10px; border-radius:5px; border:none; background:rgba(255,255,255,0.1); color:white;">
    </div>
    <button type="submit" style="width:100%; margin-top:20px; padding:12px; border-radius:5px; border:none; background:#0068C9; color:white; font-size:16px; cursor:pointer;">Submit</button>
</form>
"""
st.markdown(form_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
