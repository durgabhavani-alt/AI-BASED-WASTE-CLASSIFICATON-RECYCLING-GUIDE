import streamlit as st

st.set_page_config(
    page_title="E-Waste Intelligence",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if st.session_state.logged_in:

    pg = st.navigation(
        [
            st.Page(
                "pages/home.py",
                title="Home"
            ),

            st.Page(
                "pages/analyzer.py",
                title="Analyzer"
            ),

            st.Page(
                "pages/recycling.py",
                title="Recycling Guide"
            ),

            st.Page(
                "pages/about.py",
                title="About"
            ),

            st.Page(
                "pages/profile.py",
                title="Profile"
            ),
        ],
        position="hidden"
    )

else:

    pg = st.navigation(
        [
            st.Page(
                "pages/login.py",
                title="Login"
            )
        ],
        position="hidden"
    )

pg.run()