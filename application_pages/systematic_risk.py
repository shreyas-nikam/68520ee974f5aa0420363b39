
import streamlit as st
import pandas as pd
import plotly.express as px

def run_systematic_risk():
    st.header("Systematic Risk Deep Dive")
    st.markdown("Explore the systematic risk associated with different occupations.")

    occupation = st.selectbox("Select Occupation", ["Data Entry Clerk", "Software Engineer", "Senior Research Scientist", "Paralegal", "Other"])

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

    if occupation == "Other":
        st.markdown("Since the occupation is not in the list, the risk will default to a base value. To see accurate values, select one of the other options.")
        systematic_risk = 50
    else:
        systematic_risk = calculate_systematic_risk(occupation)

    st.write(f"Systematic Risk for {occupation}: {systematic_risk}")

    data = {'Risk Component': ['Systematic Risk'],
            'Score': [systematic_risk]}
    df = pd.DataFrame(data)

    fig = px.bar(df, x='Risk Component', y='Score', title=f'Systematic Risk for {occupation}')
    st.plotly_chart(fig)

    st.markdown("Systematic risk represents the risk inherent to a particular occupation due to automation. This is influenced by factors like the routine nature of the tasks involved and the potential for AI to perform those tasks.")
    st.markdown("The risk is calculated as follows (placeholder):")
    st.markdown("Consult the documentation for detailed formula of Systematic Risk")

    
