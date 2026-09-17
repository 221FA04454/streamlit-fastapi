import streamlit as st 
import json
st.title("JobPortal")


if st.button("Login"):
    st.switch_page("pages/login.py")


if st.button("Register"):
    st.switch_page("pages/register.py")
    


    


    