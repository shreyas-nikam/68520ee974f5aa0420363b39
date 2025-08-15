id: 68520ee974f5aa0420363b39_documentation
summary: AI Risk Score Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# AI-Q Score Lab Codelab: Understanding and Mitigating Job Displacement Risk

This codelab guides you through the AI-Q Score Lab application, a tool designed to help individuals understand and assess their potential job displacement risk due to the rise of Artificial Intelligence.  We'll explore the application's features, underlying concepts, and how you can use it to simulate and mitigate your risk. The AI-Q score is a novel approach to quantifying the risk of job displacement due to AI by combining systematic and idiosyncratic risks. By understanding the components and levers that affect your risk, you can make informed decisions about your career path and upskilling efforts.

## Setting Up the Development Environment
Duration: 00:05

Before diving into the application's functionalities, ensure you have the following:

1.  **Python 3.7+:**  The application is built using Python.
2.  **Streamlit:** Install Streamlit using pip:

    ```bash
    pip install streamlit
    pip install pandas
    pip install plotly
    ```

3.  **Clone the Repository:** (If you have the code in a repository.)  Alternatively, create the files (`app.py`, and the files in `application_pages`) in a directory.

## Running the Application
Duration: 00:02

1.  **Navigate to the directory** containing the `app.py` file in your terminal.
2.  **Run the application:**

    ```bash
    streamlit run app.py
    ```

    This command will open the application in your web browser.

## Exploring the Main Application (`app.py`)
Duration: 00:10

The `app.py` file serves as the entry point for the Streamlit application. Let's break down its key components:

1.  **Import Statements:**

    ```python
    import streamlit as st
    ```

    This line imports the Streamlit library, which is essential for creating the user interface.

2.  **Page Configuration:**

    ```python
    st.set_page_config(page_title="AI Risk Score", layout="wide")
    ```

    Configures the page title and layout to enhance the user experience.

3.  **Sidebar Content:**

    ```python
    st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
    st.sidebar.divider()
    st.title("AI-Q Score Lab")
    st.divider()
    ```

    Adds a logo and title to the sidebar for branding and navigation.

4.  **Main Content - Introduction:**

    ```python
    st.markdown("""
    ### Welcome to the AI-Q Score Lab!

    This interactive application helps you understand and assess your potential job displacement risk due to the rise of Artificial Intelligence.
    ...
    """)
    ```

    This section provides an introduction to the application, explaining its purpose, key concepts (AI-Q Score, Systematic Risk, Idiosyncratic Risk), and how to use it. The use of `st.markdown` allows for formatted text, including headings, bold text, and lists.

    <aside class="positive">
    <b>Tip:</b> The introduction clearly defines the purpose and key concepts, which is crucial for user understanding.
    </aside>

5.  **Navigation with `st.selectbox`:**

    ```python
    page = st.sidebar.selectbox(label="Navigation", options=["Risk Assessment", "Systematic Risk Deep Dive", "Idiosyncratic Risk Breakdown"])
    ```

    This creates a dropdown menu in the sidebar that allows users to navigate between different sections of the application. This is a central piece in controlling which functionality is displayed.

6.  **Conditional Page Routing:**

    ```python
    if page == "Risk Assessment":
        from application_pages.risk_assessment import run_risk_assessment
        run_risk_assessment()
    elif page == "Systematic Risk Deep Dive":
        from application_pages.systematic_risk import run_systematic_risk
        run_systematic_risk()
    elif page == "Idiosyncratic Risk Breakdown":
        from application_pages.idiosyncratic_risk import run_idiosyncratic_risk
        run_idiosyncratic_risk()
    ```

    Based on the selected page from the `st.selectbox`, the corresponding function from the respective module in the `application_pages` directory is called.  This modular approach keeps the `app.py` file clean and organized.

7.  **Footer:**

    ```python
    st.divider()
    st.write("© 2025 QuantUniversity. All Rights Reserved.")
    st.caption("The purpose of this demonstration is solely for educational use and illustration. "
               "Any reproduction of this demonstration "
               "requires prior written consent from QuantUniversity.")
    ```

    Adds a footer with copyright information and a disclaimer.

## Understanding the `application_pages` Directory
Duration: 00:05

The `application_pages` directory contains the logic for each of the three main sections of the application:

*   `risk_assessment.py`:  Calculates and displays the overall AI-Q Score based on user inputs.
*   `systematic_risk.py`:  Focuses on the systematic risk component, allowing users to explore the risk associated with different occupations.
*   `idiosyncratic_risk.py`:  Breaks down the idiosyncratic risk component, showing how individual characteristics affect the overall score.

## Deep Dive: `risk_assessment.py` - The Risk Assessment Page
Duration: 00:15

This page allows users to input their information and calculate their AI-Q Score.

1.  **Import Statements:**

    ```python
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    ```

    Imports necessary libraries for Streamlit, data manipulation (Pandas), and creating interactive charts (Plotly).

2.  **`run_risk_assessment()` Function:**

    ```python
    def run_risk_assessment():
        st.header("AI-Q Score Risk Assessment")
        st.markdown("Enter your information to calculate your AI-Q Score.")

        with st.form("risk_assessment"):
            occupation = st.text_input("Occupation")
            education_level = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
            company_stability = st.slider("Company Stability (1-10)", 1, 10)
            upskilling_level = st.slider("Upskilling Efforts (1-10)", 1, 10)
            submitted = st.form_submit_button("Calculate Risk")
    ```

    This function defines the layout and functionality of the risk assessment page.  It uses a Streamlit form (`st.form`) to collect user inputs for occupation, education level, company stability, and upskilling efforts.  The `st.form_submit_button` triggers the risk calculation when clicked.

3.  **Risk Calculation and Visualization (Inside `if submitted:`):**

    ```python
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
    ```

    This section calculates the systematic and idiosyncratic risks based on user inputs (using placeholder functions), calculates the AI-Q score, and displays the results using a Plotly bar chart.  It also includes a simulation slider to adjust the upskilling level and see the impact on the idiosyncratic risk and overall risk mitigation.

4.  **`calculate_systematic_risk()` Function:**

    ```python
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
    ```

    This function calculates the systematic risk based on the user's occupation. **Note:** This is a placeholder function and uses a simple mapping.  A real-world application would use a more sophisticated model.

5.  **`calculate_idiosyncratic_risk()` Function:**

    ```python
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
    ```

    This function calculates the idiosyncratic risk based on the user's education level, company stability, and upskilling efforts.  Like the `calculate_systematic_risk()` function, this is a simplified placeholder.

## Examining `systematic_risk.py` - Systematic Risk Deep Dive
Duration: 00:10

This page allows users to explore the systematic risk associated with different occupations.

1.  **`run_systematic_risk()` Function:**

    ```python
    def run_systematic_risk():
        st.header("Systematic Risk Deep Dive")
        st.markdown("Explore the systematic risk associated with different occupations.")

        occupation = st.selectbox("Select Occupation", ["Data Entry Clerk", "Software Engineer", "Senior Research Scientist", "Paralegal", "Other"])

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
    ```

    This function presents a selectbox for choosing an occupation and then calculates and displays the corresponding systematic risk using the `calculate_systematic_risk()` function (defined identically as in `risk_assessment.py`). A bar chart visually represents the risk.

2.  **`calculate_systematic_risk()` Function:** (Same as in `risk_assessment.py`)

    This function is identical to the one in `risk_assessment.py` and provides the systematic risk score based on a predefined mapping.

## Analyzing `idiosyncratic_risk.py` - Idiosyncratic Risk Breakdown
Duration: 00:10

This page allows users to understand how their individual characteristics contribute to their AI-Q Score.

1.  **`run_idiosyncratic_risk()` Function:**

    ```python
    def run_idiosyncratic_risk():
        st.header("Idiosyncratic Risk Breakdown")
        st.markdown("Understand how your individual characteristics contribute to your AI-Q Score.")

        education_level = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
        company_stability = st.slider("Company Stability (1-10)", 1, 10)
        upskilling_level = st.slider("Upskilling Efforts (1-10)", 1, 10)

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
    ```

    This function provides input widgets (selectbox and sliders) for education level, company stability, and upskilling efforts.  It then calculates and displays the idiosyncratic risk using the `calculate_idiosyncratic_risk()` function (defined identically as in `risk_assessment.py`). A bar chart visually represents the risk.

2.  **`calculate_idiosyncratic_risk()` Function:** (Same as in `risk_assessment.py`)

    This function is identical to the one in `risk_assessment.py` and calculates the idiosyncratic risk score based on the user's inputs.

## Improving the Application
Duration: 00:30

This application serves as a great starting point. Here are some ways to improve it:

1.  **Implement More Realistic Risk Calculation:**  Replace the placeholder risk calculation functions with more sophisticated models that consider a wider range of factors and use real-world data. Consider using external APIs or datasets for occupation risk assessment.

2.  **Expand Occupation List:**  Provide a more comprehensive list of occupations in the `systematic_risk.py` page, potentially using a searchable dropdown or an API to fetch occupations.

3.  **Add Data Persistence:**  Implement a mechanism to save user inputs and risk scores, allowing users to track their progress over time.  Consider using Streamlit's session state or a database.

4.  **Enhance Visualization:** Explore more advanced Plotly chart types to provide a richer understanding of the risk components and mitigation strategies.

5.  **Incorporate User Feedback:** Add a feedback mechanism to collect user input and improve the application based on their needs.

6. **Detailed Documentation:** The current documentation mentions consulting documentation for detailed formulas. Creating a separate documentation page or expanding the existing markdown with detailed explanations of the formulas used for systematic and idiosyncratic risk calculation would significantly enhance the educational value of the application.  This should include the sources of the formulas and the underlying assumptions.

7. **Risk Factor Weights:** Allow the user to adjust the weights of different factors contributing to idiosyncratic risk (e.g., education, company stability, upskilling).  This would allow users to explore the sensitivity of their risk score to different factors.

## Conclusion

This codelab provided a comprehensive overview of the AI-Q Score Lab application. By understanding the application's architecture, functionalities, and underlying concepts, you are now equipped to use it effectively and contribute to its further development. The AI-Q score is a valuable tool for understanding and mitigating job displacement risk in the age of AI, and this application provides a user-friendly way to explore this concept.