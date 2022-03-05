import streamlit as st
from multiapp import MultiApp
from apps import (
    basemaps,
    home,
    housing,
    plotly_maps,
    wms,
    xy,
)

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here

apps.add_app("Home", home.app)
apps.add_app("U.S. Real Estate Data", housing.app)
apps.add_app("Search Basemaps", basemaps.app)
apps.add_app("Add Points from XY", xy.app)
apps.add_app("Add Web Map Service (WMS)", wms.app)
apps.add_app("Plotly", plotly_maps.app)

# The main app
apps.run()
