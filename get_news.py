import textwrap
import requests
from pprint import pprint
from bs4 import BeautifulSoup

URL = "https://news.yandex.ru/index.rss"
xml = requests.get(URL).text
soup = BeautifulSoup(xml, 'xml')

news = [item.title.string for item in soup.find_all('item')]
for news_item in news[:20]:
    for line in textwrap.wrap(news_item):
        print(line)
    print()
