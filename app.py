import streamlit as st

# 設定網頁標題與圖示
st.set_page_config(page_title="數據工作室", layout="wide")

# --- 1. 設計流程：核心樣式與 3D 星空背景 ---
# 使用 CSS 注入背景圖與全局樣式
st.markdown(f"""
<style>
    /* 3D 星空背景設定 */
    .stApp {{
        background: url('https://images.unsplash.com/photo-1506318137071-a8e063b4b519?auto=format&fit=crop&q=80&w=2000') no-repeat center center fixed;
        background-size: cover;
    }}

    /* --- 2. 設計流程：漸層文字與漸出動畫 --- */
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    .gradient-text {{
        font-size: 80px;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(to right, #FFABAB, #83C9FF, #0068C9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeIn 3s ease-in-out;
        margin-top: 100px;
        margin-bottom: 50px;
    }}

    /* --- 3. 設計流程：縮小圖、光暈特效與點擊連結 --- */
    .case-study-container {{
        position: relative;
        width: 300px;
        margin: 0 auto;
        cursor: pointer;
        transition: transform 0.3s;
        text-align: center;
    }}

    .case-study-img {{
        width: 100%;
        border-radius: 15px;
        transition: 0.5s;
    }}

    .overlay-text {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-size: 24px;
        font-weight: bold;
        opacity: 0;
        transition: 0.5s;
        pointer-events: none;
    }}

    .case-study-container:hover .case-study-img {{
        filter: brightness(0.7) blur(2px);
        box-shadow: 0 0 30px 10px rgba(131, 201, 255, 0.6);
        transform: scale(1.05);
    }}

    .case-study-container:hover .overlay-text {{
        opacity: 1;
    }}

    /* --- 4. 設計流程：半透明聯絡資料區域 --- */
    .contact-form {{
        background-color: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 20px;
        margin-top: 100px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
    }}
    
    input, textarea {{
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }}
</style>
""", unsafe_allow_html=True)

# 渲染中間漸層文字
st.markdown('<div class="gradient-text">數據工作室</div>', unsafe_allow_html=True)

# 渲染參考案例圖片與連結
case_url = "https://marketing-objectives-managementdashboard-mlxu3hfgu6pzpysxirvjm.streamlit.app/"
# 注意：此處需更換為你圖3的實際圖片網址，目前暫用你的截圖意象替換
img_path = "https://raw.githubusercontent.com/streamlit/fluent-demo/master/img/dashboard.png" 

st.markdown(f"""
<a href="{case_url}" target="_blank" style="text-decoration: none;">
    <div class="case-study-container">
        <img src="{img_path}" class="case-study-img">
        <div class="overlay-text">參考案例</div>
    </div>
</a>
""", unsafe_allow_html=True)

# --- 5. 設計流程：請對方留下資料的區域 (FormSubmit 串接) ---
st.markdown('<div class="contact-form">', unsafe_allow_html=True)
st.subheader("聯絡我們")
st.write("歡迎與我們聯絡，讓我們一起解決您所面臨的商業挑戰！")

# 使用 FormSubmit 處理 Email 送出 (不需後端)
contact_form = f"""
<form action="https://formsubmit.co/s942509@gmail.com" method="POST">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
        <input type="text" name="統一編號" placeholder="*統一編號" required style="padding:10px; border-radius:5px;">
        <input type="text" name="公司名稱" placeholder="*公司名稱" required style="padding:10px; border-radius:5px;">
        <input type="text" name="部門" placeholder="*部門" required style="padding:10px; border-radius:5px;">
        <input type="text" name="職稱" placeholder="*職稱" required style="padding:10px; border-radius:5px;">
        <input type="text" name="名字" placeholder="*名字" required style="padding:10px; border-radius:5px;">
        <input type="text" name="姓氏" placeholder="*姓氏" required style="padding:10px; border-radius:5px;">
    </div>
    <br>
    <button type="submit" style="
        background-color: #0068C9; 
        color: white; 
        padding: 10px 30px; 
        border: none; 
        border-radius: 5px; 
        cursor: pointer;
        width: 100%;
        font-size: 18px;
    ">Submit</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)