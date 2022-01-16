import requests, sys, re
from bs4 import BeautifulSoup

sys.path.append("..")
from handlers.mysqlHandler import defaultQuery

recompile = re.compile('<.*?>')

    # url       -> URL to send request to
    # objectTag -> Object name which will be used in findAll

def requestXml( _url, _objectTag, _title, _link, _description, _hasToBeUnique = True):

    dataList = []

    try:

        r = requests.get(_url, headers = {'User-agent': 'Crypto Watcher Discord Bot | Contact Kenjii#2641 for Inquiries'})

        if r.status_code == requests.codes.ok:
            
            soup = BeautifulSoup(r.content, features='xml')

            articles = soup.findAll(_objectTag)

            for a in articles:
                title       = re.sub(recompile, '', a.find(_title).text).strip()
                link        = re.sub(recompile, '', a.find(_link).text).strip()
                description = re.sub(recompile, '', a.find(_description).text).strip()

                article = {
                    'title': title,
                    'link': link,
                    'description': description
                }

                if _hasToBeUnique is True:

                    sqlResponse = defaultQuery("SELECT id FROM cryptoarticles WHERE source = %s", (article['link'], ))

                    if not sqlResponse:
                        dataList.append(article)

                else:
                    dataList.append(article)

            return dataList

        else:
            # Extend on error handling
            print("oopsie")

    except Exception as e:
        # Extend on error handling
        print(f"(requestPost.py) request failed: {e}")