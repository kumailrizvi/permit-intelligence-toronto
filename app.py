import streamlit as st
import folium
from streamlit_folium import st_folium
from data import load_permit_data

st.set_page_config(page_title="Permit Tracker – Mississauga", layout="wide")
st.title("🏙️ Mississauga Permit Tracker (Live)")
st.markdown("Building permit data from Mississauga Open Data via ArcGIS API")

df = load_permit_data()
if df.empty:
    st.error("No data available from Mississauga API")
else:
    st.success("✅ Data loaded")
    st.dataframe(df.head(5), use_container_width=True)

    keyword = st.text_input("Filter by keyword (e.g., pharmacy, clinic, renovation)", "").strip().lower()
    if keyword:
        mask = (
            df["permit_type"].str.lower().str.contains(keyword) |
            df["address"].str.lower().str.contains(keyword) |
            df["description"].str.lower().str.contains(keyword)
        )
        filtered = df[mask]
    else:
        filtered = df.head(20)

    st.markdown(f"Found: **{len(filtered)}** matching permits")
    st.dataframe(filtered[["date","permit_type","address"]], use_container_width=True)

    m = folium.Map(location=[43.6, -79.6], zoom_start=11)
    st.subheader("📍 Permit Locations (Static Demo)")
    folium.Marker([43.6, -79.6], popup="Mississauga Center").add_to(m)
    st_folium(m, width=700)
