import streamlit as st 



if  not "loggedin_user" in st.session_state: # if True
    st.warning("no loggedin user is able to access this file") 
    st.switch_page("pages/login.py")

if st.session_state["loggedin_user"]["role"] == "Recruiter":
    st.title("RecruiterDashboard")
else:
    st.warning("you are not recruiter so you are nit allowed to access this page")    