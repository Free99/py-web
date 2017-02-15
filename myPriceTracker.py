__author__ = 'Tianshan'

import requests
from bs4 import BeautifulSoup

requests = requests.get("https://www.amazon.com/Logitech-Widescreen-Calling-Recording-Desktop/dp/B006JH8T3S/ref=sr_1_1?ie=UTF8&qid=1487139536&sr=8-1&keywords=logitech%2B920&th=1")

content = requests.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_ourprice", "class": "a-size-medium a-color-price"})

string_price = element.text.strip() # "$59.30"
price_without_symbol = string_price[1:] # "59.30"

print("The current price is {}.".format(string_price))