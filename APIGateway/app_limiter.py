import requests
import concurrent.futures
import time

def get_status(url):

    resp = requests.get(url=url)
    return resp.status_code

urls = [
    'http://127.0.0.1:5000/event',
    'http://127.0.0.1:5000/event',
    'http://127.0.0.1:5000/event',
    'http://127.0.0.1:5000/event',
    'http://127.0.0.1:5000/event',
    'http://127.0.0.1:5000/event/59',
    'http://127.0.0.1:5000/event/59',
    'http://127.0.0.1:5000/event/59',
    'http://127.0.0.1:5000/event/59',
]

tm1 = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:

    futures = []

    for url in urls:
        futures.append(executor.submit(get_status, url=url))

    for future in concurrent.futures.as_completed(futures):
        print(future.result())

tm2 = time.perf_counter()
print(f'Total time elapsed: {tm2-tm1:0.2f} seconds')