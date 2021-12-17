import sys

sys.path.append("..")
from handlers.mysqlHandler import defaultQuery
from handlers.requestPost  import requestXml

async def _fetchBitcoinDotCom():

    try:

        data = requestXml('https://news.bitcoin.com/feed/', 'item', 'title', 'link', 'description')
        
        # print(data)

        for article in data:
            defaultQuery('INSERT INTO cryptoarticles (source, title, content) VALUES (%s, %s, %s)', [article['link'], article['title'], article['description'].replace('[&#8230;]', '[...]')])

    except Exception as e:
            print(f"Bitcoin.com\'s scraping job failed. See Exception: {e}")