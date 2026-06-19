import streamlit as st
import json
from gemini_config import client

st.set_page_config(page_title="Opportunity Finder")

st.title("💼 Opportunity Finder")

role = st.text_input(
    "Target Role",
    placeholder="Data Analyst"
)

if st.button("Find Opportunities"):

    with st.spinner("Analyzing opportunities..."):

        prompt = f"""
        You are an elite global labor market analyst,
        hiring manager,
        remote work specialist,
        freelancing strategist,
        and workforce researcher.

        Analyze opportunities for:

        ROLE: {role}

        Requirements:

        1. Explain current market outlook.
        2. Suggest entry-level jobs.
        3. Suggest internship opportunities.
        4. Suggest remote jobs.
        5. Suggest freelancing opportunities.
        6. Suggest AI-resistant opportunities.
        7. Suggest portfolio requirements.
        8. Suggest networking strategy.
        9. Suggest LinkedIn strategy.
        10. Suggest first-income strategy.
        11. Estimate salary range.
        12. Mention future demand.

        Return ONLY JSON.

        {{
            "market_outlook":"",
            "entry_roles":[],
            "internships":[],
            "remote_jobs":[],
            "freelancing":[],
            "ai_resistant_roles":[],
            "portfolio_requirements":[],
            "linkedin_strategy":[],
            "networking_strategy":[],
            "first_income_plan":[],
            "salary_range":"",
            "future_demand":""
        }}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        text = text.replace(
            "```json", ""
        ).replace(
            "```", ""
        )

        try:
            data = json.loads(text)

        except Exception:
            st.error("AI returned invalid JSON.")
            st.code(text)
            st.stop()

        st.subheader("📈 Market Outlook")
        st.write(data["market_outlook"])

        st.subheader("🚀 Entry-Level Roles")
        for item in data["entry_roles"]:
            st.write("•", item)

        st.subheader("🎓 Internships")
        for item in data["internships"]:
            st.write("•", item)

        st.subheader("🌍 Remote Jobs")
        for item in data["remote_jobs"]:
            st.write("•", item)

        st.subheader("💰 Freelancing Opportunities")
        for item in data["freelancing"]:
            st.write("•", item)

        st.subheader("🛡 AI-Resistant Opportunities")
        for item in data["ai_resistant_roles"]:
            st.write("•", item)

        st.subheader("🛠 Portfolio Requirements")
        for item in data["portfolio_requirements"]:
            st.write("•", item)

        st.subheader("💼 LinkedIn Strategy")
        for item in data["linkedin_strategy"]:
            st.write("•", item)

        st.subheader("🤝 Networking Strategy")
        for item in data["networking_strategy"]:
            st.write("•", item)

        st.subheader("💵 First Income Strategy")
        for item in data["first_income_plan"]:
            st.write("•", item)

        st.subheader("📊 Future Demand")
        st.write(data["future_demand"])

        st.success(
            f"Estimated Salary Range: {data['salary_range']}"
        )