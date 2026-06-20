import os

import pandas as pd
import plotly.express as px
import requests
import streamlit as st

# --------------------------------------------------
# Configuration
# --------------------------------------------------

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)

GENERATE_URL = f"{API_URL}/generate"
HEALTH_URL = f"{API_URL}/health"

st.set_page_config(
    page_title="AI SQL Generator",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("🤖 AI SQL Generator")

    st.markdown("---")

    st.subheader("Features")

    st.success("RAG Search")
    st.success("Oracle SQL")
    st.success("FastAPI")
    st.success("Groq LLM")
    st.success("Interactive Charts")
    st.success("CSV Export")

    st.markdown("---")

    st.subheader("API Status")

    try:

        health = requests.get(
            HEALTH_URL,
            timeout=5
        )

        if health.status_code == 200:

            st.success("🟢 API Online")

        else:

            st.error("🔴 API Unhealthy")

    except Exception:

        st.error("🔴 API Offline")

    st.markdown("---")

    st.caption("API Base URL")

    st.code(API_URL)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🤖 AI SQL Generator")

st.write(
    "Generate Oracle SQL using Natural Language."
)

# --------------------------------------------------
# User Question
# --------------------------------------------------

question = st.text_area(
    "Enter your question",
    height=120,
    placeholder="Example: Show total sales by country"
)

# --------------------------------------------------
# Generate SQL
# --------------------------------------------------

if st.button(
    "🚀 Generate SQL",
    width="stretch"
):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Generating SQL..."
        ):

            try:

                response = requests.post(
                    GENERATE_URL,
                    json={
                        "question": question
                    },
                    timeout=120
                )

                if response.status_code == 200:

                    st.session_state["result"] = (
                        response.json()
                    )

                else:

                    st.error(
                        f"API Error ({response.status_code})"
                    )

                    st.code(
                        response.text
                    )

            except requests.exceptions.Timeout:

                st.error(
                    "The request timed out."
                )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Unable to connect to the API."
                )

            except Exception as ex:

                st.error(
                    str(ex)
                )

# --------------------------------------------------
# Display Results
# --------------------------------------------------

if "result" in st.session_state:

    result = st.session_state["result"]

    st.success(
        "SQL Generated Successfully"
    )

    # ----------------------------------------------

    st.subheader(
        "Generated SQL"
    )

    st.code(
        result["sql"],
        language="sql"
    )

    # ----------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Execution Time",
            f"{result['execution_time']} sec"
        )

    with col2:

        st.metric(
            "Rows Returned",
            result["row_count"]
        )

    # ----------------------------------------------

    df = pd.DataFrame(
        result["results"]
    )

    st.subheader(
        "Query Results"
    )

    st.dataframe(
        df,
        width="stretch"
    )

    # ----------------------------------------------
    # Visualization
    # ----------------------------------------------

    if len(df.columns) >= 2:

        st.subheader(
            "Visualization"
        )

        chart_type = st.selectbox(
            "Select Chart Type",
            [
                "Bar Chart",
                "Line Chart",
                "Pie Chart"
            ]
        )

        x_column = df.columns[0]
        y_column = df.columns[1]

        if chart_type == "Bar Chart":

            fig = px.bar(
                df,
                x=x_column,
                y=y_column,
                title="Bar Chart"
            )

        elif chart_type == "Line Chart":

            fig = px.line(
                df,
                x=x_column,
                y=y_column,
                markers=True,
                title="Line Chart"
            )

        else:

            fig = px.pie(
                df,
                names=x_column,
                values=y_column,
                title="Pie Chart"
            )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # ----------------------------------------------
    # Export
    # ----------------------------------------------

    st.subheader(
        "Export Results"
    )

    csv = df.to_csv(
        index=False
    ).encode(
        "utf-8"
    )

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name="results.csv",
        mime="text/csv",
        width="stretch"
    )

# --------------------------------------------------
# Example Questions
# --------------------------------------------------

st.subheader(
    "Example Questions"
)

st.markdown(
"""
- Show total sales by country

- Top 10 customers

- Monthly revenue

- Sales by product line

- Highest selling products

- Total sales by year

- Top 5 products

- Average sales by country

- Orders by status

- Total sales by year and country

- Show customers from USA

- Average sales per product line
"""
)