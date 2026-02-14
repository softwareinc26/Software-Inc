import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Software Inc | Innovation",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS for Top-Right Dropdown & Dark Theme
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
    
    /* Founder Section Card */
    .founder-card {
        background-color: #161B22;
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #30363D;
        margin-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Layout: Title on Left, Dropdown on Right
header_left, header_right = st.columns([4, 1])

with header_left:
    st.markdown("# Software <span style='color:#3b82f6;'>Inc.</span>", unsafe_allow_html=True)

with header_right:
    # Navigation Dropdown
    page = st.selectbox(
        "Menu",
        ["Home", "Services", "Portfolio", "Contact"],
        label_visibility="collapsed"
    )

st.divider()

# --- PAGE: HOME ---
if page == "Home":
    st.write("### Engineering Tomorrow's Solutions Today")
    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1000")
    
    # FOUNDERS SECTION
    st.markdown('<div class="founder-card">', unsafe_allow_html=True)
    f_col1, f_col2 = st.columns([1, 2])
    
    with f_col1:
        # Placeholder for Founder Image
        st.image("https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400", 
                 caption="Lead Developer & Founder")
    
    with f_col2:
        st.subheader("Our Founder")
        st.write("""
        Driven by a passion for technical innovation and digital storytelling. 
        As an **Instagram creator** and **Software Engineer**, our founder specializes in 
        bridging the gap between complex code and user-centric design.
        """)
        st.write("""
        Notable projects include a **Vision-based Hand Gesture Interaction system** 
        and the **Campus Lens navigation tool**, which gained significant interest for 
        large-scale implementation.
        """)
        st.markdown("""
        - **Expertise:** Python, HTML, Web Apps, AI
        - **Projects:** Campus Lens, Management Systems, Retail Ledger
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE: SERVICES ---
elif page == "Services":
    st.title("Services")
    s1, s2 = st.columns(2)
    with s1:
        st.info("### Web & Management")
        st.write("Custom builds for Doctor Management, Voting Systems, and Business Ledgers.")
    with s2:
        st.success("### AI & Navigation")
        st.write("Specialized vision-based tools and campus-wide navigation ecosystems.")

# --- PAGE: PORTFOLIO ---
elif page == "Portfolio":
    st.title("Project Portfolio")
    st.subheader("Campus Lens")
    st.write("A campus navigation tool recognized for its utility and scale.")
    st.image("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=600")

# --- PAGE: CONTACT ---
elif page == "Contact":
    st.title("Contact")
    with st.form("contact"):
        st.text_input("Name")
        st.text_area("How can we help?")
        st.form_submit_button("Send")
