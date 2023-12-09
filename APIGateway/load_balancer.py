from flask import make_response

index_url = {}

# fa index url dictionar. key = serviciu

def load_balance_requests(list_of_urls, key):
    global index_url
    index_url.setdefault(key, 0)
    total_urls = len(list_of_urls)
    if total_urls == 0:
        raise Exception("No services available")
    print(f"index {index_url[key]}")
    serviceUrl = list_of_urls[index_url[key] % total_urls]
    serviceUrl = serviceUrl.split("://", 1)[-1]
    print(serviceUrl)
    index_url[key] += 1
    return serviceUrl


def get_url(list_of_urls, key):
    try:
        url = load_balance_requests(list_of_urls, key)
        return url
    except Exception as e:
        print(e)
        return make_response("No sources available")


def reset_index(key):
    global index_url
    index_url[key] = 0
