import requests
import os
import csv
from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
LIMIT = 1000

def run_stock_job():
    url =f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}'
    response = requests.get(url)
    tickers = []

    data = response.json()
    #print(data.keys())
    #print(data['next_url'])
    for ticker in data['results']:
        tickers.append(ticker)

    LIMIT_READ_PER_MINUTE = 5000
    while 'next_url' in data #and len(tickers)<LIMIT_READ_PER_MINUTE:
        print('requesting next page', data['next_url'])
        response = requests.get(data['next_url']+f'&apiKey={POLYGON_API_KEY}')
        data = response.json()
        #print(len(tickers))
        print(data)
        for ticker in data['results']:
            tickers.append(ticker)

    example_ticker={'ticker': 'HTBK',
    'name': 'Heritage Commerce Corp',
    'market': 'stocks',
    'locale': 'us',
        'primary_exchange': 'XNAS',
        'type': 'CS',
        'active': True,
        'currency_name': 'usd',
            'cik': '0001053352',
            'composite_figi': 'BBG000C48437',
            'share_class_figi': 'BBG001SBY8P0',
            'last_updated_utc': '2025-09-29T06:04:58.488437044Z'}

    print(f"Total tickers collected: {len(tickers)}")

    # Write tickers to CSV file with the same schema as example_ticker
    csv_filename = 'tickers.csv'
    fieldnames = list(example_ticker.keys())

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for ticker in tickers:
            # Ensure all fields from example_ticker schema are present
            row = {}
            for field in fieldnames:
                row[field] = ticker.get(field, '')  # Use empty string if field is missing
            
            writer.writerow(row)
    print(f"Tickers data written to {csv_filename}")

if __name__ == '__main__':
    run_stock_job()




#  