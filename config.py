"""
Configuration file to assist `amazon_track.py` script
"""

import re
import json
import requests
from bs4 import BeautifulSoup
from functions import get_name
from functions import get_price

# path = ""

def add_link():
  
  url_raw = input("Enter Amazon product URL : ")

  # url pre-processing
  if url_raw[-1] != '/':
    url_raw = url_raw + '/'

  # strip the required parts from the url
  product_id = re.findall(r"/dp/(.+?)/", url_raw)[0]

  print("Product id : ", product_id)

  url = "https://www.amazon.in/dp/" + product_id
  request = requests.get(url, headers= {'User-agent' : 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'})

  # checking if the URL is valid
  if request.status_code != 200 :
    print("Link not valid!!\n")
    return 
  else :
    print("Product found !")

  price = get_price(request)  
  name = get_name(request)
  print("Current price : ", price)

  # input validation
  try:
    target_price = int(input("Enter target price : "))
    print("Target price set to : ", target_price)
  except ValueError:
    print("Not a valid price")
  
  # add the link to a cache file 
  item = {
    "product_name" : name,
    "product_it" : product_id,
    "target_price" : target_price,
  }

  with open('./.cache/'+ product_id + '.json', 'w', encoding='utf-8') as f:
    json.dump(item, f)

  print(json.dumps(item))


def main():
  add_link()


if __name__ == "__main__":
   main() 
