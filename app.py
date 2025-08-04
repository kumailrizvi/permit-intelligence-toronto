import streamlit as st
from streamlit_folium import st_folium
import folium
from data import load_permit_data

st.set_page_config(page_title="Ontario Permit Intelligence Tracker", layout="wide")
st.title("📍 Ontario Permit Intelligence Tracker")
st.markdown("Real-time building permit activity in Toronto (MVP).")

# Load data
df = load_permit_data()
st.success("✅ Raw data loaded:")
st.dataframe(df.head())

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

# Show filtered table
st.subheader("🗂 Permit Records")
if not filtered_df.empty:
    st.write(f"🔍 Filtered records found: {len(filtered_df)}")
    st.dataframe(filtered_df[["date", "permit_type", "address"]], use_container_width=True)
else:
    st.warning("No matching records found.")

# Static map placeholder
st.subheader("🗺 Permit Locations (Static Example)")
m = folium.Map(location=[43.7, -79.4], zoom_start=10)
folium.Marker([43.7, -79.4], popup="Static Example - Toronto").add_to(m)
st_folium(m, width=700)
