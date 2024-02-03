import re
import json
import glob
import requests
import datetime
from helper_fucntions import get_name
from helper_fucntions import get_price


products = glob.glob(".cache/*.json")
dt_ob = datetime.datetime.now()


def update_price(product, price):
  with open(product, 'r') as f:
    existing_data = json.load(f)

  current_time = dt_ob.strftime("%Y-%m-%d %H:%M")

  existing_data["current_price"].update({current_time : price})

  with open(product, 'w') as f:
    json.dump(existing_data, f, indent=4)


# Get the price using the function
for product in products:

  product_id = re.findall(r"/([A-Z0-9]+)\.json", product)[0]

  url = "https://www.amazon.in/dp/" + product_id

  # url pre-processing
  if url[-1] != '/':
    url = url + '/'
  
  response = requests.get(url, headers= {'User-agent' : 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'})

  price = get_price(response)
  name = get_name(response)

  # Print product name and price 
  if price:
    print("\n")
    print(name)
    print(f"Current price of the product Rs. {price}")
    print(url)

    update_price(product, price)
  else:
    print("Price not found")
