import pandas as pd
import requests

def load_permit_data():
    url = "https://data.peelregion.ca/api/records/1.0/search/?dataset=building-permits&q=&rows=1000&sort=issued_date&facet=municipality"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        records = data["records"]
        rows = [rec["fields"] for rec in records]

        df = pd.DataFrame(rows)

        # Cleanup / normalize if needed
        if "issued_date" in df.columns:
            df["issued_date"] = pd.to_datetime(df["issued_date"], errors="coerce")
        return df

    except Exception as e:
        print("Error loading data:", e)
        return pd.DataFrame()
