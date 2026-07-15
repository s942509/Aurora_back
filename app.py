import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="V數據工作室 | Data Studio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .stApp, .main, .block-container {
        margin: 0 !important;
        padding: 0 !important;
    }
    iframe {
        border: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

html_content = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>V數據工作室</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html, body {
            min-height: 100%;
            background: linear-gradient(135deg, #070b23 0%, #111a3d 100%);
            color: #e8f7ff;
            font-family: "Microsoft JhengHei", "Noto Sans TC", Arial, sans-serif;
            overflow-x: hidden;
        }

        #particles-js {
            position: fixed;
            inset: 0;
            z-index: 0;
        }

        .content {
            position: relative;
            z-index: 1;
            width: min(1400px, calc(100% - 64px));
            margin: 0 auto;
            padding: 95px 0 90px;
        }

        .hero {
            text-align: center;
            margin-bottom: 62px;
        }

        .title {
            font-size: clamp(56px, 8vw, 118px);
            font-weight: 800;
            letter-spacing: 8px;
            line-height: 1.15;
            background: linear-gradient(180deg, #38c4ff 15%, #c8efff 58%, #53a9ec 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 10px 22px rgba(37, 156, 255, 0.18);
            margin-bottom: 42px;
        }

        .tagline {
            text-align: left;
            font-size: clamp(25px, 2.2vw, 39px);
            font-weight: 700;
            line-height: 1.55;
            color: #d9f2ff;
            margin-bottom: 30px;
            text-shadow: 0 0 16px rgba(140, 211, 255, 0.35);
        }

        .description {
            text-align: left;
            font-size: clamp(20px, 1.75vw, 30px);
            line-height: 1.8;
            letter-spacing: 2px;
            color: #d4eaff;
            margin-bottom: 62px;
        }

        .intro {
            text-align: left;
            font-size: clamp(20px, 1.7vw, 29px);
            line-height: 1.65;
            letter-spacing: 1px;
            color: #d9efff;
            max-width: 1280px;
            margin: 0 auto 85px;
            padding: 38px 42px;
            border-left: 3px solid rgba(91, 200, 255, 0.75);
            background: rgba(8, 18, 52, 0.32);
            backdrop-filter: blur(8px);
        }

        .case-section {
            text-align: center;
            padding-top: 15px;
        }

        .case-label {
            font-size: 25px;
            font-weight: 700;
            color: #d8f3ff;
            margin-bottom: 24px;
            letter-spacing: 3px;
        }

        .case-card {
            display: inline-block;
            position: relative;
            width: min(330px, 85vw);
            height: 330px;
            overflow: hidden;
            border-radius: 28px;
            text-decoration: none;
            box-shadow: 0 0 45px rgba(79, 181, 255, 0.48);
            transition: transform 0.35s ease, box-shadow 0.35s ease;
        }

        .case-card:hover {
            transform: translateY(-12px) scale(1.04);
            box-shadow: 0 0 70px rgba(79, 181, 255, 0.85);
        }

        .case-card img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: filter 0.35s ease;
        }

        .case-card::after {
            content: "查看參考案例";
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(3, 10, 30, 0.76);
            color: white;
            font-size: 28px;
            font-weight: 700;
            opacity: 0;
            transition: opacity 0.35s ease;
        }

        .case-card:hover img {
            filter: blur(2px) brightness(0.5);
        }

        .case-card:hover::after {
            opacity: 1;
        }

        @media (max-width: 768px) {
            .content {
                width: min(100% - 36px, 1400px);
                padding: 60px 0;
            }

            .title {
                letter-spacing: 3px;
                margin-bottom: 30px;
            }

            .intro {
                padding: 26px 22px;
            }

            .case-card {
                height: 280px;
            }
        }
    </style>
</head>
<body>
    <div id="particles-js"></div>

    <main class="content">
        <section class="hero">
            <h1 class="title">V數據工作室</h1>

            <p class="tagline">繁瑣流程自動化，放大您的決策價值</p>

            <p class="description">
                協助打造專屬自動化流程，整合 Excel、Google Sheets、資料庫與儀錶板，
                讓每天重複的工作一鍵完成。
            </p>
        </section>

        <section class="intro">
            大家好，我是 Ivy。曾參與台灣國科會大數據建構計畫，協助醫療體系建立研究資料架構。<br>
            我相信，AI 的價值，不在於模型有多厲害，而在於是否建立在好的資料流程之上。<br>
            我希望透過資料整理、自動化與 AI 應用，協助企業與研究團隊減少重複工作，
            讓數據真正成為決策的力量。
        </section>

        <section class="case-section">
            <p class="case-label">參考案例</p>

            <a class="case-card"
               href="https://marketing-objectives-managementdashboard-mlxu3hfgu6pzpysxirvjm.streamlit.app/"
               target="_blank"
               rel="noopener noreferrer">
                <img src="https://github.com/s942509/Aurora_back/blob/main/demo_img.png?raw=true"
                     alt="參考案例">
            </a>
        </section>
    </main>

    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS("particles-js", {
            "particles": {
                "number": {
                    "value": 280,
                    "density": { "enable": true, "value_area": 800 }
                },
                "color": { "value": "#ffffff" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.6, "random": false },
                "size": { "value": 2.5, "random": true },
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
                    "bounce": true
                }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": { "enable": true, "mode": "grab" },
                    "onclick": { "enable": true, "mode": "repulse" },
                    "resize": true
                },
                "modes": {
                    "grab": {
                        "distance": 140,
                        "line_linked": { "opacity": 1 }
                    },
                    "repulse": {
                        "distance": 220,
                        "duration": 0.5
                    }
                }
            },
            "retina_detect": true
        });
    </script>
</body>
</html>
"""

components.html(html_content, height=1250, scrolling=True)
