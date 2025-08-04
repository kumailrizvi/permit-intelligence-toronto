import streamlit as st
from data import load_permit_data

st.set_page_config(page_title="Ontario Permit Intelligence Tracker", layout="wide")

st.title("📍 Ontario Permit Intelligence Tracker")
st.markdown("Real-time building permit activity in **Peel Region** (Mississauga, Brampton, Caledon).")

# Load permit data
try:
    df = load_permit_data()
    st.success(f"✅ Loaded {len(df)} permits")

    # Filter by date range
    st.sidebar.header("Filter Options")
    date_range = st.sidebar.date_input("Permit Date Range", [])
    if len(date_range) == 2:
        df = df[(df["date"] >= date_range[0]) & (df["date"] <= date_range[1])]

    # Filter by permit type
    permit_types = df["permit_type"].dropna().unique().tolist()
    selected_types = st.sidebar.multiselect("Permit Types", permit_types, default=permit_types)
    filtered_df = df[df["permit_type"].isin(selected_types)]

    # Display permits
    st.subheader("🗂 Permit Records")
    st.dataframe(filtered_df[["date", "permit_type", "address", "municipality"]], use_container_width=True)

except Exception as e:
    st.error("❌ Failed to load permit data.")
    st.exception(e)
