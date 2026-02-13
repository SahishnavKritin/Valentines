import streamlit as st
import base64
import random

st.set_page_config(page_title="For You ❤️", layout="centered")

# Convert image to base64
def get_base64(img_file):
    with open(img_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load background image
bg_img = get_base64("background.jpg")

page_bg_img = f"""
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{bg_img}");
    background-size: cover;
    background-position: center;
}}

.overlay {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.4);
}}

.centered {{
    text-align: center;
    color: white;
}} 

.big-text {{
    font-size: 50px;
    font-weight: bold;
    margin-top: 100px;
}}

.hearts {{
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
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

st.markdown(page_bg_img, unsafe_allow_html=True)

# Floating hearts
heart_html = "<div class='hearts'>"
for i in range(15):
    left = random.randint(0, 100)
    delay = random.uniform(0, 5)
    heart_html += f"<div class='heart' style='left:{left}%; animation-delay:{delay}s;'>❤️</div>"
heart_html += "</div>"

st.markdown(heart_html, unsafe_allow_html=True)

# Session control
if "stage" not in st.session_state:
    st.session_state.stage = "main"

st.markdown("<div class='centered'>", unsafe_allow_html=True)

# MAIN QUESTION
st.markdown("<div class='centered'>", unsafe_allow_html=True)

# MAIN QUESTION
st.markdown("<div class='centered'>", unsafe_allow_html=True)

# MAIN QUESTION
if st.session_state.stage == "main":

    # Push question lower
    st.markdown("<div style='margin-top:200px;'>", unsafe_allow_html=True)

    st.markdown("<div class='big-text'>Will you be my Valentine? 💘</div>", unsafe_allow_html=True)
    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes ❤️"):
            st.session_state.stage = "yes"

    with col2:
        if st.button("No 🙈"):
            st.session_state.stage = "confirm"

    st.markdown("</div>", unsafe_allow_html=True)


# CONFIRMATION FLOW (Appears Below)
elif st.session_state.stage == "confirm":

    st.markdown("<div style='margin-top:200px;'>", unsafe_allow_html=True)

    st.markdown("<div class='big-text'>Will you be my Valentine? 💘</div>", unsafe_allow_html=True)
    st.write("")
    st.button("Yes ❤️", key="yes_again", on_click=lambda: st.session_state.update(stage="yes"))

    st.write("")
    st.markdown("### Are you sure? 🥺")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("No, I was out of my goddamn mind."):
            st.session_state.stage = "yes"

    with col2:
        if st.button("Of course no, I'm so sorry Babycorn."):
            st.markdown("### So that's a yes? 😏")

            if st.button("Yes"):
                st.session_state.stage = "yes"

    st.markdown("</div>", unsafe_allow_html=True)


# YES SCREEN
elif st.session_state.stage == "yes":
    st.balloons()
    st.markdown("<div style='margin-top:200px;'>", unsafe_allow_html=True)
    st.markdown("<div class='big-text'>I KNEW IT ❤️</div>", unsafe_allow_html=True)
    st.markdown("### Best decision ever, Babycorn 😌")
    st.markdown("</div>", unsafe_allow_html=True)