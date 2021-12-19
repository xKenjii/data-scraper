import sched, time, asyncio

from modules.fetchCoinTelegraph     import _fetchCoinTelegraph
from modules.fetchBitcoinDotCom     import _fetchBitcoinDotCom
from modules.fetchDecryptDotCo      import _fetchDecryptDotCom
from modules.fetchEthereumDotOrg    import _fetchEthereumDotOrg

from modules.fetchPriceData         import _fetchPriceData

s = sched.scheduler(time.time, time.sleep)
loop = asyncio.get_event_loop().run_until_complete

def fetchPosts(sc): 

    loop(_fetchCoinTelegraph())
    loop(_fetchBitcoinDotCom())
    loop(_fetchDecryptDotCom())
    loop(_fetchEthereumDotOrg())

    s.enter(60, 1, fetchPosts, (sc,))

def fetchPriceData(sc):

    loop(_fetchPriceData())

    s.enter(20, 1, fetchPriceData, (sc,))


fetchPosts(s)
fetchPriceData(s)

s.run()