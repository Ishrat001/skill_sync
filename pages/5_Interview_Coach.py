import streamlit as st
import json
from gemini_config import client

st.set_page_config(page_title="Interview Coach")

# =========================
# SESSION STATES
# =========================

if "question" not in st.session_state:
    st.session_state.question = None

if "role" not in st.session_state:
    st.session_state.role = ""

if "question_count" not in st.session_state:
    st.session_state.question_count = 0

# =========================
# SIDEBAR
# =========================

with st.sidebar:
    st.title("🎯 SkillSync AI")
    st.caption("AI-Powered Career Intelligence Platform")

    st.markdown("---")

    st.markdown("""
    ### 🚀 Venture Profile

    - **Startup:** SkillSync AI  
    - **Founders:** Ishrat & Nafisa  
    - **Department:** CSE, University of Dhaka  
    - **Mission:** Bridging academic knowledge with global employability
    """)

# =========================
# MAIN UI
# =========================

st.title("🎤 AI Interview Coach")

role = st.text_input(
    "Target Role",
    value=st.session_state.role,
    placeholder="Data Analyst"
)

# =========================
# START INTERVIEW
# =========================

if st.button("🚀 Start Interview"):

    st.session_state.role = role

    try:

        prompt = f"""
        Generate one realistic interview question
        for a beginner {role}.

        Return ONLY JSON.

        {{
            "question":""
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

        data = json.loads(text)

        st.session_state.question = data["question"]
        st.session_state.question_count = 1

        st.rerun()

    except Exception:

        st.error(
            "Unable to generate interview question."
        )

# =========================
# SHOW QUESTION
# =========================

if st.session_state.question:

    st.subheader(
        f"Question {st.session_state.question_count}"
    )

    st.info(
        st.session_state.question
    )

    answer = st.text_area(
        "Your Answer"
    )

    # =========================
    # EVALUATE ANSWER
    # =========================

    if st.button("✅ Evaluate Answer"):

        try:

            prompt = f"""
            Evaluate the following interview answer.

            Role:
            {st.session_state.role}

            Question:
            {st.session_state.question}

            Answer:
            {answer}

            Return ONLY JSON.

            {{
                "confidence_score":80,
                "technical_score":75,
                "communication_score":85,
                "feedback":[]
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

            data = json.loads(text)

        except Exception:

            st.error(
                "Unable to evaluate answer."
            )

            st.stop()

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Confidence",
                f"{data['confidence_score']}%"
            )

            st.progress(
                data["confidence_score"] / 100
            )

        with c2:

            st.metric(
                "Technical",
                f"{data['technical_score']}%"
            )

            st.progress(
                data["technical_score"] / 100
            )

        with c3:

            st.metric(
                "Communication",
                f"{data['communication_score']}%"
            )

            st.progress(
                data["communication_score"] / 100
            )

        st.subheader("📝 Feedback")

        for item in data["feedback"]:
            st.write(f"• {item}")

    # =========================
    # NEXT QUESTION
    # =========================

    if st.button("➡ Next Question"):

        try:

            prompt = f"""
            Generate another interview question
            for a beginner {st.session_state.role}.

            Make it different from previous questions.

            Return ONLY JSON.

            {{
                "question":""
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

            data = json.loads(text)

            st.session_state.question = data["question"]
            st.session_state.question_count += 1

            st.rerun()

        except Exception:

            st.error(
                "Unable to generate next question."
            )