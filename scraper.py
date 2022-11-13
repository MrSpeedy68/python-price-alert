import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://www.keychron.com/products/keychron-k6-pro-qmk-via-wireless-custom-mechanical-keyboard?variant=40119467737177"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

data=[]

f = requests.get(baseurl, headers=headers).text
hun=BeautifulSoup(f, 'html.parser')

try:
    name = hun.find("h1", {"class":"h2 product-single__title"}).text.replace('\n',"")
except:
    name = None


try:
    price = hun.find("span", {"id" : "ProductPrice-7118797045849"}).text.replace('\n',"")
except:
    price = None


keyboard = {"name":name, "price":price}

data.append(keyboard)

df = pd.DataFrame(data)

print(df)

print(price)

#<h1 class="h2 product-single__title"></h1>
#<span id="ProductPrice-7118797045849" class="product__price">$119.00</span>
#
#
#
