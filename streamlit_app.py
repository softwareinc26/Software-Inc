import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Software Inc | Innovation",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed" # Hides the default left sidebar
)

# 2. Custom CSS for Right Sidebar & Text Links
st.markdown("""
    <style>
    /* Hide the default left sidebar completely */
    [data-testid="stSidebar"] {
        display: none;
    }

    /* Set main background to deep dark */
    .stApp {
        background-color: #0E1117 !important;
    }

    /* Force all standard text to light gray/white */
    .stMarkdown, p, span, label {
        color: #E2E8F0 !important;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #FFFFFF !important;
    }

    /* Custom Right Menu Container */
    .right-nav-container {
        border-left: 1px solid #30363D;
        padding-left: 30px;
        margin-top: 50px;
        height: 80vh;
    }

    /* Style buttons to appear as plain text links */
    div.stButton > button {
        background-color: transparent !important;
        color: #94A3B8 !important;
        border: none !important;
        padding: 5px 0px !important;
        font-size: 1.2rem !important;
        font-weight: 500 !important;
        text-align: left !important;
        box-shadow: none !important;
        transition: 0.3s;
        width: auto;
    }

    div.stButton > button:hover {
        color: #3b82f6 !important;
        text-decoration: underline;
    }

    /* Active Page Indicator Styling */
    .active-indicator {
        color: #3b82f6;
        font-weight: bold;
        font-size: 0.85rem;
        margin-top: -10px;
        margin-bottom: 20px;
    }

    /* Portfolio Image Styling */
    .project-img {
        border-radius: 10px;
        border: 1px solid #30363D;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State for Navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'

def change_page(name):
    st.session_state.current_page = name

# 4. Main Layout: [Content (85%)] [Right Menu (15%)]
col_content, col_spacer, col_menu = st.columns([6, 0.5, 1.5])

# --- RIGHT SIDEBAR NAVIGATION ---
with col_menu:
    st.markdown('<div class="right-nav-container">', unsafe_allow_html=True)
    st.write("### Navigation")
    st.write("") # Spacer

    # Text-link buttons
    if st.button("Home", key="nav_home"):
        change_page('Home')
    
    if st.button("Services", key="nav_services"):
        change_page('Services')
    
    if st.button("Portfolio", key="nav_portfolio"):
        change_page('Portfolio')
    
    if st.button("Contact", key="nav_contact"):
        change_page('Contact')

    # Status Indicator
    st.markdown(f'<p class="active-indicator">Currently on {st.session_state.current_page}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN CONTENT AREA ---
with col_content:
    if st.session_state.current_page == "Home":
        st.title("Software Inc.")
        st.markdown("### Engineering the future with high-performance digital solutions.")
        st.write("---")
        st.image("https://images.unsplash.com/photo-1550439062-609e1531270e?auto=format&fit=crop&w=1000", caption="Digital Excellence")
        st.write("""
        Welcome to the home of Software Inc. We specialize in building scalable web applications, 
        automated management systems, and vision-integrated tools designed to solve modern problems.
        """)

    elif st.session_state.current_page == "Services":
        st.title("Our Services")
        st.write("### 💻 Web Development")
        st.write("Custom portals for salary management, doctor management, and business ledgers using Python and HTML.")
        
        st.write("### 🖖 AI & Interaction")
        st.write("Vision-based hand gesture interaction systems and intelligent automation.")
        
        st.write("### 🗺️ Institutional Tools")
        st.write("Bespoke campus navigation tools and interactive maps for large-scale environments.")

    elif st.session_state.current_page == "Portfolio":
        st.title("Featured Projects")
        
        # Campus Lens Project
        st.subheader("Campus Lens")
        st.write("A specialized navigation tool built for SIMATS to enhance campus-wide mobility.")
        st.image("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=600")
        st.write("**Tech Stack:** Python, Streamlit, Computer Vision")
        st.divider()

        # Business Ledger Project
        st.subheader("Retail Ledger System")
        st.write("Secure business ledger application for managing retail transactions and inventory.")
        st.write("**Tech Stack:** Python, SQL Integration")

    elif st.session_state.current_page == "Contact":
        st.title("Get In Touch")
        st.write("Ready to build something amazing? Reach out below.")
        with st.form("contact_form"):
            st.text_input("Name")
            st.text_input("Email")
            st.text_area("How can we help your business?")
            submitted = st.form_submit_button("Send Inquiry")
            if submitted:
                st.success("Message sent! Our software team will contact you shortly.")
