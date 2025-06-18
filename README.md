
# AI-Q Score Streamlit Application

This Streamlit application calculates an AI-Q Score to help users understand their potential job displacement risk due to AI.

## How to Run

1.  Make sure you have Docker installed.
2.  Clone this repository.
3.  Build the Docker image: `docker build -t ai-q-score .`
4.  Run the Docker container: `docker run -p 8501:8501 ai-q-score`
5.  Open your browser and go to `http://localhost:8501`.

## Application Pages

*   **Risk Assessment:** Calculate your overall AI-Q Score.
*   **Systematic Risk Deep Dive:** Explore the systematic risk associated with different occupations.
*   **Idiosyncratic Risk Breakdown:** Understand how your individual characteristics contribute to your AI-Q Score.

## License

© 2025 QuantUniversity. All Rights Reserved.
