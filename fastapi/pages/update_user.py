import streamlit as st 
import requests


email=st.text_input("email",placeholder="enter email to do update opn")
name=st.text_input("name",placeholder="enter name to do update opn")
password=st.text_input("password",placeholder="enter passsowrd to do update opn",type="password")

if st.button("confirm_update"):
    update_data = {
        "name": name,
        "password": password
    }
    res=requests.put(f"http://127.0.0.1:8000/update_user/{email}",json=update_data) 
    if res.status_code==200:
        res_json=res.json()
        st.success(res_json)  