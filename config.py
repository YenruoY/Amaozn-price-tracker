"""
Configuration file to assist `amazon_track.py` script
"""

import os
import re
import json
import requests
import datetime
from bs4 import BeautifulSoup
from helper_fucntions import get_name
from helper_fucntions import get_price

time_object = datetime.datetime.now() 

def add_link():
  
  url_raw = input("Enter Amazon product URL : ")

  # url pre-processing
  if url_raw[-1] != '/':
    url_raw = url_raw + '/'

  # strip the required parts from the url
  product_id = re.findall(r"/dp/(.+?)/", url_raw)[0]

  print("Product id : ", product_id)

  if os.path.exists('.cache/' + product_id + '.json'):
    print("Product already added!")
    return

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
  
  current_time = time_object.strftime("%Y-%m-%d %H:%M")

  # add the link to a cache file 
  item = {
    "product_name" : name,
    "product_it" : product_id,
    "target_price" : target_price,
    "current_price" : {
      current_time : price
    }
  }

  with open('./.cache/'+ product_id + '.json', 'w', encoding='utf-8') as f:
    json.dump(item, f, indent=4)

  print("Product added for tracking...")


def main():
  add_link()


if __name__ == "__main__":
   main() 
