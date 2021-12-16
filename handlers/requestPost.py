import requests, sys
from bs4 import BeautifulSoup

sys.path.append("..")
from handlers.mysqlHandler import defaultQuery

    # url       -> URL to send request to
    # objectTag -> Object name which will be used in findAll


def requestXml(_url, _objectTag, _title, _link, _description):

    try:
#         print(_url)
        r = requests.get(_url, headers = {'User-agent': 'Crypto Watcher Discord Bot | Contact Kenjii#2641 for Inquiries'})

        if r.status_code == requests.codes.ok:
            
            soup = BeautifulSoup(r.content, features='xml')

            articles = soup.findAll(_objectTag)

            for a in articles:
                title       = a.find(_title).text 
                link        = a.find(_link).text 
                description = a.find(_description).text

                article = {
                    'title': title,
                    'link': link,
                    'description': description
                }

                sqlResponse = defaultQuery("SELECT id FROM articles WHERE source = %s", (article['link'], ))
            
                if not sqlResponse:

                    print(article['title'])
                    print(article['link'])
                    print(article['description'])
                    print('---------')
        else:
            # Extend on error handling
            print("oopsie")

    except Exception as e:
        # Extend on error handling
        print(f"request failed: {e}")