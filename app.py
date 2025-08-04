import streamlit as st
from streamlit_folium import st_folium
import folium
from data import load_permit_data

st.set_page_config(page_title="Ontario Permit Intelligence Tracker", layout="wide")
st.title("📍 Ontario Permit Intelligence Tracker")
st.markdown("Real-time building permit activity in Toronto (using backup data for now).")

# Load permit data from local CSV (fallback)
df = load_permit_data()

# Optional preview of raw data
st.write("✅ Loaded permit records:", df.shape[0])
st.dataframe(df.head(), use_container_width=True)

# Search
keyword = st.text_input("🔍 Search permits (any keyword):", "").strip().lower()

# Filter
if keyword:
    mask = (
        df["permit_type"].str.lower().str.contains(keyword) |
        df["address"].str.lower().str.contains(keyword) |
        df["description"].str.lower().str.contains(keyword) |
        df["work_type"].str.lower().str.contains(keyword)
    )
    filtered_df = df[mask]
else:
    filtered_df = df.head(15)

# Table
st.subheader("🗂 Permit Records")
st.dataframe(filtered_df[["date", "permit_type", "address", "description"]], use_container_width=True)

# Map placeholder
st.subheader("🗺 Permit Locations (Static Demo)")
m = folium.Map(location=[43.7, -79.4], zoom_start=10)
foli
