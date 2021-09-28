import requests
import time

def downloadsite(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from url")
        
def downloadsites(urls):
    with requests.Session() as session:
        for url in urls:
            downloadsite(url, session)
            
if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://www.cnn.com",
        "https://www.youtube.com",
    ] * 80
    starttime = time.time()
    downloadsites(sites)
    duration = time.time() - starttime
    print(f"downloaded {len(sites)} in {duration} seconds")