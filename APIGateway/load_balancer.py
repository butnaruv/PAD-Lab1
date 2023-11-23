index_url = 0


def get_url():
    global index_url
    from app import listOfEventManagerUrl
    total_urls = len(listOfEventManagerUrl)
    print(f"index {index_url}")
    serviceUrl = listOfEventManagerUrl[index_url%total_urls]
    serviceUrl = serviceUrl.split("://", 1)[-1]
    print(serviceUrl)
    index_url = index_url+1
    return serviceUrl