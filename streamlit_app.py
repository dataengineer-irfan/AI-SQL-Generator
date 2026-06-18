import streamlit as st

from ui.sidebar import Sidebar


st.set_page_config(
    page_title="AI SQL Generator",
    page_icon="🤖",
    layout="wide"
)

page = Sidebar.show()

st.title(page)

if page == "SQL Generator":
    st.write(
        "SQL Generator Page"
    )

elif page == "Query History":
    st.write(
        "History Page"
    )

elif page == "Performance":
    st.write(
        "Performance Page"
    )

else:
    st.write(
        """
AI SQL Generator

Built using

• FastAPI

• Streamlit

• Oracle

• RAG

• Groq LLM
"""
    )
