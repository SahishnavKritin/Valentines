import streamlit as st
import base64
import random

st.set_page_config(page_title="For You ❤️", layout="centered")

# ---------- FILE TO BASE64 ----------
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ---------- SESSION STATE ----------
if "stage" not in st.session_state:
    st.session_state.stage = "landing"

# ======================================================
# LANDING PAGE (CLEAN PAGE)
# ======================================================
if st.session_state.stage == "landing":

    st.markdown("<div style='text-align:center; margin-top:300px;'>", unsafe_allow_html=True)

    if st.button("Click Here Popoy 💌"):
        st.session_state.stage = "main"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# LOAD ASSETS FOR MAIN APP
# ======================================================
else:

    bg_img = get_base64("background.jpg")
    bg_music = get_base64("background_music.mp3")
    yay_sound = get_base64("yay_sound.mp3")

    # ---------- BACKGROUND STYLE ----------
    page_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_img}");
        background-size: cover;
        background-position: center;
    }}

    .centered {{
        text-align: center;
        color: white;
    }}

    .big-text {{
        font-size: 55px;
        font-weight: bold;
        animation: glow 2s ease-in-out infinite alternate;
    }}

    @keyframes glow {{
        from {{ text-shadow: 0 0 10px pink; }}
        to {{ text-shadow: 0 0 25px red; }}
    }}

    .heart {{
        position: absolute;
        color: pink;
        font-size: 25px;
        animation: float 6s infinite;
    }}

    @keyframes float {{
        0% {{transform: translateY(100vh); opacity: 0;}}
        50% {{opacity: 1;}}
        100% {{transform: translateY(-10vh); opacity: 0;}}
    }}
    </style>
    """
    st.markdown(page_style, unsafe_allow_html=True)

    # ---------- BACKGROUND MUSIC (starts immediately) ----------
    st.markdown(
        f"""
        <audio autoplay loop>
            <source src="data:audio/mp3;base64,{bg_music}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

    # ---------- FLOATING HEARTS ----------
    heart_html = ""
    for _ in range(15):
        left = random.randint(0, 100)
        delay = random.uniform(0, 5)
        heart_html += f"<div class='heart' style='left:{left}%; animation-delay:{delay}s;'>❤️</div>"
    st.markdown(heart_html, unsafe_allow_html=True)

    st.markdown("<div class='centered'>", unsafe_allow_html=True)

    # ======================================================
    # MAIN QUESTION
    # ======================================================
    if st.session_state.stage == "main":

        st.markdown("<div style='margin-top:200px;'>", unsafe_allow_html=True)
        st.markdown("<div class='big-text'>Will you be my Valentine? 💘</div>", unsafe_allow_html=True)
        st.write("")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Yes ❤️"):
                st.session_state.stage = "yes"
                st.rerun()

        with col2:
            if st.button("No 🙈"):
                st.session_state.stage = "confirm"
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # ======================================================
    # ARE YOU SURE
    # ======================================================
    elif st.session_state.stage == "confirm":

        st.markdown("<div style='margin-top:200px;'>", unsafe_allow_html=True)
        st.markdown("## Are you sure? 🥺")

        if st.button("No, I was out of my goddamn mind."):
            st.session_state.stage = "final_confirm"
            st.rerun()

        if st.button("Of course no, I'm so sorry Babycorn."):
            st.session_state.stage = "final_confirm"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # ======================================================
    # SO THAT'S A YES?
    # ======================================================
    elif st.session_state.stage == "final_confirm":

        st.markdown("<div style='margin-top:200px;'>", unsafe_allow_html=True)
        st.markdown("## So that's a yes? 😏")

        if st.button("Yes ❤️"):
            st.session_state.stage = "yes"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # ======================================================
    # YES SCREEN
    # ======================================================
    elif st.session_state.stage == "yes":

        # Play YAY sound once
        st.markdown(
            f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{yay_sound}" type="audio/mp3">
            </audio>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

        st.markdown("<div style='margin-top:200px;'>", unsafe_allow_html=True)
        st.markdown("<div class='big-text'>I KNEW IT ❤️</div>", unsafe_allow_html=True)
        st.markdown("### See you tomorrow at IGNNA by Midnight Sun, Nungambakkam.")
        st.markdown("### I'll pick you up at 7PM 😌")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
