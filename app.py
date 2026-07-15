import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="V數據工作室 | Data Studio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .stApp, .main, .block-container { margin: 0 !important; padding: 0 !important; }
        iframe { border: none !important; margin: 0 !important; padding: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_content = r"""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>V數據工作室</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }

html, body {
    background: #070b23;
    color: #e9f7ff;
    font-family: "Microsoft JhengHei", "Noto Sans TC", Arial, sans-serif;
    overflow-x: hidden;
}

#particles-js { position: fixed; inset: 0; z-index: 0; }

.content {
    position: relative;
    z-index: 1;
    width: min(1400px, calc(100% - 64px));
    margin: auto;
    padding: 95px 0 100px;
}

.hero { text-align: center; margin-bottom: 80px; }
.title {
    margin-bottom: 38px;
    font-size: clamp(58px, 8vw, 118px);
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: 8px;
    background: linear-gradient(180deg, #38c4ff 15%, #d5f5ff 58%, #53a9ec 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.tagline {
    margin-bottom: 25px;
    color: #d9f2ff;
    font-size: clamp(25px, 2.2vw, 39px);
    font-weight: 700;
    line-height: 1.55;
    text-align: left;
}
.description {
    color: #d4eaff;
    font-size: clamp(20px, 1.75vw, 30px);
    line-height: 1.8;
    letter-spacing: 2px;
    text-align: left;
}
.intro {
    margin: 0 auto 100px;
    padding: 38px 42px;
    border-left: 3px solid rgba(91, 200, 255, .75);
    background: rgba(8, 18, 52, .42);
    backdrop-filter: blur(8px);
    color: #d9efff;
    font-size: clamp(20px, 1.7vw, 29px);
    line-height: 1.65;
    letter-spacing: 1px;
}

.section-heading { margin: 105px 0 28px; text-align: center; }
.section-heading h2 {
    margin-bottom: 14px;
    color: #81d8ff;
    font-size: clamp(34px, 4vw, 56px);
    letter-spacing: 5px;
}
.section-heading p { color: #c8e9f8; font-size: 20px; line-height: 1.7; }

.scene {
    position: relative;
    min-height: 730px;
    overflow: hidden;
    border: 1px solid rgba(125, 208, 255, .3);
    border-radius: 30px;
    background:
        radial-gradient(circle at 50% 45%, rgba(23, 106, 181, .32), transparent 36%),
        linear-gradient(135deg, rgba(6, 16, 51, .94), rgba(12, 30, 73, .9));
    box-shadow: 0 0 55px rgba(42, 154, 255, .2);
}
.scene-note {
    position: absolute;
    top: 28px;
    left: 32px;
    z-index: 10;
    color: #ccefff;
    font-size: 17px;
    letter-spacing: 1px;
    opacity: .88;
}

/* 共用資料表與儀表板 */
.data-sheet, .medical-table, .dashboard {
    position: absolute;
    left: 50%;
    top: 53%;
    transform: translate(-50%, -50%) scale(.82);
    opacity: 0;
}
.data-sheet { width: min(660px, 86%); }
.medical-table { width: min(840px, 90%); }
.dashboard {
    width: min(720px, 88%);
    padding: 26px;
    border: 1px solid rgba(105, 213, 255, .6);
    border-radius: 20px;
    background: #091426;
    box-shadow: 0 15px 55px rgba(0, 0, 0, .55);
}
.dashboard-title { margin-bottom: 18px; color: #e5f7ff; font-size: 21px; font-weight: 700; }
.metrics { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 18px; }
.metric { padding: 13px; border-radius: 10px; background: #121f36; }
.metric small { display: block; margin-bottom: 6px; color: #9db5c8; }
.metric b { color: #73dbff; font-size: 23px; }
.chart-row { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
.chart-box { min-height: 175px; padding: 14px; border-radius: 12px; background: #101c31; }
.chart-box small { color: #b8d6e6; }

/* 醫療研究動畫 */
.medical-scene { min-height: 790px; }
.document {
    position: absolute;
    width: 205px;
    min-height: 255px;
    padding: 16px;
    border-radius: 8px;
    background: #f8f8f5;
    color: #26313b;
    box-shadow: 0 18px 28px rgba(0, 0, 0, .48);
    font-family: Arial, "Microsoft JhengHei", sans-serif;
}
.document::before { content: ""; position: absolute; inset: 10px; border: 1px solid rgba(45, 65, 77, .3); }
.document h4 { position: relative; margin-bottom: 15px; font-size: 16px; text-align: center; }
.document p { position: relative; margin: 8px 0; font-size: 12px; line-height: 1.35; }
.consent { top: 160px; left: 7%; transform: rotate(-7deg); }
.emr { top: 390px; left: 26%; transform: rotate(4deg); }
.pathology { top: 130px; right: 8%; transform: rotate(6deg); }
.csv-code { position: relative; margin-top: 10px; padding: 9px; color: #0d6940; font-size: 10px; line-height: 1.45; background: #eaf5ee; border: 1px solid #bfdcc8; }

.data-token {
    position: absolute;
    z-index: 4;
    padding: 7px 11px;
    border: 1px solid rgba(136, 226, 255, .7);
    border-radius: 16px;
    background: rgba(14, 92, 139, .9);
    color: #e3f9ff;
    font-size: 13px;
    opacity: 0;
}
.t1 { left: 18%; top: 29%; }.t2 { left: 34%; top: 20%; }.t3 { left: 51%; top: 31%; }
.t4 { right: 22%; top: 33%; }.t5 { right: 17%; bottom: 23%; }.t6 { left: 34%; bottom: 20%; }

.structured-label {
    padding: 12px 16px;
    border-radius: 14px 14px 0 0;
    background: linear-gradient(90deg, #116c91, #2aa86f);
    color: white;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 2px;
}
.medical-grid, .sheet-grid { display: grid; overflow: hidden; background: #f8fcff; color: #293d4a; }
.medical-grid { grid-template-columns: 1fr .8fr .8fr 1.1fr 1fr 1.2fr; border-radius: 0 0 14px 14px; font-size: 13px; }
.medical-grid div, .sheet-grid div { padding: 11px 8px; border-right: 1px solid #c8dbe4; border-bottom: 1px solid #c8dbe4; }
.medical-grid .head { color: white; font-weight: 700; background: #2a627d; }

.donut-wrap { display: flex; align-items: center; justify-content: center; height: 125px; }
.donut {
    width: 112px;
    height: 112px;
    border-radius: 50%;
    background: conic-gradient(#51c7ff 0 42%, #ed73b7 42% 68%, #63d7a4 68% 83%, #ffc65a 83% 100%);
    animation: rotateDonut 4s linear infinite;
}
