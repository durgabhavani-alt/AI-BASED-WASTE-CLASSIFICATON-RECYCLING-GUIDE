import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="About",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CSS
# =========================================================

st.html("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 15% 20%,
            rgba(0,210,180,.08),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 75%,
            rgba(0,150,170,.06),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #061314,
            #081b1d 50%,
            #061011
        );
}

#MainMenu,
footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* =========================================================
   NAVIGATION
   ========================================================= */

.nav-title {
    text-align: center;
    color: #789c99;
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 700;
    margin: 20px 0 10px;
}

div[data-testid="stHorizontalBlock"] {
    position: relative;
    z-index: 10;
}

div[data-testid="stHorizontalBlock"] button {
    background: #0b292a !important;
    color: #d5efec !important;
    border: 1px solid #285957 !important;
    border-radius: 8px !important;
    min-height: 42px !important;
    font-weight: 600 !important;
}

div[data-testid="stHorizontalBlock"] button:hover {
    background: #174746 !important;
    border-color: #65dfd0 !important;
    color: white !important;
}

div[data-testid="stHorizontalBlock"] button:disabled {
    background: #39756e !important;
    color: white !important;
    border: 1px solid #65dfd0 !important;
    opacity: 1 !important;
}


/* =========================================================
   MAIN
   ========================================================= */

.main-area {
    max-width: 1000px;
    margin: 0 auto;
    padding: 45px 25px 30px;
}

.heading {
    text-align: center;
}

.eyebrow {
    display: inline-block;
    padding: 7px 16px;
    border: 1px solid rgba(100,230,210,.30);
    border-radius: 30px;
    color: #82e9da;
    background: rgba(20,100,95,.10);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
}

.title {
    margin-top: 18px;
    color: #f2ffff;
    font-size: 46px;
    font-weight: 800;
}

.subtitle {
    max-width: 680px;
    margin: 12px auto 0;
    color: #9dbab7;
    font-size: 15px;
    line-height: 1.7;
}


/* =========================================================
   CARDS
   ========================================================= */

.section {
    max-width: 850px;
    margin: 30px auto 0;
}

.section-title {
    color: #eafcf9;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 14px;
}

.card {
    padding: 22px;
    margin-bottom: 14px;
    border-radius: 13px;
    background: rgba(10,34,35,.78);
    border: 1px solid rgba(100,225,210,.14);
}

.card-label {
    color: #65dfd0;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.8px;
}

.card-title {
    margin-top: 7px;
    color: #efffff;
    font-size: 18px;
    font-weight: 700;
}

.card-text {
    margin-top: 8px;
    color: #91afac;
    font-size: 13px;
    line-height: 1.7;
}


/* =========================================================
   WORKFLOW
   ========================================================= */

.workflow {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 10px;
}

.workflow-card {
    padding: 17px 13px;
    min-height: 115px;
    border-radius: 11px;
    background: rgba(12,39,40,.72);
    border: 1px solid rgba(100,225,210,.12);
}

.workflow-number {
    color: #65dfd0;
    font-size: 10px;
    font-weight: 700;
}

.workflow-title {
    margin-top: 8px;
    color: #e9fbf8;
    font-size: 13px;
    font-weight: 700;
}

.workflow-text {
    margin-top: 6px;
    color: #819d9a;
    font-size: 11px;
    line-height: 1.5;
}


/* =========================================================
   FEATURES
   ========================================================= */

.feature-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
}

.feature-card {
    padding: 20px;
    border-radius: 12px;
    background: rgba(12,39,40,.72);
    border: 1px solid rgba(100,225,210,.12);
}

.feature-number {
    color: #65dfd0;
    font-size: 11px;
    font-weight: 700;
}

.feature-title {
    margin-top: 8px;
    color: #e9fbf8;
    font-size: 15px;
    font-weight: 700;
}

.feature-text {
    margin-top: 7px;
    color: #91afac;
    font-size: 12px;
    line-height: 1.6;
}


/* =========================================================
   VISION
   ========================================================= */

.vision {
    padding: 24px;
    border-radius: 13px;
    background:
        linear-gradient(
            145deg,
            rgba(15,52,53,.85),
            rgba(7,28,30,.90)
        );
    border: 1px solid rgba(100,225,210,.17);
}

.vision-title {
    color: #65dfd0;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
}

.vision-text {
    margin-top: 10px;
    color: #c4dcda;
    font-size: 14px;
    line-height: 1.7;
}


/* =========================================================
   FOOTER
   ========================================================= */

.bottom {
    text-align: center;
    color: #718d8a;
    font-size: 11px;
    margin: 35px auto 15px;
}

</style>
""")


# =========================================================
# NAVIGATION
# =========================================================

st.html("""
<div class="nav-title">
    EXPLORE PLATFORM
</div>
""")


n1, n2, n3, n4, n5 = st.columns(
    [1, 1, 1.45, 1, 1],
    gap="small"
)


with n1:
    if st.button(
        "Home",
        key="nav_home",
        use_container_width=True
    ):
        st.switch_page("pages/home.py")


with n2:
    if st.button(
        "Analyzer",
        key="nav_analyzer",
        use_container_width=True
    ):
        st.switch_page("pages/analyzer.py")


with n3:
    if st.button(
        "Recycling Guide",
        key="nav_recycling",
        use_container_width=True
    ):
        st.switch_page("pages/recycling.py")


with n4:
    st.button(
        "About",
        key="nav_about",
        use_container_width=True,
        disabled=True
    )


with n5:
    if st.button(
        "Profile",
        key="nav_profile",
        use_container_width=True
    ):
        st.switch_page("pages/profile.py")


# =========================================================
# HEADER
# =========================================================

st.html("""
<div class="main-area">

    <div class="heading">

        <div class="eyebrow">
            ABOUT THE PLATFORM
        </div>

        <div class="title">
            E-Waste Intelligence
        </div>

        <div class="subtitle">
            An AI-assisted platform designed to identify
            electronic waste and guide users towards
            responsible recycling.
        </div>

    </div>

</div>
""")


# =========================================================
# PURPOSE
# =========================================================

st.html("""
<div class="section">

    <div class="section-title">
        Purpose
    </div>

    <div class="card">

        <div class="card-label">
            WHY THIS PLATFORM
        </div>

        <div class="card-title">
            Making E-Waste Identification Easier
        </div>

        <div class="card-text">
            E-Waste Intelligence uses image-based AI analysis
            to identify electronic devices and provide
            relevant recycling and safe-handling guidance.
            The goal is to make responsible e-waste management
            simple and accessible.
        </div>

    </div>

</div>
""")


# =========================================================
# HOW IT WORKS
# =========================================================

st.html("""
<div class="section">

    <div class="section-title">
        How The Platform Works
    </div>

    <div class="workflow">

        <div class="workflow-card">
            <div class="workflow-number">01</div>
            <div class="workflow-title">Login</div>
            <div class="workflow-text">
                Access the platform.
            </div>
        </div>

        <div class="workflow-card">
            <div class="workflow-number">02</div>
            <div class="workflow-title">Analyzer</div>
            <div class="workflow-text">
                Upload an e-waste image.
            </div>
        </div>

        <div class="workflow-card">
            <div class="workflow-number">03</div>
            <div class="workflow-title">AI Analysis</div>
            <div class="workflow-text">
                Identify the device.
            </div>
        </div>

        <div class="workflow-card">
            <div class="workflow-number">04</div>
            <div class="workflow-title">Guidance</div>
            <div class="workflow-text">
                Generate device-specific guidance.
            </div>
        </div>

        <div class="workflow-card">
            <div class="workflow-number">05</div>
            <div class="workflow-title">Recycle</div>
            <div class="workflow-text">
                Follow responsible disposal steps.
            </div>
        </div>

    </div>

</div>
""")


# =========================================================
# FEATURES
# =========================================================

st.html("""
<div class="section">

    <div class="section-title">
        Key Features
    </div>

    <div class="feature-row">

        <div class="feature-card">

            <div class="feature-number">
                01
            </div>

            <div class="feature-title">
                Image-Based Analysis
            </div>

            <div class="feature-text">
                Upload an electronic waste image
                for AI-powered identification.
            </div>

        </div>


        <div class="feature-card">

            <div class="feature-number">
                02
            </div>

            <div class="feature-title">
                Device Classification
            </div>

            <div class="feature-text">
                The AI identifies the actual device
                visible in the uploaded image.
            </div>

        </div>


        <div class="feature-card">

            <div class="feature-number">
                03
            </div>

            <div class="feature-title">
                Responsible Guidance
            </div>

            <div class="feature-text">
                Provides recycling instructions
                based on the identified device.
            </div>

        </div>

    </div>

</div>
""")


# =========================================================
# TECHNOLOGY
# =========================================================

st.html("""
<div class="section">

    <div class="section-title">
        Technology Foundation
    </div>

    <div class="card">

        <div class="card-label">
            PLATFORM TECHNOLOGY
        </div>

        <div class="card-title">
            Python · Streamlit · Gemini AI
        </div>

        <div class="card-text">
            The platform is developed using Python and Streamlit,
            with Gemini AI providing image-based analysis and
            device-specific recycling guidance.
        </div>

    </div>

</div>
""")


# =========================================================
# VISION
# =========================================================

st.html("""
<div class="section">

    <div class="vision">

        <div class="vision-title">
            VISION
        </div>

        <div class="vision-text">
            Build a practical digital solution that helps people
            understand electronic waste, handle it safely, and
            make better recycling decisions.
        </div>

    </div>

</div>
""")


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="bottom">
    E-Waste Intelligence · AI-assisted responsible e-waste management
</div>
""")