import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Permit Intelligence Tracker", layout="wide")

st.title("📍 Ontario Permit Intelligence Tracker")
st.markdown("Real-time building permit activity in Toronto (MVP).")

# Load mock data
DATA_PATH = "data/latest_permits.csv"
df = pd.read_csv(DATA_PATH)

# Filter bar
keyword = st.text_input("Filter permits by keyword (e.g. 'pharmacy', 'clinic')", "")
if keyword:
    df = df[df.apply(lambda row: row.astype(str).str.contains(keyword, case=False).any(), axis=1)]

# Show table
st.subheader("📄 Permit Records")
st.dataframe(df, use_container_width=True)

# Map
st.subheader("🗺 Permit Locations (Static Example)")
m = folium.Map(location=[43.65107, -79.347015], zoom_start=11)
folium.Marker(location=[43.65107, -79.347015], popup="123 King St - New Building").add_to(m)
st_folium(m, width=700)
