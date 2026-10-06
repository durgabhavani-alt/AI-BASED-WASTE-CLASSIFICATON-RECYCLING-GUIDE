import streamlit as st
import re
import random

st.set_page_config(
    page_title="E-Waste Intelligence",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# SESSION
# =========================================================

if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = "Sign In"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# =========================================================
# PARTICLES
# =========================================================

random.seed(25)

particles = ""

for _ in range(45):

    left = random.randint(2, 98)
    top = random.randint(2, 98)
    size = random.choice([2, 3, 4, 5])
    delay = round(random.uniform(0, 5), 2)
    duration = round(random.uniform(3, 6), 2)

    particles += f"""
    <span class="particle"
        style="
        left:{left}%;
        top:{top}%;
        width:{size}px;
        height:{size}px;
        animation-delay:{delay}s;
        animation-duration:{duration}s;
        ">
    </span>
    """


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
<style>

/* PAGE */

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(
            circle at 15% 30%,
            rgba(35, 220, 180, .13),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 25%,
            rgba(30, 210, 175, .10),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #001916 0%,
            #002a25 50%,
            #001310 100%
        );

    overflow-x: hidden;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1400px;
    padding-top: 0.8rem;
}


/* REMOVE STREAMLIT DEFAULT */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* TOP BRAND */

.top-brand {
    position: relative;
    z-index: 20;

    margin: 5px 0 0 15px;

    color: #dffff8;

    font-size: 18px;
    font-weight: 700;

    letter-spacing: .4px;
}


/* HERO */

.hero {
    position: relative;

    height: 690px;

    overflow: hidden;

    border-radius: 25px;
}


/* PARTICLES */

.particle {
    position: absolute;

    display: block;

    border-radius: 50%;

    background: #45e7bd;

    box-shadow:
        0 0 6px #45e7bd,
        0 0 16px rgba(69,231,189,.8),
        0 0 30px rgba(69,231,189,.3);

    opacity: .35;

    animation: particleMove ease-in-out infinite;
}

@keyframes particleMove {

    0%,100% {
        transform:
            translate3d(0,0,0)
            scale(.7);

        opacity: .2;
    }

    50% {
        transform:
            translate3d(0,-22px,15px)
            scale(1.4);

        opacity: 1;
    }
}


/* GLOW */

.glow-one {
    position: absolute;

    width: 520px;
    height: 520px;

    right: 3%;
    top: 70px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(45,230,190,.18),
            transparent 68%
        );

    filter: blur(5px);
}


/* GLOW RINGS */

.ring-one {
    position: absolute;

    width: 430px;
    height: 430px;

    right: 10%;
    top: 105px;

    border:
        1px solid
        rgba(67,229,190,.15);

    border-radius: 50%;

    transform:
        rotateX(65deg)
        rotateZ(-15deg);

    box-shadow:
        0 0 40px rgba(50,225,185,.08);

    animation: ringMove 8s linear infinite;
}

.ring-two {
    position: absolute;

    width: 300px;
    height: 300px;

    right: 18%;
    top: 170px;

    border:
        1px solid
        rgba(67,229,190,.10);

    border-radius: 50%;

    transform:
        rotateX(65deg)
        rotateZ(25deg);

    animation:
        ringMove 10s linear infinite reverse;
}

@keyframes ringMove {

    from {
        transform:
            rotateX(65deg)
            rotateZ(0deg);
    }

    to {
        transform:
            rotateX(65deg)
            rotateZ(360deg);
    }
}


/* CIRCUIT LINES */

.line {
    position: absolute;

    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(65,230,190,.5),
            transparent
        );

    box-shadow:
        0 0 12px rgba(65,230,190,.35);
}

.line-one {
    width: 430px;
    right: 0;
    top: 105px;

    transform: rotate(-16deg);
}

.line-two {
    width: 350px;
    right: 8%;
    bottom: 130px;

    transform: rotate(14deg);
}

.line-three {
    width: 240px;
    right: 36%;
    top: 470px;

    transform: rotate(-7deg);
}


/* HERO TEXT */

.hero-content {
    position: absolute;

    left: 55px;
    top: 125px;

    width: 60%;

    z-index: 10;
}


/* 3D TITLE */

.main-title {
    margin: 0;

    font-size: clamp(58px, 7vw, 100px);

    line-height: .86;

    font-weight: 950;

    letter-spacing: -6px;

    color: #f1fffc;

    text-shadow:
        0 2px 0 #0b6155,
        0 5px 0 #07483f,
        0 9px 0 #04362f,
        0 18px 30px rgba(0,0,0,.6),
        0 0 35px rgba(60,230,190,.16);
}

.main-title span {
    color: #43e5bb;

    text-shadow:
        0 2px 0 #087565,
        0 5px 0 #075346,
        0 9px 0 #043a31,
        0 18px 30px rgba(0,0,0,.6),
        0 0 40px rgba(60,230,190,.25);
}


/* TAGLINE */

.tagline {
    margin-top: 32px;

    color: #ecfffb;

    font-size: 30px;

    line-height: 1.15;

    font-weight: 800;
}

.tagline span {
    color: #42dfb8;
}


/* DESCRIPTION */

.description {
    margin-top: 20px;

    max-width: 500px;

    color: #91bdb5;

    font-size: 15px;

    line-height: 1.7;
}


/* SMALL TECH DETAILS */

.tech-label {
    margin-top: 35px;

    color: #4fe1bd;

    font-size: 12px;

    letter-spacing: 3px;

    text-transform: uppercase;

    opacity: .8;
}


/* LOGIN CARD */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,.09),
            rgba(255,255,255,.025)
        ) !important;

    border:
        1px solid
        rgba(82,224,197,.30) !important;

    border-radius: 27px !important;

    box-shadow:
        0 30px 80px rgba(0,0,0,.42),
        inset 0 1px 0 rgba(255,255,255,.08) !important;

    backdrop-filter: blur(22px);

    padding: 30px !important;
}


/* LOGIN TITLE */

.login-title {
    color: #effffb;

    font-size: 32px;

    font-weight: 850;

    margin-bottom: 7px;
}

.login-subtitle {
    color: #8dbab3;

    font-size: 14px;

    line-height: 1.55;

    margin-bottom: 20px;
}


/* LABEL */

label {
    color: #9fc8c0 !important;

    font-size: 13px !important;
}


/* INPUT */

div[data-baseweb="input"] {
    background: #ffffff !important;

    border:
        1px solid
        rgba(65,210,185,.35) !important;

    border-radius: 11px !important;
}


/* INPUT TEXT */

div[data-baseweb="input"] input {
    color: #000000 !important;

    background: transparent !important;

    caret-color: #000000 !important;

    font-weight: 500 !important;
}

div[data-baseweb="input"] input::placeholder {
    color: #777777 !important;
}


/* INPUT FOCUS */

div[data-baseweb="input"]:focus-within {
    border-color: #37dcb7 !important;

    box-shadow:
        0 0 0 2px
        rgba(55,220,183,.16) !important;
}


/* ALL BUTTONS */

div.stButton > button {
    border-radius: 10px !important;

    min-height: 43px !important;

    font-weight: 700 !important;
}


/* SWITCH BUTTONS */

div.stButton > button {
    background: rgba(12,55,50,.75) !important;

    color: #b9ddd7 !important;

    border:
        1px solid
        rgba(82,224,197,.20) !important;
}

div.stButton > button:hover {
    background: rgba(30,91,82,.90) !important;

    color: #ffffff !important;

    border-color: #48dabb !important;
}


/* AUTH BUTTON */

.auth-button + div button {
    width: 100% !important;

    height: 51px !important;

    border-radius: 12px !important;

    border: none !important;

    background:
        linear-gradient(
            100deg,
            #29c8a5,
            #49dfbc
        ) !important;

    color: #00261f !important;

    font-size: 15px !important;

    font-weight: 800 !important;

    box-shadow:
        0 12px 30px
        rgba(42,213,175,.18) !important;

    transition: .25s ease !important;
}

.auth-button + div button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 17px 35px
        rgba(42,213,175,.32) !important;
}


/* FOOTER */

.secure {
    text-align: center;

    color: #537d76;

    font-size: 11px;

    margin-top: 20px;
}


/* MOBILE */

@media (max-width: 900px) {

    .hero {
        height: auto;
        min-height: 580px;
    }

    .hero-content {
        left: 25px;
        top: 80px;
        width: 90%;
    }

    .main-title {
        font-size: 58px;
    }

    .tagline {
        font-size: 24px;
    }

}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# BRAND
# =========================================================

st.markdown(
    '<div class="top-brand">E-Waste Intelligence</div>',
    unsafe_allow_html=True
)


# =========================================================
# LAYOUT
# =========================================================

left, right = st.columns(
    [1.55, .72],
    gap="large"
)


# =========================================================
# LEFT SIDE
# =========================================================

with left:

    st.html(
        f"""
        <div class="hero">

            <div class="glow-one"></div>

            <div class="ring-one"></div>

            <div class="ring-two"></div>

            <div class="line line-one"></div>

            <div class="line line-two"></div>

            <div class="line line-three"></div>

            {particles}

            <div class="hero-content">

                <div class="main-title">
                    E-Waste<br>
                    <span>Intelligence</span>
                </div>

                <div class="tagline">
                    Smarter Classification.<br>
                    <span>Greener Tomorrow.</span>
                </div>

                <div class="description">
                    Identify electronic waste intelligently and
                    discover responsible recycling guidance —
                    helping turn e-waste into a better future.
                </div>

                <div class="tech-label">
                    Intelligent • Sustainable • Responsible
                </div>

            </div>

        </div>
        """
    )


# =========================================================
# RIGHT SIDE — LOGIN
# =========================================================

with right:

    with st.container(border=True):

        if st.session_state.auth_mode == "Sign In":
            title = "Welcome Back"
            subtitle = "Sign in to continue to E-Waste Intelligence."
        else:
            title = "Create Account"
            subtitle = "Create your account to get started."

        st.markdown(
            f"""
            <div class="login-title">
                {title}
            </div>

            <div class="login-subtitle">
                {subtitle}
            </div>
            """,
            unsafe_allow_html=True
        )


        # =================================================
        # SWITCH
        # =================================================

        c1, c2 = st.columns(2)

        with c1:

            if st.button(
                "Sign In",
                key="switch_signin",
                use_container_width=True
            ):

                st.session_state.auth_mode = "Sign In"
                st.rerun()


        with c2:

            if st.button(
                "Create Account",
                key="switch_create",
                use_container_width=True
            ):

                st.session_state.auth_mode = "Create Account"
                st.rerun()


        st.write("")


        # =================================================
        # SIGN IN
        # =================================================

        if st.session_state.auth_mode == "Sign In":

            email = st.text_input(
                "Email address",
                placeholder="Enter your email",
                key="signin_email"
            )

            password = st.text_input(
                "Password",
                placeholder="Enter your password",
                type="password",
                key="signin_password"
            )

            st.write("")

            st.markdown(
                '<div class="auth-button">',
                unsafe_allow_html=True
            )

            login = st.button(
                "Sign In  →",
                key="signin_button",
                use_container_width=True
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


            if login:

                if not email.strip():

                    st.error(
                        "Please enter your email."
                    )

                elif not re.match(
                    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
                    email.strip()
                ):

                    st.error(
                        "Please enter a valid email address."
                    )

                elif not password:

                    st.error(
                        "Please enter your password."
                    )

                elif len(password) < 6:

                    st.error(
                        "Password must contain at least 6 characters."
                    )

                else:

                    # LOGIN SUCCESS
                    st.session_state.logged_in = True

                    st.rerun()


        # =================================================
        # CREATE ACCOUNT
        # =================================================

        else:

            name = st.text_input(
                "Full name",
                placeholder="Enter your full name",
                key="create_name"
            )

            email = st.text_input(
                "Email address",
                placeholder="Enter your email",
                key="create_email"
            )

            password = st.text_input(
                "Create password",
                placeholder="Minimum 6 characters",
                type="password",
                key="create_password"
            )

            confirm = st.text_input(
                "Confirm password",
                placeholder="Re-enter your password",
                type="password",
                key="create_confirm"
            )

            st.write("")

            st.markdown(
                '<div class="auth-button">',
                unsafe_allow_html=True
            )

            create = st.button(
                "Create Account  →",
                key="create_account_button",
                use_container_width=True
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


            if create:

                if not name.strip():

                    st.error(
                        "Please enter your name."
                    )

                elif not email.strip():

                    st.error(
                        "Please enter your email."
                    )

                elif not re.match(
                    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
                    email.strip()
                ):

                    st.error(
                        "Please enter a valid email address."
                    )

                elif not password:

                    st.error(
                        "Please create a password."
                    )

                elif len(password) < 6:

                    st.error(
                        "Password must contain at least 6 characters."
                    )

                elif password != confirm:

                    st.error(
                        "Passwords do not match."
                    )

                else:

                    st.session_state.create_name = name.strip()
                    st.session_state.create_email = email.strip()

                    # ACCOUNT CREATED + LOGIN
                    st.session_state.logged_in = True

                    st.rerun()


        # =================================================
        # FOOTER
        # =================================================

        st.markdown(
            """
            <div class="secure">
                Secure access · E-Waste Intelligence Platform
            </div>
            """,
            unsafe_allow_html=True
        )