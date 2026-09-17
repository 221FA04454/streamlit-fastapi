# what is python ?
# what is fastapi  ? py lib which is used to build apis
# what is uvicorn ? py lib which is used create be server  
# uvicorn + fastAPI obj :--server create avutadhi / server run avvuddi

# pip install uvicorn fastapi

import streamlit as st
import requests

if st.button("Createuser"):
    st.switch_page("pages/create_user.py")

if st.button("GetUsers"):
    res=requests.get("http://127.0.0.1:8000/get_all_users")
    if res.status_code==200:
        res_json=res.json()
        st.dataframe(res_json)
    # with open()
if st.button("DeleteUser"):
    st.switch_page("pages/delete_user.py")

if st.button("UpdateUser"):
    st.switch_page("pages/update_user.py")

      


