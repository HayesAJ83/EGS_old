import streamlit as st
from multiapp import MultiApp
from apps import (
    home,
    plotly_maps,
    gallbladder,
    xy,
)

st.set_page_config(layout="wide")

apps = MultiApp()

# Add all your application here
apps.add_app("Home", home.app)
apps.add_app("Surgical Emergency Flow", xy.app)
apps.add_app("Emergency Gallbladder", gallbladder.app)
apps.add_app("Plotly", plotly_maps.app)

# The main app
apps.run()
