import streamlit as st
from multiapp import MultiApp
from apps import (
    basemaps,
    census,
    wms,
    xy,
)

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here

apps.add_app("Home", home.app)
apps.add_app("Create Timelapse", timelapse.app)
apps.add_app("U.S. Real Estate Data", housing.app)
apps.add_app("U.S. Census Data", census.app)
apps.add_app("Cesium 3D Map", cesium.app)
apps.add_app("Plotly", plotly_maps.app)
apps.add_app("Demo", demo.app)

# The main app
apps.run()
