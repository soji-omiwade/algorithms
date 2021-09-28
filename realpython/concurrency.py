import requests
import time
import threading
from concurrent.futures import ThreadPoolExecutor
import sys
from collections import Counter

thread_local = threading.local()
threading_count = int(sys.argv[1])
labordivision = Counter()

def downloadsite(url, session):
    with session.get(url) as response:
        #print(f"Read {len(response.content)} from url")
        pass
        
def downloadsites_threading(urls):
    def downloadsite(url):
        session = get_session()
        with session.get(url) as response:
            #print(f"Read {len(response.content)} from url")
            pass
        labordivision[threading.get_ident()] += 1

    def get_session():
        if not hasattr(thread_local, "session"):
            thread_local.session = requests.Session()
        return thread_local.session

    with ThreadPoolExecutor(max_workers=threading_count) as executor:
        executor.map(downloadsite, urls)
        

def downloadsites_synch(urls):
    with requests.Session() as session:
        for url in urls:
            downloadsite(url, session)
            
if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    approaches = ["synchronous", "threading"]
    res = []
    
    #synchronous
    starttime = time.time()
    downloadsites_synch(sites)
    res.append(time.time() - starttime)

    #threading
    starttime = time.time()
    downloadsites_threading(sites)
    res.append(time.time() - starttime)
    print(labordivision)
    
    for approach, runtime in zip(approaches, res):
        print(approach, "\t", f"{runtime:.1f}" )
