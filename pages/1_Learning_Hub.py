import streamlit as st
import json
from gemini_config import client

st.set_page_config(page_title="Learning Hub", page_icon="📚", layout="wide")

st.title("📚 AI Learning Hub")

role = st.text_input(
    "Target Role",
    placeholder="e.g., Data Analyst, QA Engineer, DevOps Specialist"
)

if st.button("Generate Learning Plan"):
    # ১. খালি ইনপুট গার্ড রেল
    if not role.strip():
        st.warning("⚠️ Please provide a target market role to initialize the graph.")
        st.stop()

    with st.spinner("🧠 Connecting to Gemini Cloud & Building your Roadmap..."):
        prompt = f"""
        You are an elite global career strategist and hiring manager.
        Create a complete employability roadmap for a student who wants to become a:
        ROLE: {role}

        Requirements: Provide exhaustive actionable parameters for all requested nodes.
        """

        try:
            # ২. OPTIMIZED: Strict JSON Response Mode Setup
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config={
                    "response_mime_type": "application/json", # গুগলের সার্ভারকে বাধ্য করা হচ্ছে শুধু JSON দিতে
                }
            )

            # সরাসরি খাঁটি JSON লোড করা হচ্ছে, কোনো স্ট্রিং রিপ্লেসের ঝামেলা নেই
            data = json.loads(response.text.strip())

        except Exception as e:
            st.error("🚨 Cloud Node Synch Error. AI returned an unparsable block. Please retry.")
            st.code(response.text if 'response' in locals() else str(e))
            st.stop()

        # ৩. RENDER COMPONENT INTERFACE
        st.success("✨ Roadmap Synthesized Successfully!")
        st.markdown("---")

        # Layout Column split for beautiful visual architecture
        col_main1, col_main2 = st.columns([1, 1])

        with col_main1:
            st.subheader("🌍 Role Overview")
            st.info(data.get("role_overview", "N/A"))

            st.subheader("📈 Market Demand")
            st.write(data.get("market_demand", "N/A"))

            st.subheader("🟢 Beginner Skills")
            for item in data.get("beginner_skills", []):
                st.markdown(f"- {item}")

            st.subheader("🟡 Intermediate Skills")
            for item in data.get("intermediate_skills", []):
                st.markdown(f"- {item}")

            st.subheader("🔴 Advanced Skills")
            for item in data.get("advanced_skills", []):
                st.markdown(f"- {item}")

            st.subheader("🤖 AI Tools")
            for item in data.get("ai_tools", []):
                st.markdown(f"- {item}")

        with col_main2:
            st.subheader("🛠️ Portfolio Projects")
            for item in data.get("projects", []):
                st.markdown(f"- {item}")

            st.subheader("📜 Certifications")
            for item in data.get("certifications", []):
                st.markdown(f"- {item}")

            st.subheader("🎥 YouTube Resources")
            for item in data.get("youtube_resources", []):
                st.markdown(f"- {item}")

            st.subheader("💼 LinkedIn Strategy")
            for item in data.get("linkedin_strategy", []):
                st.markdown(f"- {item}")

            st.subheader("🚀 Internship Strategy")
            for item in data.get("internship_strategy", []):
                st.markdown(f"- {item}")

            st.subheader("⚠ Common Mistakes")
            for item in data.get("common_mistakes", []):
                st.markdown(f"- {item}")

            st.subheader("📅 Learning Timeline")
            for item in data.get("timeline", []):
                st.markdown(f"- {item}")