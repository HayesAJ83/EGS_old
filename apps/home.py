import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Streamlit for Emergency General Surgery")

    st.markdown(
        """
        This multi-page web app functions to experiment with methods to visualize and more deeply understand emergency care pathways 
        interactive web apps created using [streamlit](https://streamlit.io) and open-source libraries, such as Plotly.
        This is an open-source project and you are very welcome to contribute your comments, questions, resources.

        """
    )

    st.info("Click on the left sidebar menu to navigate to the different apps.")


