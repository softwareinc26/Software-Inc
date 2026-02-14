import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Software Inc | Innovation Redefined", layout="wide")

# 2. Custom CSS for Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .hero-text {
        font-size: 50px;
        font-weight: 700;
        color: #1E3A8A;
        text-align: center;
    }
    </style>
    """, unsafe_allow_実験=True)

# 3. Sidebar Navigation
st.sidebar.title("🚀 Software Inc")
page = st.sidebar.radio("Navigate", ["Home", "Services", "Portfolio", "Contact Us"])

# 4. Home Page
if page == "Home":
    st.markdown('<p class="hero-text">We Build the Future of Software</p>', unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Transforming Ideas into Scalable Code")
        st.write("""
            At Software Inc, we specialize in high-performance web applications, 
            AI integration, and cloud infrastructure. Our mission is to bridge 
            the gap between complex problems and elegant digital solutions.
        """)
        st.button("Get Started")
    with col2:
        # Placeholder for a high-tech illustration
        st.image("https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800", caption="Engineering Excellence")

# 5. Services Page
elif page == "Services":
    st.header("Our Expertise")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("### Web Development")
        st.write("Modern frameworks (React, Next.js) and robust backends (Python/Go).")
    
    with col2:
        st.success("### AI & Data Science")
        st.write("Custom LLM integration and predictive analytics dashboards.")
        
    with col3:
        st.warning("### Cloud Ops")
        st.write("AWS/Azure architecture and CI/CD pipeline automation.")

# 6. Contact Page
elif page == "Contact Us":
    st.header("Let's Talk Shop")
    with st.form("contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        project = st.text_area("Tell us about your project")
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            st.toast(f"Thanks {name}, our team will reach out to {email} shortly!")
