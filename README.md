# Amazon.in price tracker

My personal project to track prices of products. The goal is to make is script run automatically in a server and when ever the price changes I get a notification in my phone. This way I can save my time and waste it on some other useless stuffs :)

# How does it work 

The script is still in development and hence I'm mentioning **how it should work**.

* The is `.cache` directory that containes JSON file for each of the products with the name of its product ID. 

* There are two main scripts, 
    - **config.py** : adds product to start tracking it, will also have some configuration options
    - **amazon_track.py** : this will track the price of each product that were added previously.

* The `amazon_track.py` script will execute automatically at certain time with the help of **CRON JOBS**, that means it will support only on Linux machines. 

* For notification I'm going to use **NTFY**. Documentation can be found [here](https://docs.ntfy.sh/).

* There will be a `config.py` file that will keep of the other configuration for the script, such as subscribed topic for NTFY.

# How to install it (not completed)

After cloning the repo, first run the `config.py` script. You can add Amazon product links from this script. Onces its done you can execute `amazon_track.py` script to get its current price. 

After adding multiple links, in the `.cache/` folder there will be multiple JSON files, you can open those files to get info of the current product.

~~**Note :** In the product link, anything after product ID is not required. For example : In `https://amazon.in/<product_name>/dp/<product_id>/..` everyting after `../<product_id>` should be removed including the trailing **'/'** character.~~ Not needed now, fixed on 31/01/2024.

# Dependencies 

1. requests
1. BeautifulSoup

# Things to add

1. Add option to add cron job 
1. Function to configure NTFY topic for notification

# Updates

## 31/01/2024

- Added helper functions (moved functions from `amazon_tracker.py` to `helper_functions.py`.
- Added config file that is able to cache product data.
- Now the config file can remove trackers from the product link.

## 3/02/2024

- Added function that will save the current time stamp and current price of the product.
- Performance improvements
