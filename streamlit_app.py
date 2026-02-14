import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Software Inc | Dark Mode",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Advanced CSS to Hide Sidebar and Style Right-Side Menu
st.markdown("""
    <style>
    /* Hide the default Streamlit sidebar and decoration */
    [data-testid="stSidebar"], .st-emotion-cache-16idsys, [data-testid="stSidebarNav"] {
        display: none;
    }
    
    /* Main Background */
    .stApp {
        background-color: #0E1117 !important;
    }

    /* Text Colors */
    .stMarkdown, p, span {
        color: #E2E8F0 !important;
    }
    h1, h2, h3 {
        color: #FFFFFF !important;
    }

    /* Right-side Menu Styling */
    .nav-link {
        text-decoration: none;
        color: #94A3B8 !important;
        font-size: 1.1rem;
        font-weight: 500;
        display: block;
        padding: 10px 0;
        text-align: right;
        transition: 0.3s;
    }
    .nav-link:hover {
        color: #3b82f6 !important;
    }
    .active-link {
        color: #3b82f6 !important;
        font-weight: 700;
        border-right: 3px solid #3b82f6;
        padding-right: 10px;
    }

    /* Hero Section */
    .hero-box {
        padding: 3rem;
        background: #161B22;
        border-radius: 15px;
        border: 1px solid #30363D;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Handle Navigation State
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def set_page(name):
    st.session_state.page = name

# 4. Layout: Content on Left (col1), Menu on Right (col2)
content_col, menu_col = st.columns([4, 1])

with menu_col:
    st.write("### Menu")
    # Custom Text Links
    if st.button("Home", key="btn_home", help="Go to Home", use_container_width=True, type="secondary"):
        set_page('Home')
    if st.button("Services", key="btn_serv", help="Our Expertis", use_container_width=True):
        set_page('Services')
    if st.button("Portfolio", key="btn_port", help="Our Projects", use_container_width=True):
        set_page('Portfolio')
    if st.button("Contact", key="btn_cont", help="Reach Out", use_container_width=True):
        set_page('Contact')
    
    # Visual indicator of where you are
    st.markdown(f"<div style='text-align:right; color:#3b82f6; font-size:0.8rem;'>Currently viewing: {st.session_state.page}</div>", unsafe_allow_html=True)

with content_col:
    # --- PAGE: HOME ---
    if st.session_state.page == "Home":
        st.markdown("""
            <div class="hero-box">
                <h1 style="margin:0;">Software <span style="color:#3b82f6;">Inc.</span></h1>
                <p style="color:#94A3B8;">Innovative digital solutions for a connected world.</p>
            </div>
        """, unsafe_allow_html=True)
        st.write("---")
        st.subheader("Welcome")
        st.write("We specialize in custom web applications, automation tools, and vision-based systems.")

    # --- PAGE: SERVICES ---
    elif st.session_state.page == "Services":
        st.title("Services")
        st.info("**Web Development:** Python & HTML expert builds.")
        st.success("**AI Solutions:** Gesture interaction & Vision tools.")
        st.warning("**Management:** Business Ledger & Salary systems.")

    # --- PAGE: PORTFOLIO ---
    elif st.session_state.page == "Portfolio":
        st.title("Portfolio")
        st.subheader("Campus Lens")
        st.write("Interactive navigation tool developed for college campuses.")
        st.image("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=400")

    # --- PAGE: CONTACT ---
    elif st.session_state.page == "Contact":
        st.title("Contact")
        st.write("Ready to build? Send us a message.")
        with st.form("contact"):
            st.text_input("Name")
            st.text_area("Message")
            st.form_submit_button("Submit")
