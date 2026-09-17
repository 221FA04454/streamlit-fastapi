import streamlit as st
import json
st.title("LoginForm")
with st.form("LoginForm"):
    
    e=st.text_input("Email",placeholder="Enter Email here")
    p=st.text_input("Password",placeholder="Enter Password here",type="password")
    r=st.selectbox("Choose Role ",["Recruiter","JobSeeker"])
    btn=st.form_submit_button("Login")


    if btn:
        with open("users.json","r") as r_file:
            all_users=json.load(r_file)

            for user in all_users:
                if user["email"]  == e and user["password"] == p:
                    if r== "Recruiter":
                        st.session_state["loggedin_user"]={"email":e,"password":p,"role":r}
                        st.success("loggedin as recruiter successfully and navigating towards to RecruiterDashboard") 
                        st.switch_page("pages/RecruiterDashboard.py")
                        break
                    if r == "JobSeeker":
                        st.success("loggedin as jobseeker successfully and navigating towards to JobSeekerDashboard") 
                        st.switch_page("pages/JobSeekerDashboard.py")
                        break
                        
                else:
                    st.error("user not found with that credentials")