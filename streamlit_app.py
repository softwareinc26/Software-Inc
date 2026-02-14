import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Software Inc",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed" # Starts with sidebar closed
)

# 2. CSS to Hide Menu, Sidebar, and Header
st.markdown("""
    <style>
    /* Hide the top right hamburger menu and the footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Hide the sidebar button and the sidebar itself */
    [data-testid="collapsedControl"] {display: none;}
    section[data-test-id="stSidebar"] {display: none;}
    
    /* Main Background */
    .stApp {
        background-color: #0E1117 !important;
    }
    
    /* Global Text Color */
    .stMarkdown, p, span {
        color: #E2E8F0 !important;
    }

    /* Headings */
    h1, h2, h3 {
        color: #FFFFFF !important;
        text-align: center;
    }

    /* Hero Section */
    .hero-container {
        padding: 5rem 2rem;
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #334155;
        border-radius: 20px;
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* Card styling for Portfolio */
    .portfolio-card {
        background-color: #161B22;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #30363D;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Website Content (Everything on one page)

# Hero Section
st.markdown("""
    <div class="hero-container">
        <h1 style="font-size: 3.5rem;">SOFTWARE <span style="color: #3b82f6;">INC.</span></h1>
        <p style="text-align: center; font-size: 1.3rem; color: #94A3B8 !important;">
            Specializing in Vision-Based Systems & Management Solutions
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("##") # Spacer

# Portfolio / Projects Section
st.markdown("### Featured Solutions")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="portfolio-card">', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=400", use_container_width=True)
    st.subheader("Campus Lens")
    st.write("A vision-based navigation tool designed to help students navigate educational campuses efficiently.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="portfolio-card">', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1454165205744-3b78555e5572?w=400", use_container_width=True)
    st.subheader("Business Ledger System")
    st.write("Robust software for retail store management, inventory tracking, and financial ledgers.")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# Footer-style Contact Section
st.markdown("<h3 style='text-align: center;'>Let's Build Together</h3>", unsafe_allow_html=True)
contact_col1, contact_col2, contact_col3 = st.columns([1, 2, 1])
with contact_col2:
    with st.form("clean_contact"):
        st.text_input("Name")
        st.text_input("Email")
        st.text_area("Message")
        st.form_submit_button("Submit")
