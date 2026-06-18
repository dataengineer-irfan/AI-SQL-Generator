import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI SQL Generator",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------

st.title("🤖 AI SQL Generator")

st.write(
    "Generate Oracle SQL using Natural Language."
)

# -----------------------------
# User Question
# -----------------------------

question = st.text_area(
    "Enter your question",
    height=120
)

# -----------------------------
# Generate SQL
# -----------------------------

if st.button("Generate SQL"):

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating SQL..."):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/generate",
                    json={
                        "question": question
                    }
                )

                if response.status_code == 200:

                    st.session_state["result"] = response.json()

                else:

                    st.error(
                        f"API Error : {response.text}"
                    )

            except Exception as e:

                st.error(str(e))

# -----------------------------
# Display Results
# -----------------------------

if "result" in st.session_state:

    result = st.session_state["result"]

    st.success("SQL Generated Successfully")

    st.subheader("Generated SQL")

    st.code(
        result["sql"],
        language="sql"
    )

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

    df = pd.DataFrame(
        result["results"]
    )

    st.subheader("Query Results")

    st.dataframe(
        df,
        use_container_width=True
    )

    # -----------------------------
    # Chart
    # -----------------------------

    if len(df.columns) >= 2:

        st.subheader("Visualization")

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

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        elif chart_type == "Line Chart":

            fig = px.line(
                df,
                x=x_column,
                y=y_column,
                markers=True,
                title="Line Chart"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        elif chart_type == "Pie Chart":

            fig = px.pie(
                df,
                names=x_column,
                values=y_column,
                title="Pie Chart"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # -----------------------------
    # CSV Download
    # -----------------------------

    st.subheader("Export")

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name="results.csv",
        mime="text/csv"
    )

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("AI SQL Generator")

    st.markdown("---")

    st.subheader("Features")

    st.write("✅ RAG")

    st.write("✅ Dataset Search")

    st.write("✅ Oracle SQL")

    st.write("✅ FastAPI")

    st.write("✅ Groq LLM")

# -----------------------------
# Example Questions
# -----------------------------

st.subheader("Example Questions")

st.markdown("""
- Show total sales by country

- Top 10 customers

- Monthly revenue

- Sales by product line

- Highest selling products

- Total sales by year

- Top 5 products

- Average sales by country

- Orders by status
""")