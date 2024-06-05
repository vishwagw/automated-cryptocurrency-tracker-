import requests
import pandas as pd
from datetime import datetime

def fetch_crypto_price(crypto_ids):
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': ','.join(crypto_ids), 
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def display_prices(data):
    df = pd.DataFrame(data).T
    df.columns = ['price (USD)']
    df['Timestamp'] = datetime.now()
    print(df)

if __name__ == "__name__":
    crypto_ids = ['bitcoin', 'ethereum', 'cardano']  # we can add more crypto of our choise
    data = fetch_crypto_price(crypto_ids)
    display_prices(data)

