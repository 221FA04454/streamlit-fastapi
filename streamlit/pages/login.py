
import streamlit as st
import requests

st.title("LoginForm")

# Deployed FastAPI backend
BASE_URL = "https://streamlit-fastapi-2.onrender.com"

with st.form("LoginForm"):

    e = st.text_input(
        "Email",
        placeholder="Enter Email here"
    )

    p = st.text_input(
        "Password",
        placeholder="Enter Password here",
        type="password"
    )

    r = st.selectbox(
        "Choose Role",
        ["Recruiter", "JobSeeker"]
    )

    btn = st.form_submit_button("Login")

    if btn:

        try:
            # Fetch users from deployed FastAPI
            response = requests.get(
                f"{BASE_URL}/get_all_users",
                timeout=30
            )

            if response.status_code == 200:

                all_users = response.json()

                user_found = False

                for user in all_users:

                    if (
                        user["email"] == e
                        and user["password"] == p
                        and user["role"] == r
                    ):

                        user_found = True

                        st.session_state["loggedin_user"] = {
                            "email": e,
                            "password": p,
                            "role": r
                        }

                        st.success(
                            f"Logged in as {r} successfully!"
                        )

                        if r == "Recruiter":
                            st.switch_page(
                                "pages/RecruiterDashboard.py"
                            )

                        elif r == "JobSeeker":
                            st.switch_page(
                                "pages/JobSeekerDashboard.py"
                            )

                        break

                if not user_found:
                    st.error(
                        "Invalid email, password, or role"
                    )

            else:
                st.error(
                    f"Backend error: {response.status_code}"
                )

        except requests.exceptions.RequestException as error:

            st.error(
                f"Unable to connect to FastAPI: {error}"
            )