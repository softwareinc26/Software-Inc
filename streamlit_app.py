import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="Software Inc | Innovation",
    page_icon="SI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS
st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none; }
    .stApp { background-color: #0E1117 !important; }
    .stMarkdown, p, span, label { color: #E2E8F0 !important; }
    h1, h2, h3 { color: #FFFFFF !important; }
    .stSelectbox div[data-baseweb="select"] {
        background-color: #161B22 !important;
        border: 1px solid #30363D !important;
    }
    .custom-card {
        background-color: #161B22;
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #30363D;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Layout: Title and Navigation
header_left, header_right = st.columns([4, 1])

with header_left:
    st.markdown("# Software <span style='color:#3b82f6;'>Inc.</span>", unsafe_allow_html=True)

with header_right:
    page = st.selectbox(
        "Menu",
        ["Home", "Services", "Portfolio", "Contact"],
        label_visibility="collapsed"
    )

st.divider()

# --- PAGE: HOME ---
if page == "Home":
    st.write("### Engineering Tomorrow's Solutions Today")
    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200")
    

    st.header("Our Team")
    st.write("The collaborative power behind Software Inc.")

    # Fixed Team Grid Logic
    team = [
        {"name": "Jaya Harish J", "desc": "Expert in Python backend and data architecture.", "img": "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"},
        {"name": "Sabareesh M", "desc": "Specializes in UI/UX design and frontend HTML.", "img": "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"},
        {"name": "Ashwin S", "desc": "Focuses on AI integration and vision systems.", "img": "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"},
        {"name": "Kamesh R", "desc": "Handles Social media & Marketing Dept", "img": "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"},
        {"name": "Divyesh S P", "desc": "Helping our company grow big.", "img": "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"},
    ]

    # Create a grid of 3 columns
    cols = st.columns(3)
    for i, member in enumerate(team):
        with cols[i % 3]: # This cycles through the 3 columns
            st.image(member["img"], use_container_width=True)
            st.subheader(member["name"])
            st.write(member["desc"])
            st.write("---") 
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE: SERVICES ---
elif page == "Services":
    st.title("Our Expertise")
    s1, s2 = st.columns(2)
    with s1:
        st.info("### Web & Management Systems")
        st.write("Custom builds for business ledgers, salary management, and voting systems.")
    with s2:
        st.success("### AI & Campus Technology")
        st.write("Development of interactive tools like Campus Lens and vision-based interaction.")

# --- PAGE: PORTFOLIO ---
elif page == "Portfolio":
    st.title("Projects")
    st.subheader("Campus Lens: Navigation Tool")
    st.write("Developed for SIMATS, this tool provides real-time navigation.")
    st.image("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=600")
    st.divider()
    st.subheader("Business Ledger System")
    st.write("A secure retail management portal for handling transactions and inventory.")

# --- PAGE: CONTACT ---
elif page == "Contact":
    st.title("Get In Touch")
    
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email Address")
        message = st.text_area("Project Details")
        submitted = st.form_submit_button("Send to Software Inc.")
        
        if submitted:
            if name and email and message:
                st.success(f"Success! Your message has been routed to the team.")
                st.balloons()
            else:
                st.error("Please fill out all fields.")
