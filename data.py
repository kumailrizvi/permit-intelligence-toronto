# data.py
import pandas as pd

def load_permit_data():
    df = pd.read_csv("issued-building-permits-backup.csv")
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
