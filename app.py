import streamlit as st

st.set_page_config(
    page_title="SkillSync AI",
    page_icon="🎯",
    layout="wide"
)

with st.sidebar:
    st.title("🎯 SkillSync AI")
    st.caption("AI-Powered Career Intelligence Platform")

    st.markdown("---")

    app_mode = st.radio(
        "Workspace",
        [
            " HomePage",
        ]
    )

    st.markdown("---")

    st.markdown("""
    ###  Venture Profile

    - **Startup:** SkillSync AI  
    - **Founders:** Ishrat & Nafisa  
    - **Department:** CSE, University of Dhaka  
    - **Mission:** Bridging academic knowledge with global employability
    """)

st.title("🎯 SkillSync AI")

st.markdown("""
## Turn Degrees Into Wealth

SkillSync AI is an AI-powered employability platform designed to bridge the gap between academic education and real-world opportunities.

Many graduates possess degrees but lack the specific skills demanded by today's rapidly evolving job market.

Our platform helps students identify skill gaps, develop personalized learning roadmaps, prepare for interviews, build professional resumes, and discover meaningful career opportunities.

---
""")

col1, col2 = st.columns(2)

with col1:

    st.subheader(" What We Offer")

    st.markdown("""
    - AI Career Analysis
    - Personalized Learning Roadmaps
    - Opportunity Discovery
    - ATS-Friendly Resume Building
    - Interview Preparation
    """)

with col2:

    st.subheader(" Impact")

    st.markdown("""
    - Reduce Skill Gap
    - Increase Employability
    - Improve Career Readiness
    - Enable Financial Independence
    - Support Future Workforce Development
    """)

st.markdown("---")

st.subheader(" Product Modules")

st.markdown("""
###  Career Navigator
Analyze strengths, weaknesses, employability and market fit.

###  Learning Hub
Generate personalized learning plans and skill roadmaps.

###  Opportunity Finder
Discover internships, freelancing and remote opportunities.

###  Resume Builder
Create ATS-friendly professional resumes.

###  Interview Coach
Practice interviews and receive AI-powered feedback.
""")

st.markdown("---")

st.success(
    "Built by Team SkillSync | Department of Computer Science and Engineering | University of Dhaka"
)