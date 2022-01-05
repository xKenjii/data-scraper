import sys

sys.path.append("..")
from handlers.mysqlHandler import defaultQuery
from handlers.requestPost  import requestXml

async def _fetchPolygonBlog():

    url = 'https://blog.polygon.technology/feed/'

    try:

        data = requestXml(url, "item", "title", "link", "description")

        for article in data:

            description = article['description'].replace("[&#8230;]", "...")

            defaultQuery("INSERT INTO cryptoarticles (source, designation, title, content) VALUES (%s, %s, %s, %s)", [article['link'], "POLYGON", article['title'], description])

    except Exception as e:
        print(f"Polygon\'s Blog scraping job failed. See Exception: {e}")