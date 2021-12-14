import mysql.connector, requests, sys, os, sched, time, asyncio
from mysql.connector import Error
from bs4 import BeautifulSoup

import handlers.mysqlHandler
from modules.fetchCoinTelegraph import _fetchCoinTelegraph

# handlers.mysqlHandler.defaultQuery("INSERT INTO articles (source, title, content) VALUES ('test2', 'test2', 'test2')", None)

s = sched.scheduler(time.time, time.sleep)
loop = asyncio.get_event_loop().run_until_complete

def do_something(sc): 
    loop(_fetchCoinTelegraph())
    s.enter(5, 1, do_something, (sc,))

do_something(s)

s.run()
