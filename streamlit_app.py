import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Software Inc | Dark Edition",
    page_icon="🌙",
    layout="wide"
)

# 2. Complete Dark Theme CSS
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0E1117 !important;
    }
    
    /* Global Text Color */
    .stMarkdown, p, span, label, .stSelectbox, .stTextInput {
        color: #E2E8F0 !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #161B22 !important;
        border-right: 1px solid #30363D;
    }
    
    /* Hero Section - Deep Gradient */
    .hero-container {
        padding: 4rem 2rem;
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #334155;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* Service Cards */
    .service-card {
        background-color: #161B22 !important;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #30363D;
        height: 100%;
        transition: transform 0.3s ease;
    }
    .service-card:hover {
        border-color: #3b82f6;
        transform: translateY(-5px);
    }

    /* Input Fields & Forms */
    input, textarea {
        background-color: #0D1117 !important;
        color: white !important;
        border: 1px solid #30363D !important;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6, #2563eb) !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
st.sidebar.title("🚀 Software Inc")
page = st.sidebar.radio("Navigate", ["Home", "Services", "Portfolio", "Contact"])

# --- PAGE: HOME ---
if page == "Home":
    st.markdown("""
        <div class="hero-container">
            <h1 style="font-size: 3rem; margin-bottom: 10px;">Building the Future, <span style="color: #3b82f6;">Line by Line.</span></h1>
            <p style="font-size: 1.2rem; color: #94A3B8 !important;">Specializing in AI-driven tools, web applications, and campus solutions.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Welcome to Software Inc")
        st.write("""
        We deliver high-performance software solutions tailored to modern business needs. 
        From custom management systems to vision-based interaction, our code is built 
        to scale and succeed.
        """)
        st.button("View Portfolio")
    with col2:
        st.image("https://images.unsplash.com/photo-1550439062-609e1531270e?auto=format&fit=crop&w=800", caption="Precision Engineering")

# --- PAGE: SERVICES ---
elif page == "Services":
    st.title("Our Services")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""<div class="service-card">
            <h3 style="color:#3b82f6 !important">Web Apps</h3>
            <p>Full-stack Python and HTML development for business ledgers and management systems.</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="service-card">
            <h3 style="color:#10b981 !important">AI Systems</h3>
            <p>Specialized vision-based hand gesture interaction and automated toolkits.</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="service-card">
            <h3 style="color:#f59e0b !important">Campus Tech</h3>
            <p>Interactive navigation tools and campus-specific software ecosystems.</p>
        </div>""", unsafe_allow_html=True)

# --- PAGE: PORTFOLIO ---
elif page == "Portfolio":
    st.title("Portfolio")
    
    # Project 1
    with st.container():
        c_img, c_txt = st.columns([1, 2])
        with c_img:
            st.image("https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=400")
        with c_txt:
            st.subheader("Campus Lens")
            st.write("A comprehensive navigation tool built for SIMATS to streamline campus mobility.")
            st.markdown("`Python` `Streamlit` `Computer Vision`")

# --- PAGE: CONTACT ---
elif page == "Contact":
    st.title("Contact Us")
    with st.form("contact"):
        st.text_input("Company Name")
        st.text_input("Work Email")
        st.text_area("How can we help?")
        if st.form_submit_button("Send Inquiry"):
            st.success("Your message was sent into the void (just kidding, we'll get back to you!)")
