import streamlit as st
st.title("Hassan Faisal")
about_page=st.Page(
    page="pages/about_me.py",
    title="About Me",
    icon="👤",
    default=True
)

# st.markdown('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">', unsafe_allow_html=True)
# st.markdown('<i class="material-icons">account_circle</i> This is an account icon', unsafe_allow_html=True)