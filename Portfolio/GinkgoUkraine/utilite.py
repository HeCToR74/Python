import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.walmart.com/browse/5427")
print(page.text)