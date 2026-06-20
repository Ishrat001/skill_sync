import streamlit as st
import json
from gemini_config import client

st.set_page_config(page_title="Interview Coach")

st.title("🎤 AI Interview Coach")

role = st.text_input(
    "Target Role",
    placeholder="Data Analyst"
)

if st.button("Generate Interview Question"):

    prompt = f"""
    Generate one realistic interview question
    for a beginner {role}.

    Return ONLY JSON.

    {{
        "question":""
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

        st.session_state["question"] = data["question"]

    except Exception:

        st.error(
            "Unable to generate question."
        )

if "question" in st.session_state:

    st.subheader("Interview Question")

    st.info(
        st.session_state["question"]
    )

    answer = st.text_area(
        "Your Answer"
    )

    if st.button("Evaluate Answer"):

        prompt = f"""
        Evaluate the following interview answer.

        Question:
        {st.session_state["question"]}

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
                "Unable to evaluate answer."
            )

            st.stop()

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Confidence",
                f"{data['confidence_score']}%"
            )

        with c2:
            st.metric(
                "Technical",
                f"{data['technical_score']}%"
            )

        with c3:
            st.metric(
                "Communication",
                f"{data['communication_score']}%"
            )

        st.subheader("📝 Feedback")

        for item in data["feedback"]:
            st.write("•", item)