
import requests
import pandas as pd
from datetime import datetime

def fetch_bitcoin_data(days=365, save_path='bitcoin_prices.csv'):
    '''
    Fetch historical Bitcoin price data from CoinGecko API for the past `days`.
    
    Parameters:
        days (int): Number of past days to fetch data for.
        save_path (str): Local path to save the CSV output.

    Returns:
        pd.DataFrame: DataFrame containing 'Timestamp' and 'Price' columns.
    '''
    url = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
    params = {
        'vs_currency': 'usd',
        'days': days,
        'interval': 'daily'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        prices = data['prices']
        df = pd.DataFrame(prices, columns=['Timestamp', 'Price'])
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='ms')
        df.to_csv(save_path, index=False)
        
        print(f"✅ Successfully fetched and saved {len(df)} records to {save_path}")
        return df
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return pd.DataFrame()
