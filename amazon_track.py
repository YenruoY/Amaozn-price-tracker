import re
import requests
from helper_fucntions import get_name
from helper_fucntions import get_price
from bs4 import BeautifulSoup

# Sample product URL
################################
#   Add URL below inside ""
################################
urls = [
        "",
        ""]

# Get the price using the function
for url_raw in urls:

  # url pre-processing
  if url_raw[-1] != '/':
    url_raw = url_raw + '/'

  # strip the required parts from the url
  product_id = re.findall(r"/dp/(.+?)/", url_raw)[0]
  url = "https://www.amazon.in/dp/" + product_id
  
  response = requests.get(url, headers= {'User-agent' : 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'})

  price = get_price(response)
  name = get_name(response)

  # Print product name and price 
  if price:
    print("\n")
    print(name)
    print(f"The price of the product is Rs. {price}")
    print(url)
  else:
    print("Price not found")
    
