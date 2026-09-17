import streamlit as st 

# st.session_state={
#     "loggedin_user":{
#         "e":e,
#         "p":p,
#         "r":r
#         }
#     }

if  not "loggedin_user" in st.session_state: # if True
    st.warning("no loggedin user is able to access this file") 
    st.switch_page("pages/login.py")

if st.session_state["loggedin_user"]["role"] == "JobSeeker":
    st.title("JobSeekerDashboard")
else:
    st.warning("you are not JobSeeker so you are nit allowed to access this page") 