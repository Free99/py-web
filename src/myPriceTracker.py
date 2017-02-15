__author__ = 'Tianshan'

import requests

requests = requests.get("https://www.amazon.com/Logitech-Widescreen-Calling-Recording-Desktop/dp/B006JH8T3S/ref=sr_1_1?ie=UTF8&qid=1487139536&sr=8-1&keywords=logitech%2B920&th=1")
# <span id="priceblock_ourprice" class="a-size-medium a-color-price">$59.30</span>

print(requests.content)