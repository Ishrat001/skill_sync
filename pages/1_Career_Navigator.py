import streamlit as st
from google import genai
import json

# =========================================
# FIXED GEMINI API
# =========================================


client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)


# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="SkillSync AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# MODERN UI CSS
# =========================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main {
    background: linear-gradient(180deg, #0b1020 0%, #111827 100%);
    color: #f8fafc;
}

section[data-testid="stSidebar"] {
    background: #0f172a;
    border-right: 1px solid #1e293b;
}

.block-container {
    padding-top: 2rem;
}

.hero-card {
    background: linear-gradient(135deg, #111827 0%, #1e293b 100%);
    padding: 32px;
    border-radius: 22px;
    border: 1px solid #334155;
    margin-bottom: 20px;
}

.glass-card {
    background: rgba(15, 23, 42, 0.9);
    padding: 24px;
    border-radius: 20px;
    border: 1px solid #334155;
    margin-bottom: 20px;
    backdrop-filter: blur(10px);
}

.metric-value {
    font-size: 38px;
    font-weight: 800;
    color: #38bdf8;
}

.metric-label {
    color: #94a3b8;
    font-size: 14px;
}

.red {
    color: #f43f5e;
}

.green {
    color: #22c55e;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 14px;
    font-size: 16px;
    font-weight: 700;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0px 10px 25px rgba(37,99,235,0.35);
}

input, textarea {
    border-radius: 12px !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    st.title("🎯 SkillSync AI")
    st.caption("AI-Powered Career Intelligence Platform")

    st.markdown("---")

    app_mode = st.radio(
        "Workspace",
        [
            "🔮 AI Career Navigator",
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

# =========================================
# MAIN APP
# =========================================

if app_mode == "🔮 AI Career Navigator":

    st.markdown("""
    <div class='hero-card'>
        <h1>🎯 AI Career Navigator</h1>
        <p style='font-size:18px;color:#cbd5e1;'>
        Analyze your academic background, discover future-proof career paths,
        identify missing market skills, and generate a personalized roadmap
        toward global remote opportunities.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "Full Name",
            placeholder="Your name"
        )

        degree = st.text_input(
            "Academic Background / Degree",
            placeholder="e.g. CSE, English, Zoology, BBA"
        )

    with col2:

        target_role = st.text_input(
            "Dream Career / Target Role",
            placeholder="e.g. AI Engineer, Data Analyst, UI/UX Designer"
        )

        skills_raw = st.text_area(
            "Current Skills / Experience / Interests",
            placeholder="e.g. Python, Canva, Writing, Research, Public Speaking"
        )

    if st.button("🚀 Generate AI Career Analysis"):

        if not degree or not target_role or not skills_raw:

            st.warning("Please complete all required fields.")

        else:

            with st.spinner("Generating personalized analysis..."):

                try:

                    prompt = f"""
                    You are an elite global career strategist, labor market analyst,
                    AI-powered HR consultant, EdTech mentor, startup advisor,
                    and future-of-work researcher.

                    Analyze the following student profile deeply and realistically.

                    STUDENT DATA:
                    Name: {name}
                    Academic Background: {degree}
                    Target Career: {target_role}
                    Current Skills/Interests: {skills_raw}

                    Your responsibilities:

                    1. Analyze current global job market trends.
                    2. Evaluate employability potential.
                    3. Identify academic strengths.
                    4. Detect missing industry-ready skills.
                    5. Suggest future-proof career paths.
                    6. Recommend beginner-friendly skills.
                    7. Recommend high-income remote work opportunities.
                    8. Suggest realistic project ideas.
                    9. Suggest portfolio-building strategies.
                    10. Recommend YouTube learning resources.
                    11. Generate a personalized multi-step roadmap.
                    12. Estimate market readiness percentage realistically.
                    13. Be brutally practical and realistic.
                    14. Focus on modern AI-era job market.
                    15. Avoid generic motivational language.

                    IMPORTANT:
                    Return ONLY valid raw JSON.
                    No markdown.
                    No explanation.
                    No extra text.

                    JSON FORMAT:

                    {{
                        "match_score": 65,
                        "gap_score": 35,

                        "career_paths": [
                            "AI Content Strategist",
                            "Digital Marketing Specialist",
                            "Remote Research Assistant"
                        ],

                        "market_insights": [
                            "Remote AI-assisted jobs are growing rapidly",
                            "Communication + AI tools is becoming highly valuable"
                        ],

                        "matched_assets": [
                            "Communication",
                            "Research",
                            "Writing"
                        ],

                        "missing_parameters": [
                            "Excel",
                            "SEO",
                            "AI Tools",
                            "Portfolio Projects"
                        ],

                        "recommended_skills": [
                            "Canva",
                            "ChatGPT Prompting",
                            "Excel",
                            "Digital Marketing",
                            "Notion"
                        ],

                        "project_ideas": [
                            "Create a personal portfolio website",
                            "Build a content strategy case study",
                            "Create AI-assisted blog articles"
                        ],

                        "remote_opportunities": [
                            "Freelance Content Writing",
                            "Remote Research Assistant",
                            "Virtual Assistant"
                        ],

                        "youtube_courses": [
                            {{
                                "title": "Complete Digital Marketing Course",
                                "link": "https://youtube.com/"
                            }},
                            {{
                                "title": "ChatGPT Masterclass",
                                "link": "https://youtube.com/"
                            }}
                        ],

                        "sprints": [
                            {{
                                "title": "Foundation Building",
                                "focus": "Learn essential digital and AI skills"
                            }},
                            {{
                                "title": "Portfolio Development",
                                "focus": "Build practical projects and online presence"
                            }},
                            {{
                                "title": "Monetization",
                                "focus": "Apply for internships and remote opportunities"
                            }}
                        ]
                    }}
                    """

                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt
                    )

                    raw_text = response.text.strip()

                    if raw_text.startswith("```json"):
                        raw_text = raw_text.replace("```json", "").replace("```", "").strip()

                    elif raw_text.startswith("```"):
                        raw_text = raw_text.replace("```", "").strip()

                    data = json.loads(raw_text)

                    # =========================================
                    # RESULT SECTION
                    # =========================================

                    st.markdown(f"## 📊 Career Intelligence Report for {name}")

                    c1, c2, c3 = st.columns(3)

                    with c1:
                        st.markdown(f"""
                        <div class='glass-card'>
                            <div class='metric-label'>🎯 Career Match</div>
                            <div class='metric-value'>{data['match_score']}%</div>
                        </div>
                        """, unsafe_allow_html=True)

                    with c2:
                        st.markdown(f"""
                        <div class='glass-card'>
                            <div class='metric-label'>🚨 Skill Gap</div>
                            <div class='metric-value red'>{data['gap_score']}%</div>
                        </div>
                        """, unsafe_allow_html=True)

                    with c3:
                        st.markdown(f"""
                        <div class='glass-card'>
                            <div class='metric-label'>💼 Recommended Role</div>
                            <div class='metric-value' style='font-size:22px;'>
                                {data['career_paths'][0]}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                    st.progress(data['match_score'] / 100)

                    st.markdown("## 💡 Market Insights")

                    for item in data["market_insights"]:
                        st.write(f"• {item}")

                    st.markdown("## 🧠 Recommended Career Paths")

                    for item in data["career_paths"]:
                        st.write(f"• {item}")

                    st.markdown("## ✅ Existing Strengths")

                    for item in data["matched_assets"]:
                        st.write(f"• {item}")

                    st.markdown("## ❌ Missing Industry Skills")

                    for item in data["missing_parameters"]:
                        st.write(f"• {item}")

                    st.markdown("## 🚀 Recommended Skills To Learn")

                    for item in data["recommended_skills"]:
                        st.write(f"• {item}")

                    st.markdown("## 🛠️ Project Ideas")

                    for item in data["project_ideas"]:
                        st.write(f"• {item}")

                    st.markdown("## 🌍 Remote Opportunities")

                    for item in data["remote_opportunities"]:
                        st.write(f"• {item}")

                    st.markdown("## 🎥 YouTube Learning Resources")

                    for course in data["youtube_courses"]:
                        st.markdown(
                            f"- [{course['title']}]({course['link']})"
                        )

                    st.markdown("## 🗺️ Personalized Growth Roadmap")

                    for idx, sprint in enumerate(data["sprints"]):

                        with st.expander(
                            f"🚀 Phase {idx+1}: {sprint['title']}",
                            expanded=True
                        ):
                            st.write(sprint['focus'])

                except Exception as e:

                    st.error(f"Error: {str(e)}")