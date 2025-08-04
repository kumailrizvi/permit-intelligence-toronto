import pandas as pd

def load_permit_data():
    url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/1cb6f88e-0ac2-4f61-b8b1-04b3a1f1f8ff/resource/26b6cf9d-f10e-4454-993e-6247b3c8a52b/download/issued-building-permits.csv"
    try:
        df = pd.read_csv(url, low_memory=False)
        print("✅ Loaded live data")
    except Exception as e:
        print("⚠️ Failed to load live data, using backup:", e)
        df = pd.read_csv("backup_permits.csv")

    df = df[["permit_type", "work_type", "application_date", "address", "description"]]
    df = df.rename(columns={"application_date": "date"})
    df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date
    df.dropna(subset=["permit_type", "address", "date"], inplace=True)
    return df
