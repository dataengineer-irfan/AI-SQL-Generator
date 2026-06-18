import streamlit as st


class Sidebar:

    @staticmethod
    def show():

        st.sidebar.title(
            "🤖 AI SQL Generator"
        )

        st.sidebar.markdown(
            "---"
        )

        page = st.sidebar.radio(

            "Navigation",

            [

                "SQL Generator",

                "Query History",

                "Performance",

                "About"

            ]

        )

        st.sidebar.markdown(
            "---"
        )

        st.sidebar.caption(
            "Version 1.0.0"
        )

        return page
