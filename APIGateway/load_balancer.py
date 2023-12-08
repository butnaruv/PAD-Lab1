from flask import make_response

index_url = 0

# fa index url dictionar. key = serviciu

def load_balance_requests():
    global index_url
    from app import listOfEventManagerUrl
    total_urls = len(listOfEventManagerUrl)
    if total_urls == 0:
        raise Exception("No services available")
    print(f"index {index_url}")
    serviceUrl = listOfEventManagerUrl[index_url % total_urls]
    serviceUrl = serviceUrl.split("://", 1)[-1]
    print(serviceUrl)
    index_url = index_url + 1
    return serviceUrl


def get_url():
    try:
        url = load_balance_requests()
        return url
    except Exception as e:
        print(e)
        return make_response("No sources available")


def reset_index():
    global index_url
    index_url = 0
