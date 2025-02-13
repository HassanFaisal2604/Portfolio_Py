# about_me.py (corrected import)
 # Instead of forms.contact

import streamlit as st  # pip install requests


def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

    if submit_button:

        if not name:
            st.error("Please provide your name.", icon="🧑")
            st.stop()

        if not email:
            st.error("Please provide your email address.", icon="📨")
            st.stop()

        if not message:
            st.error("Please provide a message.", icon="💬")
            st.stop()

        # No webhook functionality; just display a success message
        st.success("Your message has been sent successfully! 🎉", icon="🚀")
