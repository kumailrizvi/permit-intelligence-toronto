# data.py
import pandas as pd

def load_permit_data():
    csv_url = "https://opendata.toronto.ca/building-permits/issued-building-permits.csv"

    try:
        df = pd.read_csv(csv_url)
        df = df[["permit_type", "work_type", "application_date", "address", "description"]]
        df = df.rename(columns={"application_date": "date"})
        df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date
        df.dropna(subset=["permit_type", "address", "date"], inplace=True)
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load permit data: {e}")
