import pandas as pd

def load_permit_data():
    url = "https://data.peelregion.ca/datasets/RegionofPeel::building-permits.csv?format=csv&api=true"
    df = pd.read_csv(url, low_memory=False)
    # Inspect columns, and then:
    df = df.rename(columns={ 'applicationdate': 'date', 'permit_number': 'permit_id', 'address': 'address', /* etc */ })
    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date
    df = df.dropna(subset=['date', 'address'])
    return df
