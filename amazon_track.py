import requests
from bs4 import BeautifulSoup

def get_amazon_price(url):

  # Send HTTP request and get the HTML content
  response = requests.get(url, headers= {'User-agent' : 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'})

  content = response.content

  # Parse the HTML content with BeautifulSoup
  soup = BeautifulSoup(content, "lxml")

  # Find the element containing the price
  price_element = soup.find("span", class_="priceToPay")
  title_element = soup.find("span", id="productTitle")
  
  if not price_element:
    price_element = soup.find("span", id="price")

  if not price_element:
    price_element = soup.find("span", class_="a-price")

  # Extract the price text and remove unnecessary characters
  if price_element:
    price_text = price_element.text.split("₹")[1]
    price_text = price_text.replace("₹", "")

    return [price_text, title_element.text.strip()]
  else:
    return None


# Sample product URL
################################
#   Add URL below inside ""
################################
urls = [
        "",
        ""]

# Get the price using the function
for url in urls:
    price, title = get_amazon_price(url)

    # Print product name and price 
    if price:
        print(title)
        print(f"The price of the product is Rs. {price}")
    else:
        print("Price not found")
    
