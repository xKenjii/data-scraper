import sys, requests

sys.path.append("..")
from handlers.mysqlHandler import defaultQuery
import json

async def _fetchPriceData():
    try:
        with open("./tickers.json", "r") as jsonfile:
            tickers = json.load(jsonfile)

        # tickers = defaultQuery("SELECT ticker FROM pricechart", None)

        for ticker in tickers['tickers']:

            data = requests.get(f'https://api.binance.com/api/v3/avgPrice?symbol={ticker}USDT')

            sc = data.status_code

            if sc == 200 or sc == 301:

                data = data.json()

                price = round(float(data['price']), 2)

                defaultQuery("INSERT INTO pricechart (ticker, price) VALUES (%s, %s)", [ticker, price])
            
            else:
                print(f'(updatePriceData.py) Fetching price data failed, error code: {sc}')

    except Exception as e:
        print(f"(updatePriceData.py) Fetching prices has failed, see exception: {e}")