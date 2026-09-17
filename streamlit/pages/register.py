import streamlit as st
import json

st.title("RegisterForm")
with st.form("RegisterForm"):
    
    n=st.text_input("Name",placeholder="Enter Name here")
    e=st.text_input("Email",placeholder="Enter Email here")
    p=st.text_input("Password",placeholder="Enter Password here",type="password")
    c_p=st.text_input("Confirm_Password",placeholder="Re-Enter Password here",type="password")
    r=st.selectbox("Choose Role ",["Recruiter","JobSeeker"])
    btn=st.form_submit_button("Register")

    if btn:
        new_user={
            "name":n,
            "email":e ,
            "password":p,
            "c_password":c_p,
            "role":r
        }

        with open("users.json","r") as r_file:
            all_users=json.load(r_file) # []
            all_users.append(new_user) # [{}]
        
        with open("users.json","w") as w_file:
            json.dump(all_users,w_file) # [{}]

        st.success("successfully registered")  
        st.switch_page("pages/login.py")  


     