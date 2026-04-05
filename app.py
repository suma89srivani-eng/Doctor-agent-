import streamlit as st
from utils.symptom_checker import analyze_symptoms
from utils.triage import get_triage_level
from utils.specialist import suggest_specialist

st.set_page_config(page_title="Doctor Agent", page_icon="🩺", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
        .main-title {
            font-size: 3rem;
            font-weight: 800;
            color: white;
        }
        .hero-box {
            background: linear-gradient(90deg, #102b6a, #2d63ff);
            padding: 2rem;
            border-radius: 25px;
            color: white;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.12);
        }
        .feature-card {
            background-color: #ffffff;
            padding: 1.5rem;
            border-radius: 20px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
            border: 1px solid #e8edf5;
            min-height: 220px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
<div class="hero-box">
    <div class="main-title">🩺 Doctor Agent</div>
    <p style="font-size: 1.2rem; margin-top: 1rem;">
        A smart symptom checker that performs preliminary health triage,
        estimates urgency, suggests possible conditions, and recommends
        the right specialist.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# --- Features ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h2>🧠 Smart Symptom Analysis</h2>
        <p>Understands symptom keywords and extracts likely health indicators.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h2>⚡ Urgency Triage</h2>
        <p>Detects whether symptoms may need routine care, early consultation, or urgent help.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h2>👨‍⚕️ Specialist Guidance</h2>
        <p>Suggests which type of doctor may be most relevant for the symptoms entered.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# --- Input ---
st.subheader("📝 Describe Your Symptoms")
user_input = st.text_area(
    "Enter your symptoms below:",
    placeholder="Example: I have fever, cough, and headache for 2 days..."
)

if st.button("Analyze Symptoms"):
    if user_input.strip():
        conditions = analyze_symptoms(user_input)
        triage = get_triage_level(user_input)
        specialist = suggest_specialist(user_input)

        st.subheader("📋 Preliminary Analysis")
        st.write("### Possible Conditions")
        for condition in conditions:
            st.write(f"- {condition}")

        st.write("### Urgency Level")
        st.success(triage)

        st.write("### Recommended Specialist")
        st.info(f"👨‍⚕️ {specialist}")

        st.warning(
            "⚠️ This is not a medical diagnosis. Please consult a licensed doctor for proper evaluation."
        )
    else:
        st.error("Please enter your symptoms first.")
