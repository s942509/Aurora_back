import streamlit as st
import streamlit.components.v1 as components

# --- 步驟 1：基礎設定 ---
st.set_page_config(page_title="數據工作室 | Data Studio", layout="wide")

# --- 步驟 2：3D 星空粒子腳本 ---
# 修正重點：確保渲染器背景為透明，並將 z-index 設為 -1
starfield_js = """
<style>
    body { margin: 0; overflow: hidden; background: black; }
    #canvas-container { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; }
</style>
<div id="canvas-container"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
    let scene, camera, renderer, stars, starGeo;
    function init() {
        scene = new THREE.Scene();
        camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);
        camera.position.z = 1;
        camera.rotation.x = Math.PI/2;

        renderer = new THREE.WebGLRenderer({ alpha: true }); // 關鍵：開啟透明度
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
        let positions = starGeo.attributes.position.array;
        for (let i = 1; i < positions.length; i += 3) {
            positions[i] -= 0.2;
            if (positions[i] < -300) positions[i] = 300;
        }
        starGeo.attributes.position.needsUpdate = true;
        stars.rotation.y += 0.002;
        renderer.render(scene, camera);
        requestAnimationFrame(animate);
    }
    init();
</script>
"""

# 注入星空背景 (高度設為 0 以避免佔位)
components.html(starfield_js, height=0)

# --- 步驟 3：CSS 樣式設計 ---
st.markdown("""
<style>
    /* 讓 Streamlit 元件變透明以顯露背景粒子 */
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

    /* 案例圖片縮圖與光暈效果 */
    .case-container {
        display: flex;
        justify-content: center;
        margin-bottom: 50px;
    }
    .case-card {
        position: relative;
        width: 10%; /* ← 這裡就是控制大小的地方，你可以把它改小 */
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
        color: white !important;
        font-size: 24px;/* ← 這裡就是調整文字"參考案例"大小的地方 */
        font-weight: bold;
        opacity: 0;
        transition: 0.3s;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.9);
        white-space: nowrap;
    }
    .case-card:hover .overlay-text {
        opacity: 1;
    }
    .case-card:hover img {
        filter: brightness(0.3) blur(2px);
    }

    /* 聯絡區域樣式 */
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

# --- 步驟 4：頁面內容渲染 ---

# 1. 漸層大標題
st.markdown('<div class="gradient-title">數據工作室</div>', unsafe_allow_html=True)

# 2. 參考案例區 (修正：補上 HTML 結構以顯示圖片)
case_url = "https://marketing-objectives-managementdashboard-mlxu3hfgu6pzpysxirvjm.streamlit.app/"
demo_img = "https://github.com/s942509/Aurora_back/blob/main/demo_img.png?raw=true"

case_html = f"""
<div class="case-container">
    <a href="{case_url}" target="_blank" style="text-decoration: none;">
        <div class="case-card">
            <img src="{demo_img}" alt="Case Study">
            <div class="overlay-text">參考案例</div>
        </div>
    </a>
</div>
"""
st.markdown(case_html, unsafe_allow_html=True)

# 3. 聯絡表單區
st.markdown('<div class="contact-container">', unsafe_allow_html=True)
st.subheader("聯絡我們")
st.write("歡迎與我們聯絡，讓我們一起解決您所面臨的商業挑戰！")

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
