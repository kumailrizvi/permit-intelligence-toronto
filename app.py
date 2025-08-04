import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Ontario Permit Intelligence Tracker", layout="wide")

st.title("📍 Ontario Permit Intelligence Tracker")
st.markdown("Real-time building permit activity in Toronto (MVP).")

# Load real permit data (filtered and cleaned for MVP)
df = pd.read_csv("https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/1cb6f88e-0ac2-4f61-b8b1-04b3a1f1f8ff/resource/26b6cf9d-f10e-4454-993e-6247b3c8a52b/download/issued-building-permits.csv")
df = df[["permit_type", "work_type", "application_date", "address", "description"]]
df = df.rename(columns={"application_date": "date"})
df["date"] = pd.to_datetime(df["date"]).dt.date
df.dropna(subset=["permit_type", "address", "date"], inplace=True)

# Search bar
keyword = st.text_input("Filter permits by keyword (e.g. 'pharmacy', 'clinic')", "").strip().lower()

# Filter logic
if keyword:
    mask = (
        df["permit_type"].str.lower().str.contains(keyword) |
        df["address"].str.lower().str.contains(keyword) |
        df["description"].str.lower().str.contains(keyword) |
        df["work_type"].str.lower().str.contains(keyword)
    )
    filtered_df = df[mask]
else:
    filtered_df = df.head(10)

# Show table
st.subheader("🗂 Permit Records")
st.dataframe(filtered_df[["date", "permit_type", "address"]], use_container_width=True)

# Map placeholder
st.subheader("🗺 Permit Locations (Static Example)")
m = folium.Map(location=[43.7, -79.4], zoom_start=10)
folium.Marker([43.7, -79.4], popup="Static Example - Toronto").add_to(m)
st_folium(m, width=700)
