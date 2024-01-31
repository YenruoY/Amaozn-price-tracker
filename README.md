# Amazon.in price tracker

My personal project to track prices of products. The goal is to make is script run automatically in a server and when ever the price changes I get a notification in my phone. This way I can save my time and waste it on some other useless stuffs :)

# How does it work 

The script is still in development and hence I'm mentioning **how it should work**.

* There will be a `url.list` file that will contain link, and target price of the products I want to track. The file will be in JSON format.

* The script scrapes the product price from their product page.

* The script will execute automatically at certain time with the help of **CRON JOBS**, that means it will support only on Linux machines. 

* For notification I'm going to use **NTFY**. Documentation can be found [here](https://docs.ntfy.sh/).

* There will be a `config` file that will keep of the other configuration for the script, such as subscribed topic for NTFY.

# How to install it

Work in progress.

For now, add product link inside the URL veriable in the script. 

~~**Note :** In the product link, anything after product ID is not required. For example : In `https://amazon.in/<product_name>/dp/<product_id>/..` everyting after `../<product_id>` should be removed including the trailing **'/'** character.~~ Not needed now, fixed on 31/01/2024.

# Dependencies 

1. requests
1. BeautifulSoup

# Things to add

1. `url.list` file and a function to read the file
1. `config` file and a function to read the file
1. Add option to add cron job 

# Updates

## 31/01/2024

- Added helper functions (moved functions from `amazon_tracker.py` to `helper_functions.py`.
- Added config file that is able to cache product data.
- Now the config file can remove trackers from the product link.
