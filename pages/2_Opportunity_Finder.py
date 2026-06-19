import streamlit as st
import json
from gemini_config import client

st.set_page_config(page_title="Opportunity Finder", page_icon="💼", layout="wide")

st.title("💼 Opportunity Finder")

role = st.text_input(
    "Target Role",
    placeholder="e.g., Data Analyst, Virtual Assistant, Technical Writer"
)

if st.button("Find Opportunities"):
    # ১. ফাঁকা ইনপুট গার্ড রেল
    if not role.strip():
        st.warning("⚠️ Please enter a target role to scan the global labor market.")
        st.stop()

    with st.spinner("🔍 Analyzing global market opportunities..."):
        prompt = f"""
        You are an elite global labor market analyst, hiring manager, remote work specialist, and workforce researcher.
        Analyze opportunities for:
        ROLE: {role}

        Requirements: Exhaustively analyze current outlook, entry paths, income milestones, and scalability metrics.
        """

        try:
            # ২. OPTIMIZED: Strict JSON Response Mode
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config={
                    "response_mime_type": "application/json",  # এপিআইকে বাধ্য করা হচ্ছে শুধু বিশুদ্ধ JSON দিতে
                }
            )

            # সরাসরি লোড, কোনো ট্রিপল ব্যাকটিক ক্লিনিংয়ের ঝামেলা নেই
            data = json.loads(response.text.strip())

        except Exception as e:
            st.error("🚨 System Synch Error. Unparsable payload returned. Please try again.")
            st.code(response.text if 'response' in locals() else str(e))
            st.stop()

        # ৩. RENDER INTERFACE (Beautiful Two-Column Grid Architecture)
        st.success("🎯 Market Architecture Scaled Successfully!")
        st.markdown("---")

        # সেলারি রেঞ্জটাকে একটু হাইলাইটেড কার্ড হিসেবে উপরে দেখানো হলো
        st.info(f"💰 **Estimated Global Salary Range:** {data.get('salary_range', 'N/A')}")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📈 Market Outlook")
            st.write(data.get("market_outlook", "N/A"))

            st.subheader("🚀 Entry-Level Roles")
            for item in data.get("entry_roles", []):
                st.markdown(f"- {item}")

            st.subheader("🎓 Internships")
            for item in data.get("internships", []):
                st.markdown(f"- {item}")

            st.subheader("🌍 Remote Jobs")
            for item in data.get("remote_jobs", []):
                st.markdown(f"- {item}")

            st.subheader("🛡️ AI-Resistant Opportunities")
            for item in data.get("ai_resistant_roles", []):
                st.markdown(f"- {item}")

        with col2:
            st.subheader("💰 Freelancing Opportunities")
            for item in data.get("freelancing", []):
                st.markdown(f"- {item}")

            st.subheader("🛠️ Portfolio Requirements")
            for item in data.get("portfolio_requirements", []):
                st.markdown(f"- {item}")

            st.subheader("💼 LinkedIn Strategy")
            for item in data.get("linkedin_strategy", []):
                st.markdown(f"- {item}")

            st.subheader("🤝 Networking Strategy")
            for item in data.get("networking_strategy", []):
                st.markdown(f"- {item}")

            st.subheader("💵 First Income Strategy")
            for item in data.get("first_income_plan", []):
                st.markdown(f"- {item}")

            st.subheader("📊 Future Demand")
            st.write(data.get("future_demand", "N/A"))