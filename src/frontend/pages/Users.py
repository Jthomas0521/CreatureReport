import streamlit as st
import requests

FASTAPI_URL = "http://localhost:8000"

st.set_page_config(page_title="Registered Users", layout="wide")
st.title(" Registered Users")

try:
    res = requests.get(f"{FASTAPI_URL}/users")
    if res.status_code == 200:
        users = res.json()
        if users:
            for u in users:
                st.markdown(f"👤 **{u['email']}** — _{u['favorite_team']}_")
        else:
            st.info("No users yet.")
    else:
        st.error("Failed to load users.")
except Exception as e:
    st.error(f"Error fetching users: {e}")
