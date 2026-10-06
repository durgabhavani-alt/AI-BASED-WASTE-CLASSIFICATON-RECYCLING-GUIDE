import streamlit as st
import random
import os
import json
import html

from dotenv import load_dotenv
from google import genai
from google.genai import types


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="E-Waste Analyzer",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# GEMINI API
# =========================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY) if API_KEY else None


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "analysis_started": False,
    "detected_device": "",
    "device_category": "",
    "device_description": "",
    "recycling_guidance": []
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# GEMINI IMAGE ANALYSIS
# =========================================================

def analyze_image(image_bytes, mime_type):

    if client is None:
        st.warning(
            "AI service is not configured. Please check your .env file."
        )
        return None

    prompt = """
You are an advanced e-waste image classification system.

Analyze the uploaded image carefully and identify the actual electronic
device visible in the image.

Return ONLY valid JSON in exactly this structure:

{
    "device": "actual device name",
    "category": "e-waste category",
    "description": "short description of the identified device",
    "recycling_guidance": [
        "specific recycling instruction 1",
        "specific recycling instruction 2",
        "specific recycling instruction 3",
        "specific recycling instruction 4"
    ]
}

Important rules:

1. Identify the actual device visible in the image.
2. Never use "E-Waste Item" as the device name.
3. Never give a generic device name if a specific device can be identified.
4. If the image shows a mobile phone, identify it as Mobile Phone.
5. If the image shows a laptop, identify it as Laptop.
6. If the image shows a battery, identify it as Battery.
7. If the image shows a monitor, identify it as Monitor.
8. If the image shows a keyboard, identify it as Keyboard.
9. If the image shows a mouse, identify it as Computer Mouse.
10. If the image shows a charger, identify it as Charger.
11. If the image shows headphones or earphones, identify them correctly.
12. If the image is not electronic/e-waste, use:
    "Not an E-Waste Item"
13. Do not invent a device when the image is unclear.
14. Recycling guidance must be specific to the detected device.
15. Guidance must be practical and safe.
16. Consider batteries, data, cables, screens, plastics and other
    components when relevant.
17. Return JSON only.
"""


    # Current model first, fallback model second
    models = [
        "gemini-3.8-flash",
        "gemini-3.5-flash-lite"
    ]


    for model_name in models:

        try:

            response = client.models.generate_content(
                model=model_name,
                contents=[
                    prompt,
                    types.Part.from_bytes(
                        data=image_bytes,
                        mime_type=mime_type
                    )
                ]
            )


            if not response or not response.text:
                continue


            text = response.text.strip()


            # Remove markdown JSON fences if Gemini returns them
            if text.startswith("```"):
                text = text.replace("```json", "")
                text = text.replace("```", "")
                text = text.strip()


            result = json.loads(text)


            device = result.get(
                "device",
                "Unknown Device"
            )

            category = result.get(
                "category",
                "Electronic Waste"
            )

            description = result.get(
                "description",
                ""
            )

            guidance = result.get(
                "recycling_guidance",
                []
            )


            if not isinstance(guidance, list):
                guidance = [str(guidance)]


            return {
                "device": str(device),
                "category": str(category),
                "description": str(description),
                "recycling_guidance": [
                    str(item) for item in guidance
                ]
            }


        except Exception as e:

            error_text = str(e)


            # Try the next Gemini model for temporary
            # availability / quota / model errors
            if (
                "503" in error_text
                or "UNAVAILABLE" in error_text
                or "429" in error_text
                or "RESOURCE_EXHAUSTED" in error_text
                or "404" in error_text
                or "NOT_FOUND" in error_text
            ):
                continue


            # Do not show raw technical Gemini errors
            st.warning(
                "The image could not be analyzed right now. "
                "Please try again with a clear image."
            )

            return None


    # Both models unavailable
    st.warning(
        "AI service is temporarily busy. "
        "Please try analyzing the image again in a moment."
    )

    return None


# =========================================================
# BACKGROUND PARTICLES
# =========================================================

random.seed(25)

particles = ""

for _ in range(12):

    left = random.randint(5, 95)
    top = random.randint(5, 95)
    size = random.choice([2, 3])
    delay = round(random.uniform(0, 4), 1)

    particles += f"""
    <span class="particle" style="
        left:{left}%;
        top:{top}%;
        width:{size}px;
        height:{size}px;
        animation-delay:{delay}s;
    "></span>
    """


# =========================================================
# CSS
# =========================================================

st.html(f"""
<style>

.stApp {{
    background:
        radial-gradient(
            circle at 15% 15%,
            rgba(0,210,180,.07),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 80%,
            rgba(0,160,180,.06),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #061314,
            #081b1d,
            #061011
        );
}}


#MainMenu,
footer {{
    visibility: hidden;
}}

header {{
    background: transparent !important;
}}


/* PARTICLES */

.particle {{
    position: fixed;
    border-radius: 50%;
    background: rgba(90,235,215,.55);
    box-shadow: 0 0 7px rgba(80,230,210,.35);
    pointer-events: none;
    z-index: 0;
    animation: particleMove 9s ease-in-out infinite;
}}

@keyframes particleMove {{

    0% {{
        transform: translateY(30px);
        opacity: 0;
    }}

    30% {{
        opacity: .55;
    }}

    70% {{
        opacity: .3;
    }}

    100% {{
        transform: translateY(-100px);
        opacity: 0;
    }}

}}


/* NAV */

.nav-title {{
    position: relative;
    z-index: 5;
    text-align: center;
    color: #789c99;
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 700;
    margin: 18px 0 9px;
}}

div[data-testid="stHorizontalBlock"] {{
    position: relative;
    z-index: 10;
}}

div[data-testid="stHorizontalBlock"] button {{
    background: #0b292a !important;
    color: #d5efec !important;
    border: 1px solid #285957 !important;
    border-radius: 8px !important;
    min-height: 40px !important;
    font-weight: 600 !important;
}}

div[data-testid="stHorizontalBlock"] button:hover {{
    background: #174746 !important;
    border-color: #65dfd0 !important;
}}

div[data-testid="stHorizontalBlock"] button:disabled {{
    background: #39756e !important;
    color: white !important;
    border: 1px solid #65dfd0 !important;
    opacity: 1 !important;
}}


/* HEADER */

.page-header {{
    position: relative;
    z-index: 2;
    text-align: center;
    margin-top: 35px;
}}

.badge {{
    display: inline-block;
    padding: 7px 16px;
    border: 1px solid rgba(100,230,210,.30);
    border-radius: 30px;
    color: #7ee8da;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
}}

.title {{
    margin-top: 14px;
    color: #f2ffff;
    font-size: 44px;
    font-weight: 800;
}}

.subtitle {{
    max-width: 700px;
    margin: 10px auto;
    color: #9bb7b4;
    font-size: 15px;
    line-height: 1.6;
}}


/* UPLOAD */

.upload-section {{
    position: relative;
    z-index: 2;
    max-width: 820px;
    margin: 30px auto 0;
    padding: 23px;
    border-radius: 15px;
    background: linear-gradient(
        145deg,
        rgba(18,53,54,.94),
        rgba(8,30,32,.96)
    );
    border: 1px solid rgba(100,225,210,.20);
}}

.upload-label {{
    color: #68dfd0;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
}}

.upload-title {{
    margin-top: 7px;
    color: white;
    font-size: 21px;
    font-weight: 700;
}}

.upload-description {{
    margin-top: 6px;
    color: #91afac;
    font-size: 13px;
}}


/* FILE UPLOADER */

div[data-testid="stFileUploader"] {{
    position: relative;
    z-index: 20;
    max-width: 820px;
    margin: 15px auto 0;
}}

div[data-testid="stFileUploaderDropzone"] {{
    background: #0b2426 !important;
    border: 2px dashed #4f9e96 !important;
    border-radius: 14px !important;
    min-height: 140px !important;
}}

div[data-testid="stFileUploaderDropzone"]:hover {{
    border-color: #68dfd0 !important;
}}

div[data-testid="stFileUploaderDropzone"] p,
div[data-testid="stFileUploaderDropzone"] span {{
    color: white !important;
}}

div[data-testid="stFileUploaderDropzone"] small {{
    color: #b7d6d2 !important;
}}

div[data-testid="stFileUploaderDropzone"] button {{
    background: #4a8f87 !important;
    color: white !important;
    border: 1px solid #79e6d9 !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
}}


/* INFO */

.info-area {{
    position: relative;
    z-index: 2;
    max-width: 820px;
    margin: 20px auto 0;
}}

.info-card {{
    padding: 17px;
    min-height: 95px;
    border-radius: 13px;
    background: rgba(9,29,30,.75);
    border: 1px solid rgba(100,225,210,.13);
}}

.info-label {{
    color: #65dfd0;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
}}

.info-value {{
    margin-top: 8px;
    color: #e8faf7;
    font-size: 15px;
    font-weight: 650;
}}


/* PREVIEW */

.preview {{
    position: relative;
    z-index: 2;
    max-width: 820px;
    margin: 25px auto 0;
    padding: 17px;
    border-radius: 15px;
    background: rgba(8,28,30,.85);
    border: 1px solid rgba(100,225,210,.16);
}}


/* ANALYZE */

.analyze-area {{
    position: relative;
    z-index: 20;
    max-width: 400px;
    margin: 23px auto 0;
}}

.analyze-area button {{
    background: #397d76 !important;
    color: white !important;
    border: 1px solid #65dfd0 !important;
    border-radius: 9px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}}

.analyze-area button:hover {{
    background: #4d958c !important;
}}


/* RESULT */

.result {{
    position: relative;
    z-index: 2;
    max-width: 820px;
    margin: 27px auto 0;
    padding: 24px;
    border-radius: 16px;
    background: linear-gradient(
        145deg,
        rgba(14,43,44,.90),
        rgba(8,27,29,.95)
    );
    border: 1px solid rgba(100,225,210,.16);
}}

.result-title {{
    color: #efffff;
    font-size: 20px;
    font-weight: 700;
}}

.result-text {{
    margin-top: 8px;
    color: #91afac;
    font-size: 13px;
    line-height: 1.6;
}}

.result-value {{
    margin-top: 16px;
    padding: 17px;
    border-radius: 12px;
    background: rgba(6,23,25,.85);
    border: 1px solid rgba(100,225,210,.13);
}}

.result-label {{
    color: #789493;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
}}

.result-main {{
    margin-top: 6px;
    color: #68dfd0;
    font-size: 23px;
    font-weight: 750;
}}


/* GUIDANCE */

.guidance {{
    margin-top: 18px;
    padding: 18px;
    border-radius: 12px;
    background: rgba(5,22,24,.75);
    border: 1px solid rgba(100,225,210,.12);
}}

.guidance-title {{
    color: #65dfd0;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
}}

.guidance-item {{
    margin-top: 10px;
    padding: 10px 12px;
    border-left: 2px solid #4f9e96;
    color: #c6dfdc;
    font-size: 13px;
    line-height: 1.5;
}}


/* CONTINUE */

.continue-box {{
    position: relative;
    z-index: 20;
    max-width: 500px;
    margin: 25px auto 0;
}}

.continue-box button {{
    background: #397d76 !important;
    color: white !important;
    border: 1px solid #65dfd0 !important;
    border-radius: 9px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
}}

.continue-box button:hover {{
    background: #4d958c !important;
}}


/* BOTTOM */

.bottom {{
    position: relative;
    z-index: 2;
    text-align: center;
    max-width: 820px;
    margin: 22px auto;
    color: #718d8a;
    font-size: 12px;
}}

</style>

{particles}
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

    st.button(
        "Analyzer",
        key="nav_analyzer",
        use_container_width=True,
        disabled=True
    )


with n3:

    if st.button(
        "Recycling Guide",
        key="nav_recycling",
        use_container_width=True
    ):
        st.switch_page("pages/recycling.py")


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
# HEADER
# =========================================================

st.html("""
<div class="page-header">

    <div class="badge">
        INTELLIGENT E-WASTE ANALYSIS
    </div>

    <div class="title">
        E-Waste Analyzer
    </div>

    <div class="subtitle">
        Upload an electronic waste image and let the AI
        identify the device and provide relevant recycling guidance.
    </div>

</div>
""")


# =========================================================
# UPLOAD SECTION
# =========================================================

st.html("""
<div class="upload-section">

    <div class="upload-label">
        IMAGE INPUT
    </div>

    <div class="upload-title">
        Upload E-Waste Image
    </div>

    <div class="upload-description">
        Select a clear image of an electronic item.
        Supported formats are JPG, JPEG, PNG and WEBP.
    </div>

</div>
""")


uploaded_file = st.file_uploader(
    "Upload your e-waste image",
    type=["jpg", "jpeg", "png", "webp"],
    label_visibility="visible"
)


# =========================================================
# NO IMAGE
# =========================================================

if uploaded_file is None:

    st.session_state.analysis_started = False

    st.session_state.detected_device = ""
    st.session_state.device_category = ""
    st.session_state.device_description = ""
    st.session_state.recycling_guidance = []


    st.html("""
    <div class="info-area">

        <div style="
            display:grid;
            grid-template-columns:repeat(3,1fr);
            gap:12px;
        ">

            <div class="info-card">
                <div class="info-label">SUPPORTED</div>
                <div class="info-value">JPG · PNG · WEBP</div>
            </div>

            <div class="info-card">
                <div class="info-label">INPUT</div>
                <div class="info-value">E-Waste Image</div>
            </div>

            <div class="info-card">
                <div class="info-label">PROCESS</div>
                <div class="info-value">AI Classification</div>
            </div>

        </div>

    </div>

    <div class="bottom">
        Upload an image to start the classification process.
    </div>
    """)


# =========================================================
# IMAGE UPLOADED
# =========================================================

else:

    st.html("""
    <div class="preview">

        <div class="upload-label">
            IMAGE PREVIEW
        </div>

    </div>
    """)


    st.image(
        uploaded_file,
        width=500
    )


    st.html("""
    <div class="info-area">

        <div style="
            display:grid;
            grid-template-columns:repeat(3,1fr);
            gap:12px;
        ">

            <div class="info-card">
                <div class="info-label">FILE STATUS</div>
                <div class="info-value">Ready</div>
            </div>

            <div class="info-card">
                <div class="info-label">FILE TYPE</div>
                <div class="info-value">Image</div>
            </div>

            <div class="info-card">
                <div class="info-label">AI STATUS</div>
                <div class="info-value">Ready For Analysis</div>
            </div>

        </div>

    </div>
    """)


    # =====================================================
    # ANALYZE BUTTON
    # =====================================================

    st.html('<div class="analyze-area">')

    analyze_clicked = st.button(
        "Analyze Image",
        key="analyze_image",
        use_container_width=True
    )

    st.html('</div>')


    if analyze_clicked:

        if client is None:

            st.warning(
                "AI service is not configured. "
                "Please check your .env file."
            )

        else:

            with st.spinner(
                "AI is identifying the device and preparing recycling guidance..."
            ):

                image_bytes = uploaded_file.getvalue()

                mime_type = uploaded_file.type

                result = analyze_image(
                    image_bytes,
                    mime_type
                )


            if result:

                st.session_state.detected_device = result["device"]

                st.session_state.device_category = result["category"]

                st.session_state.device_description = result["description"]

                st.session_state.recycling_guidance = result[
                    "recycling_guidance"
                ]

                st.session_state.analysis_started = True

                st.rerun()


    # =====================================================
    # RESULT
    # =====================================================

    if st.session_state.analysis_started:

        device = html.escape(
            st.session_state.detected_device
        )

        category = html.escape(
            st.session_state.device_category
        )

        description = html.escape(
            st.session_state.device_description
        )


        guidance_html = ""

        for item in st.session_state.recycling_guidance:

            safe_item = html.escape(str(item))

            guidance_html += f"""
            <div class="guidance-item">
                {safe_item}
            </div>
            """


        st.html(f"""
        <div class="result">

            <div class="result-title">
                Classification Analysis
            </div>

            <div class="result-text">
                The AI analyzed the uploaded image and identified
                the electronic device shown below.
            </div>


            <div class="result-value">

                <div class="result-label">
                    DETECTED DEVICE
                </div>

                <div class="result-main">
                    {device}
                </div>

            </div>


            <div class="result-value">

                <div class="result-label">
                    CATEGORY
                </div>

                <div class="result-main">
                    {category}
                </div>

            </div>


            <div class="result-value">

                <div class="result-label">
                    DESCRIPTION
                </div>

                <div class="result-text">
                    {description}
                </div>

            </div>


            <div class="guidance">

                <div class="guidance-title">
                    DEVICE-SPECIFIC RECYCLING GUIDANCE
                </div>

                {guidance_html}

            </div>

        </div>
        """)


        # =================================================
        # CONTINUE TO RECYCLING GUIDE
        # =================================================

        st.html("""
        <div style="
            position:relative;
            z-index:20;
            text-align:center;
            color:#789c99;
            font-size:11px;
            letter-spacing:1.5px;
            margin-top:24px;
            margin-bottom:10px;
        ">
            CONTINUE PROCESS
        </div>
        """)


        st.html('<div class="continue-box">')

        if st.button(
            "Continue to Recycling Guide  →",
            key="continue_recycling",
            use_container_width=True
        ):

            st.switch_page(
                "pages/recycling.py"
            )

        st.html('</div>')


        st.html("""
        <div class="bottom">
            The Recycling Guide will use the device identified by AI
            to provide relevant handling and recycling information.
        </div>
        """)