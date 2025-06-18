
import streamlit as st
import pandas as pd
import plotly.express as px

def run_idiosyncratic_risk():
    st.header("Idiosyncratic Risk Breakdown")
    st.markdown("Understand how your individual characteristics contribute to your AI-Q Score.")

    education_level = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
    company_stability = st.slider("Company Stability (1-10)", 1, 10)
    upskilling_level = st.slider("Upskilling Efforts (1-10)", 1, 10)

    # Idiosyncratic Risk calculation (same as in risk_assessment.py)
    def calculate_idiosyncratic_risk(education, stability, upskilling):
        # Education Level Factor (Simplified)
        education_factor = {
            "High School": 70,
            "Bachelor's": 50,
            "Master's": 30,
            "PhD": 10
        }[education]

        # Combine factors (Simplified - adjust as needed)
        risk = education_factor + (10 - stability) * 5 + (10 - upskilling) * 2
        return risk

    idiosyncratic_risk = calculate_idiosyncratic_risk(education_level, company_stability, upskilling_level)

    st.write(f"Idiosyncratic Risk: {idiosyncratic_risk}")

    data = {'Risk Component': ['Idiosyncratic Risk'],
            'Score': [idiosyncratic_risk]}
    df = pd.DataFrame(data)

    fig = px.bar(df, x='Risk Component', y='Score', title='Idiosyncratic Risk Breakdown')

    st.plotly_chart(fig)

    st.markdown("Idiosyncratic risk represents your individual vulnerability to AI-driven job displacement. Factors like education, company stability, and upskilling efforts can significantly influence this risk.")
    st.markdown("The risk is calculated as follows (placeholder):")
    st.markdown("Consult the documentation for detailed formula of Idiosyncratic Risk")


