import streamlit as st

from contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/picofme (3).png", width=250)

with col2:
    st.title("Hassan Faisal", anchor=False)
    st.write(
        "Computer Science Student | AI & DSA Enthusiast | Aspiring Backend Developer"
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    
    - Strong programming knowledge in Python and C++
    - Good understanding of Data Structures & Algorithms
    - Learning Backend Development with Django
    - Experience with Linux (Ubuntu) for development
    - Strong problem-solving skills with hands-on coding experience
    - 2 years of experience in Professional photography
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Technical Skills", anchor=False)
st.write(
    """
    - Programming: Python (Django, Flask), C++, SQL
    - Web Development: HTML, CSS, JavaScript
    - Databases: MySQL, PostgreSQL
    - Tools & Platforms: Git, Linux (Ubuntu), Streamlit
    - AI & Data Science: Machine Learning basics, Pandas, NumPy
    - Content Creation: Photography, Image Editing
    """
)
