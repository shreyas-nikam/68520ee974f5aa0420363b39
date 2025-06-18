
import streamlit as st
import pandas as pd
import plotly.express as px

def run_risk_assessment():
    st.header("AI-Q Score Risk Assessment")
    st.markdown("Enter your information to calculate your AI-Q Score.")

    with st.form("risk_assessment"):
        occupation = st.text_input("Occupation")
        education_level = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
        company_stability = st.slider("Company Stability (1-10)", 1, 10)
        upskilling_level = st.slider("Upskilling Efforts (1-10)", 1, 10)
        submitted = st.form_submit_button("Calculate Risk")

    if submitted:
        # Calculate risk scores (replace with actual calculation logic)
        systematic_risk = calculate_systematic_risk(occupation)
        idiosyncratic_risk = calculate_idiosyncratic_risk(education_level, company_stability, upskilling_level)
        ai_q_score = systematic_risk + idiosyncratic_risk

        # Create a Pandas DataFrame for the bar chart
        data = {'Risk Component': ['Systematic Risk', 'Idiosyncratic Risk'],
                'Score': [systematic_risk, idiosyncratic_risk]}
        df = pd.DataFrame(data)

        # Create the bar chart using Plotly
        fig = px.bar(df, x='Risk Component', y='Score', title='AI-Q Risk Breakdown')
        st.plotly_chart(fig)

        # Simulation example
        upskilling_change = st.slider("Adjust Upskilling Level", 1, 10, upskilling_level, key="upskilling_slider")
        new_idiosyncratic_risk = calculate_idiosyncratic_risk(education_level, company_stability, upskilling_change)
        mitigation_data = {'Risk Component': ['Systematic Risk', 'Idiosyncratic Risk (Original)', 'Idiosyncratic Risk (Mitigated)'],
                        'Score': [systematic_risk, idiosyncratic_risk, new_idiosyncratic_risk]}
        mitigation_df = pd.DataFrame(mitigation_data)
        mitigation_fig = px.bar(mitigation_df, x='Risk Component', y='Score', title='Risk Mitigation Simulation')
        st.plotly_chart(mitigation_fig)

        st.write(f"AI-Q Score: {ai_q_score}")

    def calculate_systematic_risk(occupation):
        # This is a placeholder; in a real application, it would use a more complex calculation.
        risk_mapping = {
            "Data Entry Clerk": 80,
            "Software Engineer": 30,
            "Senior Research Scientist": 10,
            "Paralegal": 65 #from the attached document
        }

        #If the input does not match return a neutral value to avoid an error
        return risk_mapping.get(occupation,50)

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
