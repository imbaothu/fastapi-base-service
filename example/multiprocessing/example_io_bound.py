import threading
import requests

def fetch_url(url):
    response = requests.get(url)
    print(f"{url}: {len(response.content)} bytes")

urls = [
    'http://example.com',
    'http://example.org',
    'http://example.net'
]

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Finished fetching all URLs")
