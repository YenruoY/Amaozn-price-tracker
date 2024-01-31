import requests
from bs4 import BeautifulSoup

def get_price(response):

  content = response.content

  # Parse the HTML content with BeautifulSoup
  soup = BeautifulSoup(content, "lxml")

  # Find the element containing the price
  price_element = soup.find("span", class_="priceToPay")
  
  if not price_element:
    price_element = soup.find("span", id="price")

  if not price_element:
    price_element = soup.find("span", class_="a-price")

  # Extract the price text and remove unnecessary characters
  if price_element:
    price_text = price_element.text.split("₹")[1]
    price_text = price_text.replace("₹", "")

    return price_text 
  else:
    return None

def get_name(response):
  content = response.content
  soup = BeautifulSoup(content, "lxml")
  title_element = soup.find("span", id="productTitle")

  return title_element.text.strip()
