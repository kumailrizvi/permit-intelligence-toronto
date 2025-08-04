import pandas as pd
import requests

def load_permit_data():
    url = "https://services6.arcgis.com/hM5ymMLbxIyWTjn2/arcgis/rest/services/2024_Building_Permits/FeatureServer/0/query"
    params = {
        "where": "1=1",
        "outFields": "PermitType,WorkType,IssuedDate,Address,WorkDesc",
        "f": "json",
        "resultRecordCount": 1000
    }
    try:
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        records = resp.json().get("features", [])
        df = pd.DataFrame([r["attributes"] for r in records])
        df = df.rename(columns={
            "PermitType": "permit_type",
            "WorkType": "work_type",
            "IssuedDate": "date",
            "Address": "address",
            "WorkDesc": "description"
        })
        df["date"] = pd.to_datetime(df["date"], unit="ms", errors="coerce")
        df.dropna(subset=["permit_type","address","date"], inplace=True)
        return df
    except Exception as e:
        print(f"Error fetching Mississauga data: {e}")
        return pd.DataFrame()
