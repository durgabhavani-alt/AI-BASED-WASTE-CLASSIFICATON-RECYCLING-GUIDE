import streamlit as st
import random

st.set_page_config(
    page_title="E-Waste Intelligence",
    layout="wide",
    initial_sidebar_state="collapsed"
)

random.seed(42)

particles = ""

for _ in range(30):
    left = random.randint(2, 98)
    top = random.randint(5, 95)
    size = random.choice([2, 3, 4])
    delay = round(random.uniform(0, 7), 2)
    duration = round(random.uniform(7, 12), 2)

    particles += f"""
    <span class="particle" style="
        left:{left}%;
        top:{top}%;
        width:{size}px;
        height:{size}px;
        animation-delay:{delay}s;
        animation-duration:{duration}s;
    "></span>
    """

st.html(f"""
<style>

.stApp {{
    background:
        radial-gradient(circle at 15% 20%, rgba(0,210,180,.10), transparent 30%),
        radial-gradient(circle at 85% 75%, rgba(0,150,170,.08), transparent 30%),
        linear-gradient(135deg, #061314, #081b1d 50%, #061011);
}}

#MainMenu,
footer {{
    visibility: hidden;
}}

header {{
    background: transparent !important;
}}

.particle {{
    position: fixed;
    border-radius: 50%;
    background: rgba(95,245,220,.8);
    box-shadow: 0 0 9px rgba(70,240,215,.7);
    pointer-events: none;
    z-index: 0;
    animation: flow 10s linear infinite;
}}

@keyframes flow {{
    0% {{
        transform: translate(0, 35px);
        opacity: 0;
    }}
    20% {{
        opacity: .7;
    }}
    50% {{
        transform: translate(40px, -50px);
        opacity: .9;
    }}
    100% {{
        transform: translate(-20px, -115px);
        opacity: 0;
    }}
}}

.hero {{
    position: relative;
    z-index: 2;
    text-align: center;
    padding: 48px 20px 30px 20px;
}}

.eyebrow {{
    display: inline-block;
    padding: 8px 17px;
    border: 1px solid rgba(100,230,210,.35);
    border-radius: 30px;
    color: #8af0df;
    background: rgba(20,100,95,.12);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}}

.title {{
    margin-top: 20px;
    font-size: clamp(44px, 6vw, 72px);
    font-weight: 800;
    letter-spacing: -3px;
    line-height: 1.05;
    color: #f4ffff;
    text-shadow: 0 0 35px rgba(70,230,210,.20);
}}

.subtitle {{
    margin-top: 15px;
    font-size: 21px;
    font-weight: 500;
    color: #b8e4df;
}}

.description {{
    max-width: 720px;
    margin: 15px auto 0 auto;
    color: #9ab8b5;
    font-size: 15px;
    line-height: 1.8;
}}

/* Navigation buttons */

div[data-testid="stHorizontalBlock"] button {{
    min-height: 42px !important;
    border-radius: 9px !important;
    border: 1px solid rgba(100,220,205,.28) !important;
    background: rgba(13,45,46,.90) !important;
    color: #d9f8f4 !important;
    font-weight: 600 !important;
}}

div[data-testid="stHorizontalBlock"] button:hover {{
    border-color: #65e4d2 !important;
    background: rgba(35,91,88,.95) !important;
    color: #ffffff !important;
}}

/* Feature cards */

.feature-box {{
    padding: 28px;
    min-height: 220px;
    border-radius: 18px;
    border: 1px solid rgba(100,225,210,.22);
    background:
        linear-gradient(
            145deg,
            rgba(18,53,54,.94),
            rgba(8,31,33,.96)
        );
    box-shadow:
        0 15px 45px rgba(0,0,0,.28),
        inset 0 1px 0 rgba(255,255,255,.05);
}}

.feature-label {{
    color: #6ee6d5;
    font-size: 11px;
    letter-spacing: 2px;
    font-weight: 700;
}}

.feature-title {{
    margin-top: 13px;
    color: #f1ffff;
    font-size: 23px;
    font-weight: 750;
}}

.feature-text {{
    margin-top: 11px;
    color: #aac5c2;
    font-size: 14px;
    line-height: 1.7;
}}

</style>

{particles}

<div class="hero">

    <div class="eyebrow">
        INTELLIGENT E-WASTE MANAGEMENT
    </div>

    <div class="title">
        E-Waste Intelligence
    </div>

    <div class="subtitle">
        Smarter Classification. Greener Tomorrow.
    </div>

    <div class="description">
        Identify electronic waste intelligently and discover
        responsible recycling guidance through one unified platform.
    </div>

</div>
""")

# -----------------------------
# CENTER NAVIGATION
# -----------------------------

st.markdown(
    """
    <div style="
        text-align:center;
        color:#82aaa6;
        font-size:11px;
        letter-spacing:2px;
        margin:8px 0 12px 0;
        font-weight:600;
    ">
        EXPLORE PLATFORM
    </div>
    """,
    unsafe_allow_html=True
)

n1, n2, n3, n4, n5 = st.columns(
    [1, 1, 1.45, 1, 1],
    gap="small"
)

with n1:
    st.button("Home", use_container_width=True)

with n2:
    if st.button("Analyzer", use_container_width=True):
        st.switch_page("pages/analyzer.py")

with n3:
    if st.button("Recycling Guide", use_container_width=True):
        st.switch_page("pages/recycling.py")

with n4:
    if st.button("About", use_container_width=True):
        st.switch_page("pages/about.py")

with n5:
    if st.button("Profile", use_container_width=True):
        st.switch_page("pages/profile.py")

st.write("")
st.write("")

# -----------------------------
# FEATURE CARDS
# -----------------------------

col1, col2 = st.columns(2, gap="large")

with col1:

    st.html("""
    <div class="feature-box">

        <div class="feature-label">
            01 / ANALYSIS
        </div>

        <div class="feature-title">
            E-Waste Analyzer
        </div>

        <div class="feature-text">
            Upload an electronic waste image and analyze
            its category using the intelligent classification
            system.
        </div>

    </div>
    """)

    st.write("")

    if st.button(
        "Open Analyzer  →",
        key="open_analyzer",
        use_container_width=True
    ):
        st.switch_page("pages/analyzer.py")


with col2:

    st.html("""
    <div class="feature-box">

        <div class="feature-label">
            02 / GUIDANCE
        </div>

        <div class="feature-title">
            Recycling Guide
        </div>

        <div class="feature-text">
            Explore responsible handling, disposal and
            recycling guidance for electronic waste.
        </div>

    </div>
    """)

    st.write("")

    if st.button(
        "Open Recycling Guide  →",
        key="open_recycling",
        use_container_width=True
    ):
        st.switch_page("pages/recycling.py")