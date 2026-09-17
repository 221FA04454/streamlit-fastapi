import streamlit as st 
import requests
# requests.post()

st.title("create user form")
with st.form("Create_user"):
    n=st.text_input("Name",placeholder="enter name here")
    e=st.text_input("Email",placeholder="enter name here")
    p=st.text_input("password",placeholder="enter name here",type="password")
    c_p=st.text_input("confirm_password",placeholder="enter name here",type="password")
    r=st.selectbox("Choose role :- ",["Recruiter","JobSeeker"])
    btn=st.form_submit_button("Create_User")
    if btn:
        new_user={
            "name":n,
            "email":e ,
            "password":p,
            "role":r
        }

        if p == c_p:
            res=requests.post("http://127.0.0.1:8000/create_user",json=new_user)
            if res.status_code==200:
                st.write(res.json()["msg"])
            else:
                st.error("something went wrong")    
            

