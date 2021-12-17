import sched, time, asyncio

from modules.fetchCoinTelegraph  import _fetchCoinTelegraph
from modules.fetchBitcoinDotCom  import _fetchBitcoinDotCom
from modules.fetchDecryptDotCo   import _fetchDecryptDotCom
from modules.fetchEthereumDotOrg import _fetchEthereumDotOrg

s = sched.scheduler(time.time, time.sleep)
loop = asyncio.get_event_loop().run_until_complete

def do_something(sc): 

    loop(_fetchCoinTelegraph())
    loop(_fetchBitcoinDotCom())
    loop(_fetchDecryptDotCom())
    loop(_fetchEthereumDotOrg())

    s.enter(60, 1, do_something, (sc,))

do_something(s)

s.run()