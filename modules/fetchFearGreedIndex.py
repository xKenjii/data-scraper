import sys, requests

sys.path.append("..")
from handlers.mysqlHandler import defaultQuery

async def _fetchFearGreedIndex():
    
    try:
        data = requests.get('https://api.alternative.me/fng/?limit=1')

        sc = data.status_code

        if sc == 200 or 301:
            
            data = data.json()

            if data['data'][0]['value'] != None:

                existingData = defaultQuery("SELECT * FROM feargreedindex ORDER BY id DESC LIMIT 1", ())

                if int(existingData[0][1]) != int(data['data'][0]['value']):

                    defaultQuery("INSERT INTO feargreedindex (value, classification) VALUES (%s, %s)", [data['data'][0]['value'], data['data'][0]['value_classification']])

        else:
            print(f'(fetchFearGreedIndex.py) Fetching Bitcoin\'s fear and greed index has failed: {sc}')

    except Exception as e:
        print(f"(fetchFearGreedIndex.py) Fetching Fear & Greed has failed, see exception: {e}")