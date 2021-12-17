import sys

sys.path.append("..")
from handlers.mysqlHandler import defaultQuery
from handlers.requestPost  import requestXml

async def _fetchDecryptDotCom():

    try:

        data = requestXml('https://decrypt.co/feed', 'item', 'title', 'link', 'description')

        for article in data:
            defaultQuery('INSERT INTO cryptoarticles (source, title, content) VALUES (%s, %s, %s)', [article['link'], article['title'], article['description']])

    except Exception as e:
            print(f"Decrypt.com\'s scraping job failed. See Exception: {e}")