# application_pages/risk_assessment.py

import streamlit as st
import pandas as pd
import plotly.express as px

def run_risk_assessment():
    st.header("AI-Q Score Risk Assessment")
    st.markdown("Enter your information to calculate your AI-Q Score.")

    # Initialize session state if not exists
    if 'last_submitted' not in st.session_state:
        st.session_state.last_submitted = {
            'occupation': '',
            'education_level': '',
            'company_stability': 1,
            'upskilling_level': 1,
            'systematic_risk': 0,
            'idiosyncratic_risk': 0,
            'ai_q_score': 0
        }

    def calculate_systematic_risk(occupation):
        risk_mapping = {
            "Data Entry Clerk": 80,
            "Software Engineer": 30,
            "Senior Research Scientist": 10,
            "Paralegal": 65
        }
        return risk_mapping.get(occupation, 50)

    def calculate_idiosyncratic_risk(education, stability, upskilling):
        education_factor = {
            "High School": 70,
            "Bachelor's": 50,
            "Master's": 30,
            "PhD": 10
        }[education]
        return education_factor + (10 - stability) * 5 + (10 - upskilling) * 2

    with st.form("risk_assessment"):
        occupation = st.text_input("Occupation")
        education_level = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
        company_stability = st.slider("Company Stability (1-10)", 1, 10)
        upskilling_level = st.slider("Upskilling Efforts (1-10)", 1, 10)
        submitted = st.form_submit_button("Calculate Risk")

    if submitted:
        # Calculate risk scores
        systematic_risk = calculate_systematic_risk(occupation)
        idiosyncratic_risk = calculate_idiosyncratic_risk(education_level, company_stability, upskilling_level)
        ai_q_score = systematic_risk + idiosyncratic_risk

        # Store the submitted values
        st.session_state.last_submitted = {
            'occupation': occupation,
            'education_level': education_level,
            'company_stability': company_stability,
            'upskilling_level': upskilling_level,
            'systematic_risk': systematic_risk,
            'idiosyncratic_risk': idiosyncratic_risk,
            'ai_q_score': ai_q_score
        }

    # Show charts if we have data
    if st.session_state.last_submitted['systematic_risk'] > 0:
        # Create a Pandas DataFrame for the initial bar chart
        data = {'Risk Component': ['Systematic Risk', 'Idiosyncratic Risk'],
                'Score': [st.session_state.last_submitted['systematic_risk'], 
                         st.session_state.last_submitted['idiosyncratic_risk']]}
        df = pd.DataFrame(data)

        # Create the bar chart using Plotly
        fig = px.bar(df, x='Risk Component', y='Score', title='AI-Q Risk Breakdown')
        st.plotly_chart(fig)

        # Show simulation slider and updated chart
        upskilling_change = st.slider(
            "Adjust Upskilling Level", 
            1, 10, 
            st.session_state.last_submitted['upskilling_level'],
            key="upskilling_slider"
        )
        
        new_idiosyncratic_risk = calculate_idiosyncratic_risk(
            st.session_state.last_submitted['education_level'],
            st.session_state.last_submitted['company_stability'],
            upskilling_change
        )
        
        mitigation_data = {
            'Risk Component': ['Systematic Risk', 'Idiosyncratic Risk (Original)', 'Idiosyncratic Risk (Mitigated)'],
            'Score': [
                st.session_state.last_submitted['systematic_risk'],
                st.session_state.last_submitted['idiosyncratic_risk'],
                new_idiosyncratic_risk
            ]
        }
        mitigation_df = pd.DataFrame(mitigation_data)
        mitigation_fig = px.bar(mitigation_df, x='Risk Component', y='Score', title='Risk Mitigation Simulation')
        st.plotly_chart(mitigation_fig)

        # Show the original AI-Q Score
        st.success(f"AI-Q Score: {st.session_state.last_submitted['ai_q_score']}")
        
        # Show the new potential score
        new_score = st.session_state.last_submitted['systematic_risk'] + new_idiosyncratic_risk
        st.info(f"Potential AI-Q Score after upskilling adjustment: {new_score}")
