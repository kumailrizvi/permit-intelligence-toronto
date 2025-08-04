import streamlit as st
from streamlit_folium import st_folium
import folium
from data import load_permit_data

st.set_page_config(page_title="Ontario Permit Intelligence Tracker", layout="wide")
st.title("📍 Ontario Permit Intelligence Tracker")
st.markdown("Real-time building permit activity in Toronto (MVP).")

df = load_permit_data()

if df.empty:
    st.error("❌ No data could be loaded from the Toronto Open Data portal.")
else:
    st.success("✅ Raw data loaded:")
    st.dataframe(df.head(5), use_container_width=True)

    keyword = st.text_input("Filter permits by keyword (e.g. 'pharmacy', 'clinic', 'king')", "").strip().lower()

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

    st.markdown(f"🔍 Filtered records found: **{len(filtered_df)}**")

    st.subheader("🗂 Permit Records")
    st.dataframe(filtered_df[["date", "permit_type", "address"]], use_container_width=True)

    st.subheader("🗺 Permit Locations (Static Example)")
    m = folium.Map(location=[43.7, -79.4], zoom_start=10)
    folium.Marker([43.7, -79.4], popup="Toronto City Center").add_to(m)
    st_folium(m, width=700)
