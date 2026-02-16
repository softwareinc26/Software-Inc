import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Software Inc | Innovation",
    page_icon="SI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS for Top-Right Dropdown, Dark Theme, and Team Cards
st.markdown("""
    <style>
    /* Hide the default sidebar */
    [data-testid="stSidebar"] { display: none; }

    /* Main Dark Background */
    .stApp {
        background-color: #0E1117 !important;
    }

    /* Force text colors for readability */
    .stMarkdown, p, span, label {
        color: #E2E8F0 !important;
    }
    h1, h2, h3 {
        color: #FFFFFF !important;
    }

    /* Dropdown Styling */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #161B22 !important;
        border: 1px solid #30363D !important;
    }
    
    /* Section Cards */
    .custom-card {
        background-color: #161B22;
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #30363D;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }

    /* Team Image Styling */
    .team-img img {
        border-radius: 10px;
        border: 1px solid #3b82f6;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Layout: Title on Left, Dropdown on Right
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
    
    # FOUNDERS SECTION
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    f_col1, f_col2 = st.columns([1, 2])
    

    with f_col2:
        st.subheader("Meet the Founder")
        st.write("""
        Bridging the gap between creative storytelling and technical excellence. 
        As an **Instagram creator** and **Software Engineer**, our founder specializes in 
        delivering user-centric digital tools like the **Campus Lens** navigation system.
        """)
        st.markdown("""
        - 🎓 **Developer of Campus Lens** (Developed for SIMATS)
        - 📸 **Digital Content Creator**
        - 🛠️ **Tech Stack:** Python, HTML, Computer Vision
        """)
    st.markdown('</div>', unsafe_allow_html=True)

    # TEAM SECTION
    st.write("---")
    st.header("Our Team")
    st.write("The collaborative power behind Software Inc.")

    # 5 Team Members in a Grid
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    row2_col1, row2_col2, _ = st.columns(3)

    team = [
        {"name": "Harish J", "desc": "Expert in Python backend and data architecture.", "img": "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"},
        {"name": "Sabareesh M", "desc": "Specializes in UI/UX design and frontend HTML.", "img": "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"},
        {"name": "Ashwin S", "desc": "Focuses on AI integration and vision systems.", "img": "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"},
        {"name": "Kamesh R", "desc": "Handles Social media & Marketing Dept", "img": "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"},
        {"name": "Divyesh S P", "desc": "Helping our company grow big.", "img": "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"},
    ]

    t_cols = [row1_col1, row1_col2, row1_col3, row2_col1, row2_col2]

    for i, member in enumerate(team):
        with t_cols[i]:
            st.image(member["img"], use_container_width=True)
            st.subheader(member["name"])
            st.write(member["desc"])
            st.write("") # Spacer

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
    st.write("Developed for SIMATS, this tool provides real-time navigation and has been scaled for campus-wide use.")
    st.image("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=600")
    st.divider()
    st.subheader("Business Ledger System")
    st.write("A secure retail management portal for handling transactions and inventory.")

# --- PAGE: CONTACT ---
elif page == "Contact":
    st.title("Get In Touch")
    with st.form("contact"):
        st.text_input("Full Name")
        st.text_input("Email")
        st.text_area("Tell us about your project")
        if st.form_submit_button("Send Message"):
            st.success("Message received. Our team will reach out to you shortly!")
