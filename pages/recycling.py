import streamlit as st
import html


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Recycling Guide",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# GET AI ANALYSIS RESULT
# =========================================================

detected_device = st.session_state.get(
    "detected_device",
    ""
)

device_category = st.session_state.get(
    "device_category",
    ""
)

device_description = st.session_state.get(
    "device_description",
    ""
)

recycling_guidance = st.session_state.get(
    "recycling_guidance",
    []
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
            rgba(0,210,180,.10),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 75%,
            rgba(0,150,170,.08),
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
    color: #ffffff !important;
}


/* ACTIVE BUTTON */

div[data-testid="stHorizontalBlock"] button:disabled {
    background: #39756e !important;
    color: #ffffff !important;
    border: 1px solid #65dfd0 !important;
    opacity: 1 !important;
}


/* =========================================================
   MAIN AREA
   ========================================================= */

.main-area {
    position: relative;
    z-index: 2;
    max-width: 1050px;
    margin: 0 auto;
    padding: 40px 25px 20px;
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
    background: rgba(20,100,95,.12);
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
   DETECTED DEVICE
   ========================================================= */

.device-area {
    max-width: 850px;
    margin: 30px auto 0;
}

.device-card {
    padding: 22px 24px;
    border-radius: 14px;
    background:
        linear-gradient(
            145deg,
            rgba(15,52,53,.92),
            rgba(7,28,30,.95)
        );
    border: 1px solid rgba(100,225,210,.20);
}

.device-label {
    color: #65dfd0;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
}

.device-name {
    margin-top: 8px;
    color: #f1fffd;
    font-size: 27px;
    font-weight: 800;
}

.device-category {
    margin-top: 6px;
    color: #82cfc5;
    font-size: 13px;
    font-weight: 600;
}

.device-description {
    margin-top: 12px;
    color: #9dbab7;
    font-size: 13px;
    line-height: 1.65;
}


/* =========================================================
   GUIDANCE
   ========================================================= */

.guidance-area {
    max-width: 850px;
    margin: 32px auto 0;
}

.section-title {
    color: #eafcf9;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 18px;
}

.guidance-card {
    padding: 19px 22px;
    margin-bottom: 11px;
    border-left: 2px solid #4fcfc0;
    background: rgba(12,39,40,.72);
    border-radius: 0 12px 12px 0;
}

.guidance-number {
    color: #65dfd0;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
}

.guidance-text {
    margin-top: 7px;
    color: #d4e9e6;
    font-size: 13px;
    line-height: 1.65;
}


/* =========================================================
   SAFETY
   ========================================================= */

.safety-area {
    max-width: 850px;
    margin: 28px auto 0;
}

.safety-card {
    padding: 20px 23px;
    border-radius: 13px;
    background: rgba(46,61,45,.30);
    border: 1px solid rgba(180,210,150,.15);
}

.safety-label {
    color: #b8d89e;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.7px;
}

.safety-text {
    margin-top: 8px;
    color: #b8c9b8;
    font-size: 13px;
    line-height: 1.65;
}


/* =========================================================
   NO ANALYSIS
   ========================================================= */

.empty-area {
    max-width: 850px;
    margin: 35px auto 0;
}

.empty-card {
    padding: 30px;
    text-align: center;
    border-radius: 14px;
    background: rgba(10,32,33,.75);
    border: 1px solid rgba(100,225,210,.15);
}

.empty-title {
    color: #eafcf9;
    font-size: 20px;
    font-weight: 700;
}

.empty-text {
    max-width: 600px;
    margin: 10px auto 0;
    color: #91afac;
    font-size: 13px;
    line-height: 1.7;
}


/* =========================================================
   BUTTON
   ========================================================= */

.next-area {
    max-width: 420px;
    margin: 30px auto 0;
}

.next-area button {
    background: #397d76 !important;
    color: white !important;
    border: 1px solid #65dfd0 !important;
    border-radius: 9px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}

.next-area button:hover {
    background: #4d958c !important;
}


/* =========================================================
   FOOTER
   ========================================================= */

.bottom {
    position: relative;
    z-index: 2;
    text-align: center;
    max-width: 850px;
    margin: 25px auto;
    color: #718d8a;
    font-size: 12px;
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

    st.button(
        "Recycling Guide",
        key="nav_recycling",
        use_container_width=True,
        disabled=True
    )


with n4:

    if st.button(
        "About",
        key="nav_about",
        use_container_width=True
    ):
        st.switch_page("pages/about.py")


with n5:

    if st.button(
        "Profile",
        key="nav_profile",
        use_container_width=True
    ):
        st.switch_page("pages/profile.py")


# =========================================================
# PAGE HEADER
# =========================================================

st.html("""
<div class="main-area">

    <div class="heading">

        <div class="eyebrow">
            RESPONSIBLE E-WASTE MANAGEMENT
        </div>

        <div class="title">
            Recycling Guide
        </div>

        <div class="subtitle">
            View recycling and safe-handling recommendations
            based on the electronic device identified by AI.
        </div>

    </div>

</div>
""")


# =========================================================
# NO AI RESULT
# =========================================================

if not detected_device:

    st.html("""
    <div class="empty-area">

        <div class="empty-card">

            <div class="empty-title">
                No Device Analysis Available
            </div>

            <div class="empty-text">
                Upload an electronic waste image in the Analyzer
                and let the AI identify the device first.
                Device-specific recycling guidance will appear here
                after successful analysis.
            </div>

        </div>

    </div>
    """)


    st.html('<div class="next-area">')

    if st.button(
        "Go to Analyzer  →",
        key="go_analyzer",
        use_container_width=True
    ):
        st.switch_page("pages/analyzer.py")

    st.html('</div>')


# =========================================================
# AI RESULT AVAILABLE
# =========================================================

else:

    safe_device = html.escape(
        str(detected_device)
    )

    safe_category = html.escape(
        str(device_category)
    )

    safe_description = html.escape(
        str(device_description)
    )


    # =====================================================
    # DETECTED DEVICE
    # =====================================================

    st.html(f"""
    <div class="device-area">

        <div class="device-card">

            <div class="device-label">
                AI IDENTIFIED DEVICE
            </div>

            <div class="device-name">
                {safe_device}
            </div>

            <div class="device-category">
                {safe_category}
            </div>

            <div class="device-description">
                {safe_description}
            </div>

        </div>

    </div>
    """)


    # =====================================================
    # DEVICE-SPECIFIC GUIDANCE
    # =====================================================

    st.html("""
    <div class="guidance-area">

        <div class="section-title">
            Recommended Recycling Process
        </div>

    </div>
    """)


    if recycling_guidance:

        for index, guidance in enumerate(
            recycling_guidance,
            start=1
        ):

            safe_guidance = html.escape(
                str(guidance)
            )


            st.html(f"""
            <div style="
                max-width:850px;
                margin:0 auto;
            ">

                <div class="guidance-card">

                    <div class="guidance-number">
                        STEP {index:02d}
                    </div>

                    <div class="guidance-text">
                        {safe_guidance}
                    </div>

                </div>

            </div>
            """)

    else:

        st.html("""
        <div style="
            max-width:850px;
            margin:0 auto;
        ">

            <div class="guidance-card">

                <div class="guidance-text">
                    No device-specific guidance was returned.
                    Please use an authorised e-waste recycling
                    facility for safe disposal.
                </div>

            </div>

        </div>
        """)


    # =====================================================
    # SAFETY NOTE
    # =====================================================

    st.html("""
    <div class="safety-area">

        <div class="safety-card">

            <div class="safety-label">
                GENERAL SAFETY NOTE
            </div>

            <div class="safety-text">
                Do not burn, break, or dispose of electronic
                devices with ordinary household waste.
                Damaged or swollen batteries should be handled
                with extra care and taken to an appropriate
                authorised collection or recycling facility.
            </div>

        </div>

    </div>
    """)


    # =====================================================
    # BACK TO ANALYZER
    # =====================================================

    st.html('<div class="next-area">')

    if st.button(
        "Analyze Another Device  →",
        key="analyze_another",
        use_container_width=True
    ):

        st.session_state.analysis_started = False
        st.session_state.detected_device = ""
        st.session_state.device_category = ""
        st.session_state.device_description = ""
        st.session_state.recycling_guidance = []

        st.switch_page(
            "pages/analyzer.py"
        )

    st.html('</div>')


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="bottom">
    AI-assisted classification → device-specific guidance
    → responsible e-waste recycling.
</div>
""")