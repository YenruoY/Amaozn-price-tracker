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
for url in urls:
  
  response = requests.get(url, headers= {'User-agent' : 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'})

  price = get_price(response)
  name = get_price(response)

  # Print product name and price 
  if price:
    print(title)
    print(f"The price of the product is Rs. {price}")
    print(url)
  else:
    print("Price not found")
    
