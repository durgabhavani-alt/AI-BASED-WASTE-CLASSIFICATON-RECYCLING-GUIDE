import streamlit as st
import random
import html

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Profile | E-Waste Intelligence",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "logged_in": False,
    "create_name": "",
    "create_email": "",
    "create_username": "",
    "create_password": "",
    "profile_name": "",
    "profile_email": "",
    "profile_username": "",
    "profile_password": "",
    "profile_role": "E-Waste Intelligence User",
    "notifications": True,
    "auto_save": True,
    "profile_edit": False,
    "settings_open": False,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# =========================================================
# LOAD USER DETAILS
# =========================================================

if not st.session_state.profile_name:
    st.session_state.profile_name = (
        st.session_state.create_name.strip()
        if st.session_state.create_name
        else "E-Waste User"
    )

if not st.session_state.profile_email:
    st.session_state.profile_email = (
        st.session_state.create_email.strip()
        if st.session_state.create_email
        else "user@example.com"
    )

if not st.session_state.profile_username:
    st.session_state.profile_username = (
        st.session_state.create_username.strip()
        if st.session_state.create_username
        else "ewaste_user"
    )

if not st.session_state.profile_password:
    st.session_state.profile_password = (
        st.session_state.create_password
        if st.session_state.create_password
        else ""
    )

# =========================================================
# SAFE DISPLAY VALUES
# =========================================================

user_name = html.escape(st.session_state.profile_name)
user_email = html.escape(st.session_state.profile_email)
username = html.escape(st.session_state.profile_username)

# Password is NEVER displayed as plain text
password_display = "••••••••"

# =========================================================
# MOVING PARTICLES
# =========================================================

random.seed(35)

particles = ""

for _ in range(20):

    left = random.randint(2, 98)
    top = random.randint(5, 95)
    size = random.randint(2, 4)
    duration = random.randint(12, 22)
    delay = random.randint(0, 12)

    particles += f"""
        <span class="particle"
              style="
                left:{left}%;
                top:{top}%;
                width:{size}px;
                height:{size}px;
                animation-duration:{duration}s;
                animation-delay:-{delay}s;
              ">
        </span>
    """

# =========================================================
# CSS
# =========================================================

st.html(
    f"""
    <style>

    /* =========================================
       PAGE
       ========================================= */

    .stApp {{
        background:
            radial-gradient(
                circle at 50% 40%,
                rgba(20, 184, 166, 0.055),
                transparent 34%
            ),
            #061416;
    }}

    .block-container {{
        max-width: 1400px !important;
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
    }}

    section[data-testid="stSidebar"] {{
        display: none;
    }}

    /* =========================================
       PARTICLES
       ========================================= */

    .particle {{
        position: fixed;
        border-radius: 50%;
        display: block;

        background: rgba(45, 212, 191, 0.30);

        box-shadow:
            0 0 8px rgba(45, 212, 191, 0.16);

        pointer-events: none;
        z-index: 0;

        animation-name: moveParticle;
        animation-timing-function: linear;
        animation-iteration-count: infinite;
    }}

    @keyframes moveParticle {{

        0% {{
            transform: translate3d(0, 25px, 0);
            opacity: 0;
        }}

        20% {{
            opacity: 0.45;
        }}

        50% {{
            transform: translate3d(28px, -35px, 0);
            opacity: 0.25;
        }}

        80% {{
            opacity: 0.40;
        }}

        100% {{
            transform: translate3d(-20px, -90px, 0);
            opacity: 0;
        }}

    }}

    /* =========================================
       NAVIGATION
       ========================================= */

    div[data-testid="stHorizontalBlock"] {{
        align-items: center;
    }}

    div[data-testid="stButton"] > button {{
        background: transparent !important;
        color: #829c9c !important;

        border: 1px solid transparent !important;
        border-radius: 7px !important;

        font-size: 13px !important;
        font-weight: 500 !important;

        min-height: 38px !important;

        box-shadow: none !important;

        transition: all 0.2s ease !important;
    }}

    div[data-testid="stButton"] > button:hover {{
        color: #d9ffff !important;
        background: rgba(45, 212, 191, 0.055) !important;
    }}

    div[data-testid="stButton"] > button:disabled {{
        color: #50dfca !important;

        background:
            rgba(45, 212, 191, 0.09) !important;

        border:
            1px solid rgba(45, 212, 191, 0.15) !important;

        opacity: 1 !important;
    }}

    /* =========================================
       CENTER AREA
       ========================================= */

    .profile-wrapper {{
        min-height: 70vh;

        display: flex;
        justify-content: center;
        align-items: center;

        position: relative;
        z-index: 2;
    }}

    /* =========================================
       STRAIGHT RECTANGLE CARD
       ========================================= */

    .profile-card {{
        width: 520px;

        padding: 34px 38px;

        background:
            rgba(8, 26, 28, 0.97);

        border:
            1px solid rgba(78, 211, 194, 0.18);

        border-radius: 4px;

        box-shadow:
            0 28px 80px rgba(0, 0, 0, 0.45);

        position: relative;
    }}

    /* =========================================
       PROFILE LOGO
       ========================================= */

    .profile-logo {{
        width: 72px;
        height: 72px;

        margin: 0 auto 18px auto;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 50%;

        background:
            linear-gradient(
                145deg,
                #123d3d,
                #0b292b
            );

        border:
            1px solid rgba(78, 211, 194, 0.35);

        color: #5be0ce;

        font-size: 28px;
        font-weight: 600;

        box-shadow:
            0 0 30px rgba(45, 212, 191, 0.08);
    }}

    .profile-heading {{
        text-align: center;

        color: #efffff;

        font-size: 25px;
        font-weight: 600;

        margin-bottom: 5px;
    }}

    .profile-caption {{
        text-align: center;

        color: #6f8b8b;

        font-size: 12px;

        margin-bottom: 28px;
    }}

    /* =========================================
       INFORMATION ROWS
       ========================================= */

    .info-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;

        min-height: 48px;

        border-bottom:
            1px solid rgba(130, 180, 178, 0.08);
    }}

    .info-label {{
        color: #6d8989;

        font-size: 10px;

        letter-spacing: 1.2px;

        text-transform: uppercase;
    }}

    .info-value {{
        color: #d8eeee;

        font-size: 13px;

        text-align: right;

        max-width: 65%;

        word-break: break-word;
    }}

    .role-value {{
        color: #63ddcc;
    }}

    .status-value {{
        color: #54dfca;
        font-weight: 600;
    }}

    /* =========================================
       ACTION BUTTONS
       ========================================= */

    .action-title {{
        color: #9bb5b4;

        font-size: 11px;

        letter-spacing: 1px;

        text-transform: uppercase;

        margin-top: 24px;
        margin-bottom: 10px;
    }}

    /* =========================================
       FOOTER
       ========================================= */

    .profile-footer {{
        position: fixed;

        bottom: 12px;
        left: 0;

        width: 100%;

        text-align: center;

        color: #3e5859;

        font-size: 10px;

        z-index: 2;
    }}

    /* =========================================
       MOBILE
       ========================================= */

    @media (max-width: 700px) {{

        .profile-card {{
            width: 90vw;
            padding: 28px 24px;
        }}

        .info-row {{
            gap: 15px;
        }}

        .info-value {{
            max-width: 60%;
        }}

    }}

    </style>

    {particles}
    """
)

# =========================================================
# NAVIGATION
# =========================================================

nav1, nav2, nav3, nav4, nav5 = st.columns(
    [1, 1, 1, 1, 1],
    gap="small"
)

with nav1:
    if st.button("Home", use_container_width=True):
        st.switch_page("pages/home.py")

with nav2:
    if st.button("Analyzer", use_container_width=True):
        st.switch_page("pages/analyzer.py")

with nav3:
    if st.button("Recycling Guide", use_container_width=True):
        st.switch_page("pages/recycling.py")

with nav4:
    if st.button("About", use_container_width=True):
        st.switch_page("pages/about.py")

with nav5:
    st.button(
        "Profile",
        use_container_width=True,
        disabled=True
    )

# =========================================================
# PROFILE CARD
# =========================================================

st.html(
    f"""
    <div class="profile-wrapper">

        <div class="profile-card">

            <div class="profile-logo">
                {user_name[0].upper()}
            </div>

            <div class="profile-heading">
                {user_name}
            </div>

            <div class="profile-caption">
                E-Waste Intelligence Account
            </div>

            <div class="info-row">
                <span class="info-label">
                    Username
                </span>

                <span class="info-value">
                    @{username}
                </span>
            </div>

            <div class="info-row">
                <span class="info-label">
                    Full Name
                </span>

                <span class="info-value">
                    {user_name}
                </span>
            </div>

            <div class="info-row">
                <span class="info-label">
                    Email
                </span>

                <span class="info-value">
                    {user_email}
                </span>
            </div>

            <div class="info-row">
                <span class="info-label">
                    Password
                </span>

                <span class="info-value">
                    {password_display}
                </span>
            </div>

            <div class="info-row">
                <span class="info-label">
                    Project Role
                </span>

                <span class="info-value role-value">
                    E-Waste Intelligence User
                </span>
            </div>

            <div class="info-row">
                <span class="info-label">
                    Account Status
                </span>

                <span class="info-value status-value">
                    Active
                </span>
            </div>

        </div>

    </div>
    """
)

# =========================================================
# ACTION BUTTONS
# =========================================================

st.markdown(
    '<div class="action-title">Account Settings</div>',
    unsafe_allow_html=True
)

edit_col, settings_col, signout_col = st.columns(
    [1, 1, 1]
)

# =========================================================
# EDIT PROFILE
# =========================================================

with edit_col:

    if st.button(
        "Edit Profile",
        use_container_width=True
    ):
        st.session_state.profile_edit = (
            not st.session_state.profile_edit
        )

# =========================================================
# SETTINGS
# =========================================================

with settings_col:

    if st.button(
        "Settings",
        use_container_width=True
    ):
        st.session_state.settings_open = (
            not st.session_state.settings_open
        )

# =========================================================
# SIGN OUT
# =========================================================

with signout_col:

    if st.button(
        "Sign Out",
        use_container_width=True
    ):
        st.session_state.logged_in = False
        st.rerun()

# =========================================================
# EDIT PROFILE PANEL
# =========================================================

if st.session_state.profile_edit:

    st.markdown(
        "### Edit Profile"
    )

    edit_name = st.text_input(
        "Full Name",
        value=st.session_state.profile_name
    )

    edit_username = st.text_input(
        "Username",
        value=st.session_state.profile_username
    )

    edit_email = st.text_input(
        "Email",
        value=st.session_state.profile_email
    )

    edit_password = st.text_input(
        "Password",
        value=st.session_state.profile_password,
        type="password"
    )

    save_col, cancel_col = st.columns(2)

    with save_col:

        if st.button(
            "Save Changes",
            use_container_width=True
        ):

            if (
                edit_name.strip()
                and edit_username.strip()
                and edit_email.strip()
            ):

                st.session_state.profile_name = (
                    edit_name.strip()
                )

                st.session_state.profile_username = (
                    edit_username.strip()
                )

                st.session_state.profile_email = (
                    edit_email.strip()
                )

                st.session_state.profile_password = (
                    edit_password
                )

                st.session_state.create_name = (
                    edit_name.strip()
                )

                st.session_state.create_username = (
                    edit_username.strip()
                )

                st.session_state.create_email = (
                    edit_email.strip()
                )

                st.session_state.create_password = (
                    edit_password
                )

                st.session_state.profile_edit = False

                st.success(
                    "Profile updated successfully."
                )

                st.rerun()

            else:

                st.error(
                    "Name, username and email are required."
                )

    with cancel_col:

        if st.button(
            "Cancel",
            use_container_width=True
        ):
            st.session_state.profile_edit = False
            st.rerun()

# =========================================================
# SETTINGS PANEL
# =========================================================

if st.session_state.settings_open:

    st.markdown(
        "### Settings"
    )

    st.session_state.notifications = st.toggle(
        "Notifications",
        value=st.session_state.notifications
    )

    st.session_state.auto_save = st.toggle(
        "Auto-save analysis",
        value=st.session_state.auto_save
    )

    if st.session_state.notifications:
        st.caption("Notifications are enabled.")
    else:
        st.caption("Notifications are disabled.")

    if st.session_state.auto_save:
        st.caption("Latest analysis is kept during the session.")
    else:
        st.caption("Automatic analysis saving is disabled.")

# =========================================================
# FOOTER
# =========================================================

st.html(
    """
    <div class="profile-footer">
        E-Waste Intelligence · Responsible Technology
    </div>
    """
)