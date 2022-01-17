import sys

sys.path.append("..")
from handlers.mysqlHandler import defaultQuery
from handlers.requestPost  import requestXml

async def _fetchArticles():

    try:

        sourceData = defaultQuery('SELECT * FROM articlesources', None)

        for data in sourceData:

            xmlData = requestXml(data[1], data[2], data[3], data[4], data[5])

            for article in xmlData:

                if data[7] == 0:
                    description = article['description']
                else:
                    description = ""

                defaultQuery('INSERT INTO cryptoarticles (source, designation, title, content) VALUES (%s, %s, %s, %s)', [article['link'], data[6], article['title'], description])

    except Exception as e:
        print(f"(fetchArticles.py) Fetching articles has failed, see exception: {e}")