import streamlit as st
import json
from gemini_config import client

st.set_page_config(page_title="Resume Builder")

with st.sidebar:
    st.title("🎯 SkillSync AI")
    st.caption("AI-Powered Career Intelligence Platform")

    st.markdown("---")

    app_mode = st.radio(
        "Workspace",
        [
            "🔮 AI Resume Builder",
        ]
    )

    st.markdown("---")

    st.markdown("""
    ### 🚀 Venture Profile

    - **Startup:** SkillSync AI  
    - **Founders:** Ishrat & Nafisa  
    - **Department:** CSE, University of Dhaka  
    - **Mission:** Bridging academic knowledge with global employability
    """)

st.title("📄 AI Resume Builder")

name = st.text_input("Full Name")

degree = st.text_input(
    "Degree",
    placeholder="BSc in CSE"
)

skills = st.text_area(
    "Skills",
    placeholder="Python, SQL, Excel"
)

projects = st.text_area(
    "Projects",
    placeholder="Inventory Management System"
)

if st.button("Generate Resume"):

    with st.spinner("Building ATS-friendly resume..."):

        prompt = f"""
        Create a professional ATS-friendly resume.

        Name: {name}
        Degree: {degree}
        Skills: {skills}
        Projects: {projects}

        Return ONLY JSON.

        {{
            "professional_summary":"",
            "career_objective":"",
            "skills":[],
            "projects":[],
            "education":""
        }}
        """

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            text = response.text.strip()

            text = text.replace(
                "```json",""
            ).replace(
                "```",""
            )

            data = json.loads(text)

        except Exception:

            st.error(
                "Unable to generate resume. Please try again."
            )

            st.stop()

        st.subheader("👤 Professional Summary")
        st.write(data["professional_summary"])

        st.subheader("🎯 Career Objective")
        st.write(data["career_objective"])

        st.subheader("🧠 Skills")

        for item in data["skills"]:
            st.write("•", item)

        st.subheader("🛠 Projects")

        for item in data["projects"]:
            st.write("•", item)

        st.subheader("🎓 Education")
        st.write(data["education"])

        # =========================
        # DOWNLOAD RESUME
        # =========================

        resume_text = f"""
        PROFESSIONAL SUMMARY

        {data["professional_summary"]}

        CAREER OBJECTIVE

        {data["career_objective"]}

        SKILLS

        {chr(10).join(data["skills"])}

        PROJECTS

        {chr(10).join(data["projects"])}

        EDUCATION

        {data["education"]}
        """

        st.download_button(
            label="📥 Download Resume",
            data=resume_text,
            file_name="resume.txt",
            mime="text/plain"
        )