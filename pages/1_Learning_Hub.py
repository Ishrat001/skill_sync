import streamlit as st
import json
from gemini_config import client

st.set_page_config(page_title="Learning Hub")

st.title("📚 AI Learning Hub")

role = st.text_input(
    "Target Role",
    placeholder="Data Analyst"
)

if st.button("Generate Learning Plan"):

    if not role.strip():
        st.warning("⚠️ Please provide a target market role to initialize the graph.")
        st.stop()

    with st.spinner("Building roadmap..."):

        prompt = f"""
        You are an elite global career strategist,
        learning architect,
        AI mentor,
        hiring manager,
        and workforce analyst.

        Create a complete employability roadmap
        for a student who wants to become:

        ROLE: {role}

        Requirements:

        1. Explain the role.
        2. Explain market demand.
        3. List beginner skills.
        4. List intermediate skills.
        5. List advanced skills.
        6. Recommend AI tools.
        7. Recommend learning sequence.
        8. Recommend certifications.
        9. Recommend YouTube resources.
        10. Recommend portfolio projects.
        11. Suggest internship strategy.
        12. Suggest LinkedIn strategy.
        13. Mention common mistakes.
        14. Suggest a realistic timeline.

        Return ONLY JSON.

        {{
            "role_overview":"",
            "market_demand":"",
            "beginner_skills":[],
            "intermediate_skills":[],
            "advanced_skills":[],
            "ai_tools":[],
            "youtube_resources":[],
            "certifications":[],
            "projects":[],
            "linkedin_strategy":[],
            "internship_strategy":[],
            "common_mistakes":[],
            "timeline":[]
        }}
        """

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        except Exception as e:

            st.error(
                "Gemini service is temporarily unavailable. Please try again."
            )

            st.stop()

        text = response.text.strip()

        text = text.replace(
            "```json", ""
        ).replace(
            "```", ""
        )

        try:
            data = json.loads(text)

        except Exception:
            st.error("AI returned invalid response. Please try again.")
            st.code(text)
            st.stop()

        st.subheader("🌍 Role Overview")
        st.write(data["role_overview"])

        st.subheader("📈 Market Demand")
        st.write(data["market_demand"])

        st.subheader("🟢 Beginner Skills")
        for item in data["beginner_skills"]:
            st.write("•", item)

        st.subheader("🟡 Intermediate Skills")
        for item in data["intermediate_skills"]:
            st.write("•", item)

        st.subheader("🔴 Advanced Skills")
        for item in data["advanced_skills"]:
            st.write("•", item)

        st.subheader("🤖 AI Tools")
        for item in data["ai_tools"]:
            st.write("•", item)

        st.subheader("🛠 Portfolio Projects")
        for item in data["projects"]:
            st.write("•", item)

        st.subheader("📜 Certifications")
        for item in data["certifications"]:
            st.write("•", item)

        st.subheader("🎥 YouTube Resources")
        for item in data["youtube_resources"]:
            st.write("•", item)

        st.subheader("💼 LinkedIn Strategy")
        for item in data["linkedin_strategy"]:
            st.write("•", item)

        st.subheader("🚀 Internship Strategy")
        for item in data["internship_strategy"]:
            st.write("•", item)

        st.subheader("⚠ Common Mistakes")
        for item in data["common_mistakes"]:
            st.write("•", item)

        st.subheader("📅 Learning Timeline")
        for item in data["timeline"]:
            st.write("•", item)