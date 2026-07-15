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

    #particles-js {
        position: fixed;
        inset: 0;
        z-index: 0;
    }

    .content {
        position: relative;
        z-index: 1;
        width: min(1400px, calc(100% - 64px));
        margin: auto;
        padding: 95px 0 100px;
    }

    .hero { text-align: center; margin-bottom: 80px; }

    .title {
        font-size: clamp(58px, 8vw, 118px);
        font-weight: 800;
        letter-spacing: 8px;
        line-height: 1.15;
        margin-bottom: 38px;
        background: linear-gradient(180deg, #38c4ff 15%, #d5f5ff 58%, #53a9ec 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 10px 22px rgba(37, 156, 255, .18);
    }

    .tagline {
        text-align: left;
        font-size: clamp(25px, 2.2vw, 39px);
        font-weight: 700;
        line-height: 1.55;
        color: #d9f2ff;
        margin-bottom: 25px;
    }

    .description {
        text-align: left;
        font-size: clamp(20px, 1.75vw, 30px);
        line-height: 1.8;
        letter-spacing: 2px;
        color: #d4eaff;
    }

    .intro {
        font-size: clamp(20px, 1.7vw, 29px);
        line-height: 1.65;
        letter-spacing: 1px;
        color: #d9efff;
        margin: 0 auto 110px;
        padding: 38px 42px;
        border-left: 3px solid rgba(91, 200, 255, .75);
        background: rgba(8, 18, 52, .42);
        backdrop-filter: blur(8px);
    }

    .section-heading {
        text-align: center;
        margin: 110px 0 28px;
    }

    .section-heading h2 {
        font-size: clamp(34px, 4vw, 56px);
        color: #81d8ff;
        letter-spacing: 5px;
        margin-bottom: 14px;
    }

    .section-heading p {
        font-size: 20px;
        color: #c8e9f8;
        line-height: 1.7;
    }

    /* 共用動畫舞台 */
    .scene {
        position: relative;
        min-height: 700px;
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
        opacity: .85;
    }

    /* ========== 動畫一：行銷資料整合 ========== */
    .island {
        position: absolute;
        width: 165px;
        height: 110px;
        border-radius: 50%;
        background:
            radial-gradient(ellipse at 50% 38%, #58ce82 0 22%, #2e8c56 23% 35%, #174e43 36% 55%, transparent 56%),
            radial-gradient(ellipse at 50% 78%, #1676ae 0 38%, transparent 40%);
        filter: drop-shadow(0 18px 12px rgba(0, 0, 0, .55));
        transition: all 1.2s cubic-bezier(.55, .05, .25, 1);
    }

    .flag {
        position: absolute;
        top: 2px;
        left: 70px;
        width: 4px;
        height: 48px;
        background: #dff8ff;
    }

    .flag span {
        position: absolute;
        top: 0;
        left: 4px;
        min-width: 48px;
        padding: 4px 7px;
        border-radius: 0 5px 5px 0;
        color: white;
        font-size: 11px;
        font-weight: 700;
        text-align: center;
        background: #1877f2;
    }

    .flag.google span { background: #4285f4; }
    .flag.line span { background: #06c755; }
    .flag.money span { background: #e0a51b; }

    .m1 { left: 7%; top: 36%; }
    .m2 { right: 8%; top: 23%; }
    .m3 { left: 18%; bottom: 10%; }
    .m4 { right: 17%; bottom: 10%; }

    .marketing-scene.run .m1 { transform: translate(330px, 100px) scale(.72); opacity: 0; }
    .marketing-scene.run .m2 { transform: translate(-340px, 180px) scale(.72); opacity: 0; }
    .marketing-scene.run .m3 { transform: translate(195px, -170px) scale(.72); opacity: 0; }
    .marketing-scene.run .m4 { transform: translate(-230px, -170px) scale(.72); opacity: 0; }

    .data-sheet, .dashboard {
        position: absolute;
        left: 50%;
        top: 52%;
        width: min(660px, 86%);
        transform: translate(-50%, -50%) scale(.7);
        opacity: 0;
        transition: all .8s ease;
    }

    .marketing-scene.run .data-sheet {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1);
        transition-delay: 2.8s;
    }

    .marketing-scene.run .data-sheet {
        animation: fadeSheet 3.7s forwards;
    }

    @keyframes fadeSheet {
        0%, 74% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
        100% { opacity: 0; transform: translate(-50%, -50%) scale(.88); }
    }

    .sheet-window {
        overflow: hidden;
        border: 1px solid #8edcff;
        border-radius: 14px;
        background: #f7fbff;
        box-shadow: 0 15px 45px rgba(0, 0, 0, .45);
        color: #25364b;
    }

    .sheet-top {
        padding: 12px 16px;
        background: #1a9b59;
        color: white;
        font-weight: 700;
        font-size: 16px;
    }

    .sheet-grid {
        display: grid;
        grid-template-columns: 1.2fr .9fr .9fr .9fr .9fr;
        font-size: 13px;
    }

    .sheet-grid div {
        min-height: 38px;
        padding: 10px 8px;
        border-right: 1px solid #d6e2da;
        border-bottom: 1px solid #d6e2da;
    }

    .sheet-grid .head {
        color: white;
        font-weight: 700;
        background: #3b7f5d;
    }

    .dashboard {
        padding: 26px;
        border: 1px solid rgba(105, 213, 255, .6);
        border-radius: 20px;
        background: #091426;
        box-shadow: 0 15px 55px rgba(0, 0, 0, .55);
    }

    .marketing-scene.run .marketing-dashboard {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1);
        transition-delay: 6.8s;
    }

    .dashboard-title {
        margin-bottom: 18px;
        color: #e5f7ff;
        font-size: 21px;
        font-weight: 700;
    }

    .metrics {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
        margin-bottom: 18px;
    }

    .metric {
        padding: 13px;
        border-radius: 10px;
        background: #121f36;
    }

    .metric small { display: block; color: #9db5c8; margin-bottom: 6px; }
    .metric b { color: #73dbff; font-size: 23px; }

    .chart-row {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 18px;
    }

    .chart-box {
        min-height: 175px;
        padding: 14px;
        border-radius: 12px;
        background: #101c31;
    }

    .chart-box small { color: #b8d6e6; }

    .bars {
        height: 124px;
        display: flex;
        align-items: end;
        justify-content: space-around;
        gap: 10px;
        padding-top: 15px;
    }

    .bar {
        width: 18%;
        border-radius: 6px 6px 0 0;
        background: linear-gradient(180deg, #5ccfff, #3c7bf5);
        animation: barMove 1.7s ease-in-out infinite alternate;
    }

    .bar:nth-child(2) { animation-delay: .2s; background: linear-gradient(180deg, #f76ec8, #9c5fff); }
    .bar:nth-child(3) { animation-delay: .5s; }
    .bar:nth-child(4) { animation-delay: .1s; background: linear-gradient(180deg, #5bd9a3, #31a46d); }
    .bar:nth-child(5) { animation-delay: .4s; }

    @keyframes barMove {
        from { transform: scaleY(.52); transform-origin: bottom; }
        to { transform: scaleY(1); transform-origin: bottom; }
    }

    .line-chart {
        position: relative;
        height: 124px;
        margin-top: 15px;
        overflow: hidden;
    }

    .line-chart svg {
        width: 100%;
        height: 100%;
    }

    .line-chart path {
        fill: none;
        stroke: #f46cc4;
        stroke-width: 4;
        stroke-linecap: round;
        stroke-dasharray: 400;
        stroke-dashoffset: 400;
        animation: drawLine 2.2s ease-in-out infinite alternate;
    }

    @keyframes drawLine {
        from { stroke-dashoffset: 400; opacity: .45; }
        to { stroke-dashoffset: 0; opacity: 1; }
    }

    /* ========== 動畫二：醫療研究資料結構化 ========== */
    .medical-scene { min-height: 780px; }

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
        transition: all 1.1s ease;
    }

    .document::before {
        content: "";
        position: absolute;
        inset: 10px;
        border: 1px solid rgba(45, 65, 77, .3);
        pointer-events: none;
    }

    .document h4 {
        position: relative;
        margin-bottom: 15px;
        font-size: 16px;
        text-align: center;
    }

    .document p {
        position: relative;
        margin: 8px 0;
        font-size: 12px;
        line-height: 1.35;
    }

    .consent { top: 155px; left: 7%; transform: rotate(-7deg); }
    .emr { top: 365px; left: 26%; transform: rotate(4deg); }
    .pathology { top: 125px; right: 8%; transform: rotate(6deg); }

    .csv-code {
        position: relative;
        margin-top: 10px;
        padding: 9px;
        color: #0d6940;
        font-size: 10px;
        line-height: 1.45;
        background: #eaf5ee;
        border: 1px solid #bfdcc8;
    }

    .medical-scene.run .consent { transform: translate(285px, 135px) rotate(0deg) scale(.6); opacity: 0; }
    .medical-scene.run .emr { transform: translate(105px, -75px) rotate(0deg) scale(.6); opacity: 0; }
    .medical-scene.run .pathology { transform: translate(-295px, 170px) rotate(0deg) scale(.6); opacity: 0; }

    .data-token {
        position: absolute;
        z-index: 4;
        padding: 7px 11px;
        border: 1px solid rgba(136, 226, 255, .7);
        border-radius: 16px;
        color: #e3f9ff;
        font-size: 13px;
        background: rgba(14, 92, 139, .86);
        opacity: 0;
    }

    .t1 { left: 20%; top: 27%; }
    .t2 { left: 34%; top: 19%; }
    .t3 { left: 51%; top: 30%; }
    .t4 { right: 24%; top: 32%; }
    .t5 { right: 17%; bottom: 23%; }
    .t6 { left: 34%; bottom: 20%; }

    .medical-scene.run .data-token {
        animation: flyToCenter 1.8s ease-in forwards;
        animation-delay: 2.2s;
    }

    .medical-scene.run .t2 { animation-delay: 2.45s; }
    .medical-scene.run .t3 { animation-delay: 2.7s; }
    .medical-scene.run .t4 { animation-delay: 2.95s; }
    .medical-scene.run .t5 { animation-delay: 3.15s; }
    .medical-scene.run .t6 { animation-delay: 3.35s; }

    @keyframes flyToCenter {
        0% { opacity: 0; }
        20% { opacity: 1; }
        75% { opacity: 1; transform: translate(0, 0) scale(1); }
        100% {
            opacity: 0;
            transform: translate(calc(50vw - 50% - 360px), calc(390px - 50vh)) scale(.28);
        }
    }

    .medical-table {
        position: absolute;
        left: 50%;
        top: 53%;
        width: min(840px, 90%);
        transform: translate(-50%, -50%) scale(.75);
        opacity: 0;
        transition: all .75s ease;
    }

    .medical-scene.run .medical-table {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1);
        transition-delay: 4.4s;
        animation: medicalTableOut 3.4s forwards;
    }

    @keyframes medicalTableOut {
        0%, 70% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
        100% { opacity: 0; transform: translate(-50%, -50%) scale(.88); }
    }

    .structured-label {
        padding: 12px 16px;
        border-radius: 14px 14px 0 0;
        background: linear-gradient(90deg, #116c91, #2aa86f);
        color: white;
        font-size: 18px;
        font-weight: 700;
        letter-spacing: 2px;
    }

    .medical-grid {
        display: grid;
        grid-template-columns: 1fr .8fr .8fr 1.1fr 1fr 1.2fr;
        overflow: hidden;
        border-radius: 0 0 14px 14px;
        background: #f8fcff;
        color: #293d4a;
        font-size: 13px;
    }

    .medical-grid div {
        padding: 11px 8px;
        border-right: 1px solid #c8dbe4;
        border-bottom: 1px solid #c8dbe4;
    }

    .medical-grid .head {
        color: white;
        font-weight: 700;
        background: #2a627d;
    }

    .medical-dashboard {
        top: 53%;
        width: min(760px, 88%);
    }

    .medical-scene.run .medical-dashboard {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1);
        transition-delay: 7.8s;
    }

    .donut-wrap {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 125px;
    }

    .donut {
        width: 112px;
        height: 112px;
        border-radius: 50%;
        background: conic-gradient(#51c7ff 0 42%, #ed73b7 42% 68%, #63d7a4 68% 83%, #ffc65a 83% 100%);
        animation: rotateDonut 4s linear infinite;
    }

    .donut::after {
        content: "研究\n受試者";
        white-space: pre;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 70px;
        height: 70px;
        margin: 21px;
        border-radius: 50%;
        background: #101c31;
        color: #e8f7ff;
        font-size: 12px;
        text-align: center;
    }

    @keyframes rotateDonut {
        to { transform: rotate(360deg); }
    }

    /* 參考案例 */
    .case-section {
        text-align: center;
        padding-top: 105px;
    }

    .case-label {
        margin-bottom: 24px;
        color: #d8f3ff;
        font-size: 25px;
        font-weight: 700;
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
        box-shadow: 0 0 45px rgba(79, 181, 255, .48);
        transition: transform .35s ease, box-shadow .35s ease;
    }

    .case-card:hover {
        transform: translateY(-12px) scale(1.04);
        box-shadow: 0 0 70px rgba(79, 181, 255, .85);
    }

    .case-card img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: filter .35s ease;
    }

    .case-card::after {
        content: "查看參考案例";
        position: absolute;
        inset: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(3, 10, 30, .76);
        color: white;
        font-size: 28px;
        font-weight: 700;
        opacity: 0;
        transition: opacity .35s ease;
    }

    .case-card:hover img { filter: blur(2px) brightness(.5); }
    .case-card:hover::after { opacity: 1; }

    @media (max-width: 768px) {
        .content { width: min(100% - 30px, 1400px); padding-top: 55px; }
        .title { letter-spacing: 3px; }
        .intro { padding: 25px 20px; }
        .scene { min-height: 670px; }
        .scene-note { left: 18px; right: 18px; font-size: 14px; }
        .island { transform: scale(.72); }
        .m1 { left: -5%; } .m2 { right: -5%; }
        .m3 { left: 0; } .m4 { right: 0; }
        .document { transform: scale(.72); }
        .consent { left: -5%; } .emr { left: 20%; } .pathology { right: -5%; }
        .chart-row { grid-template-columns: 1fr; }
        .dashboard { padding: 16px; }
        .metrics { gap: 7px; }
        .metric b { font-size: 16px; }
        .medical-grid { font-size: 9px; }
        .medical-grid div { padding: 7px 3px; }
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

    <section class="section-heading">
        <h2>行銷資料整合</h2>
        <p>分散的平台資料，集中為可追蹤、可決策的資訊。</p>
    </section>

    <section class="scene marketing-scene js-scene">
        <div class="scene-note">Meta、Google、LINE 與金流資料，自動集中、整理並即時視覺化</div>

        <div class="island m1"><div class="flag"><span>Meta</span></div></div>
        <div class="island m2"><div class="flag google"><span>Google</span></div></div>
        <div class="island m3"><div class="flag line"><span>LINE</span></div></div>
        <div class="island m4"><div class="flag money"><span>$ 金流</span></div></div>

        <div class="data-sheet">
            <div class="sheet-window">
                <div class="sheet-top">Google Sheets ｜ Marketing Data</div>
                <div class="sheet-grid">
                    <div class="head">日期</div><div class="head">平台</div><div class="head">曝光</div><div class="head">轉換</div><div class="head">營收</div>
                    <div>2026/07/01</div><div>Meta</div><div>82,450</div><div>1,268</div><div>$96,200</div>
                    <div>2026/07/01</div><div>Google</div><div>65,710</div><div>998</div><div>$88,750</div>
                    <div>2026/07/01</div><div>LINE</div><div>41,300</div><div>650</div><div>$48,100</div>
                    <div>2026/07/01</div><div>後台訂單</div><div>－</div><div>2,916</div><div>$233,050</div>
                </div>
            </div>
        </div>

        <div class="dashboard marketing-dashboard">
            <div class="dashboard-title">行銷成效儀表板</div>
            <div class="metrics">
                <div class="metric"><small>總曝光</small><b>189,460</b></div>
                <div class="metric"><small>轉換數</small><b>2,916</b></div>
                <div class="metric"><small>本月營收</small><b>$233K</b></div>
            </div>
            <div class="chart-row">
                <div class="chart-box">
                    <small>各平台轉換數</small>
                    <div class="bars">
                        <div class="bar" style="height:65%"></div>
                        <div class="bar" style="height:88%"></div>
                        <div class="bar" style="height:52%"></div>
                        <div class="bar" style="height:75%"></div>
                        <div class="bar" style="height:45%"></div>
                    </div>
                </div>
                <div class="chart-box">
                    <small>每日營收趨勢</small>
                    <div class="line-chart">
                        <svg viewBox="0 0 300 120" preserveAspectRatio="none">
                            <path d="M0,90 C25,70 35,85 58,60 S95,40 115,62 S145,98 170,55 S205,20 225,45 S260,72 300,25"></path>
                        </svg>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section-heading">
        <h2>醫療研究資料結構化</h2>
        <p>從受試者同意書、電子病歷與病理報告，擷取關鍵欄位並建立可分析資料庫。</p>
    </section>

    <section class="scene medical-scene js-scene">
        <div class="scene-note">OCR 關鍵字擷取 → 資料結構化 → 研究儀表板（以下皆為去識別示意資料）</div>

        <div class="document consent">
            <h4>受試者同意書</h4>
            <p>研究計畫：婦癌臨床研究</p>
            <p>受試者姓名：王○○</p>
            <p>病歷號碼：MRN-XXXX21</p>
            <p>性別：Female</p>
            <p>同意日期：2026/06/18</p>
            <p>簽署狀態：已同意</p>
        </div>

        <div class="document emr">
            <h4>Electronic Medical Record</h4>
            <div class="csv-code">
                patient_id, visit_date, dx_code<br>
                PT-0182, 2026-06-18, C54.1<br>
                PT-0182, 2026-06-22, OP-HTX<br>
                lab_hgb, stage, follow_up<br>
                11.2, FIGO_II, 2026-07-10
            </div>
        </div>

        <div class="document pathology">
            <h4>Pathology Report</h4>
            <p>Specimen: Endometrium</p>
            <p>Histologic type: Adenocarcinoma</p>
            <p>Tumor size: 6.7 cm</p>
            <p>Myometrial invasion: Present</p>
            <p>Lymph node: Negative</p>
            <p>Stage: FIGO II</p>
        </div>

        <div class="data-token t1">受試者 ID</div>
        <div class="data-token t2">同意日期</div>
        <div class="data-token t3">診斷代碼 C54.1</div>
        <div class="data-token t4">腫瘤大小 6.7 cm</div>
        <div class="data-token t5">FIGO Stage II</div>
        <div class="data-token t6">淋巴結陰性</div>

        <div class="medical-table">
            <div class="structured-label">資料結構化｜Research Database</div>
            <div class="medical-grid">
                <div class="head">subject_id</div><div class="head">consent</div><div class="head">sex</div><div class="head">diagnosis</div><div class="head">tumor_size</div><div class="head">stage</div>
                <div>PT-0182</div><div>2026-06-18</div><div>F</div><div>C54.1</div><div>6.7 cm</div><div>FIGO II</div>
                <div>PT-0217</div><div>2026-06-20</div><div>F</div><div>C53.9</div><div>3.1 cm</div><div>FIGO IB</div>
                <div>PT-0241</div><div>2026-06-22</div><div>F</div><div>C54.1</div><div>2.8 cm</div><div>FIGO I</div>
                <div>PT-0268</div><div>2026-06-24</div><div>F</div><div>C56.9</div><div>4.5 cm</div><div>FIGO III</div>
            </div>
        </div>

        <div class="dashboard medical-dashboard">
            <div class="dashboard-title">醫療研究資料儀表板</div>
            <div class="metrics">
                <div class="metric"><small>納入受試者</small><b>248</b></div>
                <div class="metric"><small>完成同意書</small><b>231</b></div>
                <div class="metric"><small>資料完整度</small><b>93.1%</b></div>
            </div>
            <div class="chart-row">
                <div class="chart-box">
                    <small>分期分布</small>
                    <div class="donut-wrap"><div class="donut"></div></div>
                </div>
                <div class="chart-box">
                    <small>每月納入個案數</small>
                    <div class="line-chart">
                        <svg viewBox="0 0 300 120" preserveAspectRatio="none">
                            <path d="M0,100 C25,84 42,92 65,72 S100,32 123,57 S155,80 180,44 S215,18 238,40 S270,58 300,20"></path>
                        </svg>
                    </div>
                </div>
            </div>
        </div>
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
        particles: {
            number: { value: 220, density: { enable: true, value_area: 800 } },
            color: { value: "#ffffff" },
            shape: { type: "circle" },
            opacity: { value: 0.55, random: false },
            size: { value: 2.3, random: true },
            line_linked: {
                enable: true,
                distance: 135,
                color: "#83c9ff",
                opacity: 0.25,
                width: 1.3
            },
            move: {
                enable: true,
                speed: 0.25,
                direction: "none",
                random: false,
                straight: false,
                out_mode: "out",
                bounce: true
            }
        },
        interactivity: {
            detect_on: "canvas",
            events: {
                onhover: { enable: true, mode: "grab" },
                onclick: { enable: true, mode: "repulse" },
                resize: true
            },
            modes: {
                grab: { distance: 140, line_linked: { opacity: 1 } },
                repulse: { distance: 220, duration: 0.5 }
            }
        },
        retina_detect: true
    });

    // 捲動進入畫面後播放一次
    const scenes = document.querySelectorAll(".js-scene");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting && !entry.target.classList.contains("run")) {
                entry.target.classList.add("run");
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.42 });

    scenes.forEach((scene) => observer.observe(scene));
</script>
</body>
</html>
"""

components.html(html_content, height=3600, scrolling=True)
