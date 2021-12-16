import sys, requests
from bs4 import BeautifulSoup

sys.path.append("..")
from handlers.mysqlHandler import defaultQuery
from handlers.requestPost  import requestXml

async def _fetchCoinTelegraph(): 
    urls = ('https://cointelegraph.com/rss', 'https://cointelegraph.com/editors_pick_rss', 'https://cointelegraph.com/rss/tag/ethereum', 'https://cointelegraph.com/rss/tag/blockchain', 'https://cointelegraph.com/rss/tag/bitcoin', 'https://cointelegraph.com/rss/tag/altcoin', 'https://cointelegraph.com/rss/tag/litecoin', 'https://cointelegraph.com/rss/tag/monero', 'https://cointelegraph.com/rss/tag/regulation', 'https://cointelegraph.com/rss/category/weekly-overview')

    for url in urls:

        try:
            
            requestXml(url, 'item', 'title', 'link', 'description')
            # requestXml(url)
            # r = requests.get(url, headers = {'User-agent': 'Crypto Watcher Discord Bot'})

            # if r.status_code == requests.codes.ok:

            #     r.json()

            #     soup = BeautifulSoup(r.content, features='xml')
    
            #     articles = soup.findAll('item')

            #     for a in articles:
            #         title       = a.find('title').text
            #         link        = a.find('link').text
            #         description = a.find('description').text

            #         article = {
            #             'title': title,
            #             'link': link,
            #             'description': description
            #         }

            # else:
            #     print("Oopsie")

        except Exception as e:
            print(f"CoinTelegraph\'s scraping job failed. See Exception: {e}")