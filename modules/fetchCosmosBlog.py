import sys

sys.path.append("..")
from handlers.mysqlHandler import defaultQuery
from handlers.requestPost  import requestXml

async def _fetchCosmosBlog():

    url = 'https://blog.cosmos.network/feed'

    try:

        data = requestXml(url, "item", "title", "link", "link")

        # As no sensible data can be retrieved from the description/content
        # it will be inserted as null

        for article in data:

            defaultQuery("INSERT INTO cryptoarticles (source, designation, title, content) VALUES (%s, %s, %s, %s)", [article['link'], "COSMOS", article["title"], ""])
            

    except Exception as e:
        print(f"Cosmos\' Blog scraping job failed. See Exception: {e}")