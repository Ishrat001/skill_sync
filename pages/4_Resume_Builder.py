import streamlit as st
import json
from gemini_config import client

st.set_page_config(page_title="Resume Builder")

with st.sidebar:
    st.title("🎯 SkillSync AI")
    st.caption("AI-Powered Career Intelligence Platform")

    st.markdown("---")

    st.radio(
        "Workspace",
        [
            "AI Resume Builder",
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

        IMPORTANT:
        Return ONLY valid JSON.

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
                model="gemini-2.0-flash",
                contents=prompt
            )

            text = response.text.strip()

            text = text.replace(
                "```json", ""
            ).replace(
                "```", ""
            )

            data = json.loads(text)

        except Exception:

            st.error(
                "Unable to generate resume. Please try again."
            )

            st.stop()

        st.subheader("🧾 Professional Summary")
        st.write(
            data.get(
                "professional_summary",
                "Not available"
            )
        )

        st.subheader("🎯 Career Objective")
        st.write(
            data.get(
                "career_objective",
                "Not available"
            )
        )

        st.subheader("🛠 Skills")

        skills_data = data.get("skills", [])

        if isinstance(skills_data, list):

            for item in skills_data:
                st.write(f"• {item}")

        else:
            st.write(skills_data)

        st.subheader("🚀 Projects")

        projects_data = data.get("projects", [])

        if isinstance(projects_data, list):

            for item in projects_data:
                st.write(f"• {item}")

        else:
            st.write(projects_data)

        st.subheader("🎓 Education")

        st.write(
            data.get(
                "education",
                degree
            )
        )