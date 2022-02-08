from urllib import response
import requests

def get_data(url):
    response = requests.get(url)    
    try:
        return response.json()
    except ConnectionError as e:
        return e
