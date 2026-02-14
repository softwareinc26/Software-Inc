import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Software Inc | Digital Solutions",
    page_icon="💻",
    layout="wide"
)

# 2. Custom CSS for Professional Styling
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #f8fafc;
    }
    
    /* Hero section styling */
    .hero-container {
        padding: 3rem;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Custom Card styling for Services/Portfolio */
    .card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: white;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        height: 100%;
    }
    
    h1, h2, h3 {
        color: #1e293b;
    }
    
    .hero-container h1 {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
st.sidebar.title("🚀 Software Inc")
page = st.sidebar.radio("Navigation", ["Home", "Services", "Portfolio", "Contact"])

# --- PAGE: HOME ---
if page == "Home":
    st.markdown("""
        <div class="hero-container">
            <h1>Engineering the Next Generation of Software</h1>
            <p style="font-size: 1.2rem;">We transform complex challenges into elegant, scalable digital experiences.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Why Partner With Us?")
        st.write("""
        At Software Inc, we don't just write code; we build assets. Whether you need a 
        robust business ledger system or a cutting-edge campus navigation tool, our 
        team delivers performance-driven results.
        """)
        st.button("Explore Our Work")
    with col2:
        st.image("https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=800", caption="Code is our Craft")

# --- PAGE: SERVICES ---
elif page == "Services":
    st.title("Our Expertise")
    st.write("Specialized solutions tailored to your business needs.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("### Web Development")
        st.write("Developing dynamic web applications using Python, HTML, and modern frameworks.")
    with c2:
        st.success("### AI & Automation")
        st.write("Vision-based systems and gesture interaction for the next tech frontier.")
    with c3:
        st.warning("### Management Systems")
        st.write("Custom-built salary, doctor, and voting management portals.")

# --- PAGE: PORTFOLIO ---
elif page == "Portfolio":
    st.title("Featured Projects")
    st.write("A glimpse into our successful deployments.")
    
    # Project 1: Campus Navigation
    with st.container():
        col_img, col_txt = st.columns([1, 2])
        with col_img:
            st.image("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=400")
        with col_txt:
            st.subheader("Campus Lens: Navigation Tool")
            st.write("""
            An interactive navigation tool designed for educational institutions (like SIMATS) 
            to help students and visitors find their way easily across campus.
            """)
            st.markdown("**Tech Stack:** Python, Streamlit, Web Tech")

    st.divider()

    # Project 2: Business Ledger
    with st.container():
        col_img, col_txt = st.columns([1, 2])
        with col_img:
            st.image("https://images.unsplash.com/photo-1454165205744-3b78555e5572?auto=format&fit=crop&w=400")
        with col_txt:
            st.subheader("Retail & Ledger Management")
            st.write("Secure systems for managing business ledgers and retail inventory.")
            st.markdown("**Tech Stack:** Python, Database Integration")

# --- PAGE: CONTACT ---
elif page == "Contact":
    st.title("Get In Touch")
    st.write("Ready to start your project? Let’s connect.")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        msg = st.text_area("How can we help you?")
        
        if st.form_submit_button("Submit Request"):
            if name and email:
                st.success(f"Thank you, {name}! Our software team will contact you at {email} soon.")
            else:
                st.error("Please fill in your name and email.")
