__author__ = 'jason'
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "" + str(page)    #will fill later
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll(): #will fill later
            href = "" + link.get("href");
            title = link.string #this gets the text section, not the HTML
            print(href)
            print(title)
            page += 1
def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll(): #will fill later
        print(item_name.string)
    for link in soup.findAll('a'):
        href = "" + link.get('href')    #will fill later
        print(href)

trade_spider(1)