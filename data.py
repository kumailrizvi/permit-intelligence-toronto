import pandas as pd

def load_permit_data():
    # Load from local file instead of broken URL
    df = pd.read_csv("backup_permits.csv", low_memory=False)

    # Clean & rename
    df = df[["permit_type", "work_type", "application_date", "address", "description"]]
    df = df.rename(columns={"application_date": "date"})
    df["date"] = pd.to_datetime(df["date"]).dt.date
    df.dropna(subset=["permit_type", "address", "date"], inplace=True)
    
    return df
