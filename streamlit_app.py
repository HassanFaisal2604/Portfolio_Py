import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "todo.py",
    title="TO DO APP",
    icon="👨‍🏭",
)

project_2_page = st.Page(
    "qr_code_generator.py",
    title="QR Code Generator",
    icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)


# --- SHARED ON ALL PAGES ---



# --- RUN NAVIGATION ---
pg.run()
