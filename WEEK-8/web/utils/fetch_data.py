
def fetch_data(url):
    import requests
    from pprint import pprint
    response = requests.get(url)
    data = response.json()
    return data
