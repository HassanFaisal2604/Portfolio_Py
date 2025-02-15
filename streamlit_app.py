import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# Add hero section
st.title("Welcome to My Portfolio")

# Add main content
st.header("Portfolio Overview")
st.markdown("""
### 👋 Hello there!

I'm Hassan, a Computer Science student passionate about building things with code. 
This portfolio showcases my projects and skills.

### 📚 What you'll find here:

- **About Me**: Learn about my background and skills
- **Todo App**: A simple but effective task management application
- **QR Code Generator**: Create QR codes easily
- **Photography**: View my photography portfolio

*Use the sidebar to navigate through different sections!*
""")

# Add a footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")

# --- PAGE SETUP ---
# about_page = st.Page( 
#     page=about_page.py# Update path
#     title="About Me",
#     icon=":material/account_circle:",
# )
# project_1_page = st.Page(  # Update path
#     title="TO DO APP",
#     icon="👨‍🏭",
# )

# project_2_page = st.Page(
#     path="pages/qr_code_generator.py",  # Update path
#     title="QR Code Generator",
#     icon=":material/smart_toy:",
# )

# # Add the new photography page
# project_3_page = st.Page(
#     path="pages/photography.py",  # Update path
#     title="Photography",
#     icon="📸",
# )


# # --- NAVIGATION SETUP [WITH SECTIONS]---
# pg = st.navigation(
#     {
#         "Projects": [st.Page("about_me.py"), project_2_page, project_3_page],
#     }
# )


# --- SHARED ON ALL PAGES ---



# --- RUN NAVIGATION ---

# pg.run()