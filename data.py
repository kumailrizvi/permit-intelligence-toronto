import pandas as pd

def load_permit_data():
    # This URL returns the latest permits issued in Peel Region (Mississauga/Brampton/Caledon)
    url = "https://data.peelregion.ca/api/records/1.0/search/?dataset=building-permits&q=&rows=1000&sort=issued_date&facet=municipality"
    
    # Get JSON data
    response = pd.read_json(url)
    
    # Extract records
    records = response["records"]
    data = [rec["fields"] for rec in records]
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Normalize column names and types
    df["date"] = pd.to_datetime(df["issued_date"], errors="coerce")
    df["permit_type"] = df.get("permit_type", "Unknown")
    df["address"] = df.get("address", "")
    df["municipality"] = df.get("municipality", "")
    
    return df
