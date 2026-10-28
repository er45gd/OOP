import streamlit as st
from PIL import Image
#create resume

col1, col2, = st.columns((4, 5))

with col1:
    st.title("Ethan Huddleston")
    st.header("Student, Game design")

with col2:
    st.markdown("***About Me:***")
    st.text("Freshman")
    st.text("I'm learning OOP in Fall 2026.")
    st.divider()

st.markdown("***Qualifications:***")
st.text("High School diploma")
st.divider()

st.markdown("***Work Experience:***")
st.text("Whataburger employee, 2025-now")
st.text("Work study janitorial, John Brown University 2026-2027")
st.divider()

st.markdown("***Projects:***")
st.text("Vending Machine Simulation")
st.divider()

st.markdown("***Contact me:***")
userName = st.text_input("your name")
userEmail = st.text_input("your email ID")
userMessage = st.text_input("your message")
#st.text("Phone: 480-815-2056")
#st.text("E-mail: Ethan.R.Huddleston@gmail.com")
st.divider()

#st.balloons()
#st.snow()
