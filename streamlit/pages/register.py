
import streamlit as st
import requests

st.title("RegisterForm")

# Deployed FastAPI backend
BASE_URL = "https://streamlit-fastapi-2.onrender.com"

with st.form("RegisterForm"):

    n = st.text_input(
        "Name",
        placeholder="Enter Name here"
    )

    e = st.text_input(
        "Email",
        placeholder="Enter Email here"
    )

    p = st.text_input(
        "Password",
        placeholder="Enter Password here",
        type="password"
    )

    c_p = st.text_input(
        "Confirm_Password",
        placeholder="Re-Enter Password here",
        type="password"
    )

    r = st.selectbox(
        "Choose Role",
        ["Recruiter", "JobSeeker"]
    )

    btn = st.form_submit_button("Register")

    if btn:

        if p != c_p:
            st.error("Passwords do not match")

        elif not n or not e or not p:
            st.error("Please fill all required fields")

        else:

            new_user = {
                "name": n,
                "email": e,
                "password": p,
                "c_password": c_p,
                "role": r
            }

            try:

                response = requests.post(
                    f"{BASE_URL}/create_user",
                    json=new_user,
                    timeout=30
                )

                if response.status_code == 200:

                    st.success(
                        "Successfully registered"
                    )

                    st.switch_page(
                        "pages/login.py"
                    )

                else:

                    st.error(
                        f"Registration failed: "
                        f"{response.status_code}"
                    )

            except requests.exceptions.RequestException as error:

                st.error(
                    f"Unable to connect to FastAPI: {error}"
                )