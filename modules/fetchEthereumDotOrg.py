import sys

sys.path.append("..")
from handlers.mysqlHandler import defaultQuery
from handlers.requestPost  import requestXml

async def _fetchEthereumDotOrg():

    try:
                                                                                # guid = link
        data = requestXml('https://blog.ethereum.org/feed.xml', 'item', 'title', 'guid', 'description')

        for article in data:
            defaultQuery('INSERT INTO cryptoarticles (source, title, content) VALUES (%s, %s, %s)', [article['link'], article['title'], article['description']])

    except Exception as e:
            print(f"Decrypt.com\'s scraping job failed. See Exception: {e}")