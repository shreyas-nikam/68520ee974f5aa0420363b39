
import streamlit as st

st.set_page_config(page_title="AI Risk Score", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("AI-Q Score Lab")
st.divider()

st.markdown("""
### Welcome to the AI-Q Score Lab!

This interactive application helps you understand and assess your potential job displacement risk due to the rise of Artificial Intelligence.
The AI-Q Score is a comprehensive metric, combining **Systematic Risk** (inherent to your occupation) and **Idiosyncratic Risk** (your personal vulnerability).

**Here's how it works:**

1.  **Input your information:** Provide details about your occupation, education, company stability, and upskilling efforts.
2.  **Calculate your AI-Q Score:** The application will calculate your overall risk score and break it down into its components.
3.  **Explore mitigation strategies:** Use the simulation tools to see how changes in your upskilling level or other factors can impact your risk.

**Key Concepts:**

*   **AI-Q Score:** A numerical representation of your overall risk (Systematic Risk + Idiosyncratic Risk).
*   **Systematic Risk:** The risk associated with your occupation due to AI automation.
*   **Idiosyncratic Risk:** Your individual vulnerability based on your human capital, employer's stability, and upskilling efforts.

**Definitions, Examples, and Formulae:**

*   **AI-Q Score:** A numerical representation of an individual's overall risk of job displacement due to AI.  It is the sum of Systematic and Idiosyncratic Risk.

    *   *Formula:*  AI-Q Score = Systematic Risk + Idiosyncratic Risk

*   **Systematic Risk ($H$ or $H_I$):** Represents the risk inherent to a particular occupation due to automation. This is a dynamic index reflecting the macro-level automation hazard of an occupation, modified by prevailing economic conditions and the velocity of AI innovation.

    *   *Example:* Jobs involving routine tasks have higher Systematic Risk.
    *   *Formula:*  See individual page for details.

*   **Idiosyncratic Risk ($V$ or $V_I$):** Represents the individual's specific vulnerability based on their human capital, employer's stability, and upskilling efforts. This is the granular, multi-factor assessment of an individual's vulnerability based on their specific human capital, their employer's stability, and their proactive upskilling efforts.

    *   *Example:* Individuals with higher education and more upskilling have lower Idiosyncratic Risk.
    *   *Formula:* See individual page for details.

* The concepts of **Systematic Risk** and **Idiosyncratic Risk** are referenced from the provided document "AI-Q Score: A Multi-Factor Parametric Framework for Quantifying and Mitigating AI-Driven Job Displacement Risk," highlighting the analogy between financial risk management and career risk management in the age of AI.
""")

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Risk Assessment", "Systematic Risk Deep Dive", "Idiosyncratic Risk Breakdown"])

if page == "Risk Assessment":
    from application_pages.risk_assessment import run_risk_assessment
    run_risk_assessment()
elif page == "Systematic Risk Deep Dive":
    from application_pages.systematic_risk import run_systematic_risk
    run_systematic_risk()
elif page == "Idiosyncratic Risk Breakdown":
    from application_pages.idiosyncratic_risk import run_idiosyncratic_risk
    run_idiosyncratic_risk()
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
