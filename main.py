import sched, time, asyncio, json

from modules.fetchArticles          import _fetchArticles

from modules.updatePriceData        import _updatePriceData
from modules.fetchPriceData         import _fetchPriceData
from modules.fetchFearGreedIndex    import _fetchFearGreedIndex # Only applies to Bitcoin.

with open("config.json", "r") as jsonfile:
    config = json.load(jsonfile)

s = sched.scheduler(time.time, time.sleep)
loop = asyncio.get_event_loop().run_until_complete

def fetchPosts(sc):

    loop(_fetchArticles())

    s.enter(config["interval"]["fetchPosts"], 1, fetchPosts, (sc,))

def updatePriceData(sc):

    loop(_updatePriceData())

    s.enter(config["interval"]["updatePriceData"], 1, updatePriceData, (sc,))

def fetchPriceData(sc):

    loop(_fetchPriceData())

    s.enter(config["interval"]["fetchPriceData"], 1, fetchPriceData, (sc,))

def fetchFearAndGreedIndex(sc):

    loop(_fetchFearGreedIndex())

    s.enter(config["interval"]["fetchFearAndGreedIndex"], 1, fetchFearAndGreedIndex, (sc,))

fetchPosts(s)
updatePriceData(s)
fetchPriceData(s)
fetchFearAndGreedIndex(s)

s.run()