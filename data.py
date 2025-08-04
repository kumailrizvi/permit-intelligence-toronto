import pandas as pd

def load_permit_data():
    url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/1cb6f88e-0ac2-4f61-b8b1-04b3a1f1f8ff/resource/26b6cf9d-f10e-4454-993e-6247b3c8a52b/download/issued-building-permits.csv"
    local_backup = "issued-building-permits.csv"

    try:
        df = pd.read_csv(url, low_memory=False)
    except Exception as e:
        print("⚠️ Could not load online data, using local backup instead.")
        df = pd.read_csv(local_backup)

    df = df.rename(columns={
        "Permit Type": "permit_type",
        "Work Type": "work_type",
        "Application Date": "date",
        "Address": "address",
        "Work Description": "description"
    })

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df.dropna(subset=["permit_type", "address", "date"], inplace=True)

    return df
