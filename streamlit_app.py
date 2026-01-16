import os
import requests
import streamlit as st

st.set_page_config(page_title="Family Details", page_icon="👪", layout="centered")
st.title("Family Details")
name = st.text_input("Enter celebrity name")
backend = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")
timeout_secs = int(os.environ.get("BACKEND_TIMEOUT", "600"))
if st.button("Fetch"):
    if not name.strip():
        st.error("Please enter a name")
    else:
        with st.spinner(f"Fetching from backend (timeout {timeout_secs}s)..."):
            try:
                r = requests.post(f"{backend}/family", json={"name": name}, timeout=timeout_secs)
                if r.status_code == 200:
                    data = r.json()
                    st.subheader(data.get("name", ""))
                    st.write(data.get("family", ""))
                else:
                    st.error(f"Error {r.status_code}")
            except requests.exceptions.Timeout:
                st.error("Request timed out. Try again; first run can take longer while models load.")
            except Exception as e:
                st.error(str(e))
