import pandas as pd
import requests

def load_permit_data():
    url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/datastore_search"
    params = {
        "resource_id": "26b6cf9d-f10e-4454-993e-6247b3c8a52b",
        "limit": 1000  # adjust for more data
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        records = response.json()["result"]["records"]
        df = pd.DataFrame(records)

        # Keep only relevant columns
        df = df[["permit_type", "work_type", "application_date", "address", "description"]]
        df = df.rename(columns={"application_date": "date"})
        df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date
        df.dropna(subset=["permit_type", "address", "date"], inplace=True)
        return df

    except Exception as e:
        print(f"⚠️ Error loading from API: {e}")
        return pd.DataFrame(columns=["permit_type", "work_type", "date", "address", "description"])
