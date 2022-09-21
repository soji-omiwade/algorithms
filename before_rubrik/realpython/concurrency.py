import requests
import time
import threading
from concurrent.futures import ThreadPoolExecutor
import sys
from collections import Counter
import asyncio
import aiohttp

def downloadsites_synchronous(urls):
    def downloadsite(url, session):
        with session.get(url) as response:
            if not response:
                raise Exception()

    with requests.Session() as session:
        for url in urls:
            downloadsite(url, session)

def downloadsites_threading(urls):
    def downloadsite(url):
        session = get_session()
        with session.get(url) as response:
            if not response:
                raise Exception()
        labordivision[threading.get_ident()] += 1

    def get_session():
        if not hasattr(thread_local, "session"):
            thread_local.session = requests.Session()
        return thread_local.session

    with ThreadPoolExecutor(max_workers=threading_count) as executor:
        executor.map(downloadsite, urls)

async def downloadsites_eventloop(sites):
    async def downloadsite(session, url):
        async with session.get(url) as response:
            if not response:
                raise Exception()
            
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(downloadsite(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)
        
            
thread_local = threading.local()
threading_count = int(sys.argv[1])
labordivision = Counter()
taskcount = int(sys.argv[2])

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://www.cnn.com",
        "https://www.youtube.com",
        "https://www.yahoo.com"
    ] * (taskcount // 2)
    approaches = []
    res = []
    
    '''synchronous'''
    starttime = time.time()
    downloadsites_synchronous(sites)
    approaches.append("synchronous")
    res.append(time.time() - starttime)

    '''threading'''
    starttime = time.time()
    downloadsites_threading(sites)
    approaches.append("threading")
    res.append(time.time() - starttime)
    print(len(labordivision), labordivision)
    
    '''eventloop'''
    starttime = time.time()
    asyncio.get_event_loop().run_until_complete(downloadsites_eventloop(sites))
    approaches.append("eventloop")
    res.append(time.time() - starttime)
    
    
    for approach, runtime in zip(approaches, res):
        print(approach, "\t", f"{runtime:.1f}" )
