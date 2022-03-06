import leafmap.foliumap as leafmap
import pandas as pd
import streamlit as st


def app():

    st.title("Surgical Admissions")

    sample_url = "https://raw.githubusercontent.com/HayesAJ83/EGS/main/data/unscheduled_all.csv"
    #"https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/world_cities.csv"
    url = st.text_input("Enter URL:", sample_url)
    m = leafmap.Map( center=[56.52, -3.4], zoom=8.32, locate_control=True, plugin_LatLngPopup=False)

    if url:

        try:
            df = pd.read_csv(url)

            columns = df.columns.values.tolist()
            row1_col1, row1_col2, row1_col3, row1_col4, row1_col5 = st.columns(
                [1, 1, 3, 1, 1]
            )

            lon_index = 0
            lat_index = 0

            for col in columns:
                if col.lower() in ["lon", "longitude", "long", "lng"]:
                    lon_index = columns.index(col)
                elif col.lower() in ["lat", "latitude"]:
                    lat_index = columns.index(col)

            with row1_col1:
                x = st.selectbox("Longitude column", columns, lon_index)

            with row1_col2:
                y = st.selectbox("Latitude column", columns, lat_index)

            with row1_col4:
                heatmap = st.checkbox("Add heatmap")

            
            with row1_col5:
                if "age_yr" in columns:
                    index = columns.index("age_yr")
                else:
                    index = 0
                    heatmap_col = st.selectbox("Select heatmap data", columns, index)
                try:
                    m.add_heatmap(df, y, x, heatmap_col)
                except:
                    st.error("Please select a numeric column")

            try:
                m.add_points_from_xy(df, x, y)
            except:
                st.error("")

        except Exception as e:
            st.error(e)

    m.to_streamlit()
