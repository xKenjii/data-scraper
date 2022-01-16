import sys, requests

sys.path.append("..")
from handlers.mysqlHandler import defaultQuery

async def _fetchPriceData():
    
    try:
        tickers = defaultQuery("SELECT ticker FROM pricedata", None)

        for ticker in tickers:

            data = requests.get(f'https://api.binance.com/api/v3/avgPrice?symbol={ticker[0]}USDT')
            
            sc = data.status_code

            if sc == 200 or sc == 301:

                data = data.json()

                price = round(float(data['price']), 2)

                defaultQuery("UPDATE pricedata SET price = %s WHERE ticker = %s", [price, ticker[0]])

            else:
                print(f'(fetchPriceData.py) Fetching price data failed, error code: {sc}')

    except Exception as e:
        print(f"(fetchPriceData.py) Fetching prices has failed, see exception: {e}")