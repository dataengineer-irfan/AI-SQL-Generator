import streamlit as st
import requests

st.set_page_config(
    page_title="AI SQL Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI SQL Generator")

st.write(
    "Generate Oracle SQL using Natural Language."
)

question = st.text_area(
    "Enter your question",
    height=120
)

if st.button("Generate SQL"):

    if question.strip():

        with st.spinner("Generating SQL..."):

            response = requests.post(
                "http://127.0.0.1:8000/generate",
                json={
                    "question": question
                }
            )

            if response.status_code == 200:

                result = response.json()

                st.success("SQL Generated")

                st.subheader("SQL")

                st.code(
                    result["sql"],
                    language="sql"
                )

                st.metric(
                    "Execution Time",
                    f"{result['execution_time']} sec"
                )

            else:

                st.error(
                    "API Error"
                )
with st.sidebar:

    st.title("AI SQL Generator")

    st.markdown("---")

    st.write("Features")

    st.write("✅ RAG")

    st.write("✅ Dataset Search")

    st.write("✅ Oracle SQL")

    st.write("✅ FastAPI")

    st.write("✅ Groq LLM")
st.subheader("Example Questions")

st.markdown("""
- Show total sales by country

- Top 10 customers

- Monthly revenue

- Sales by product line

- Highest selling products
""")    