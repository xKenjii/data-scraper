import sys

sys.path.append("..")
from handlers.mysqlHandler import defaultQuery
from handlers.requestPost  import requestXml
 
async def _fetchCoinTelegraph(): 
    urls = ('https://cointelegraph.com/rss', 'https://cointelegraph.com/editors_pick_rss', 'https://cointelegraph.com/rss/tag/ethereum', 'https://cointelegraph.com/rss/tag/blockchain', 'https://cointelegraph.com/rss/tag/bitcoin', 'https://cointelegraph.com/rss/tag/altcoin', 'https://cointelegraph.com/rss/tag/litecoin', 'https://cointelegraph.com/rss/tag/monero', 'https://cointelegraph.com/rss/tag/regulation', 'https://cointelegraph.com/rss/category/weekly-overview')

    for url in urls:

        try:
            
            data = requestXml(url, 'item', 'title', 'link', 'description')
            
            for article in data:
                defaultQuery('INSERT INTO cryptoarticles (source, title, content) VALUES (%s, %s, %s)', [article['link'], article['title'], article['description']])

        except Exception as e:
            print(f"CoinTelegraph\'s scraping job failed. See Exception: {e}")