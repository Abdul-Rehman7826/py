from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json
session = HTMLSession()

r = session.get(
    'https://www.realtor.com/realestateandhomes-search/Aurora_CO/show-newest-listings/sby-6')

r.html.render()

html = BeautifulSoup(r.html.html, "html.parser")

data_section = html.find("script", type="application/json")

data = json.loads(data_section.text)
properties = {"properties": data["props"]["pageProps"]["properties"]}
# print(properties)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(properties, f)
