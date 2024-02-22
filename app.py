# from flask import Flask
# from views import views
from bs4 import BeautifulSoup
import requests
from pywebio.output import *
from pywebio import session
from pywebio import start_server
import numpy as np

def app():
    def Extract_CellphoneS(url = None):
        page_to_scrape = requests.get(url)
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")


        def custom_selector(tag):
            return tag.name == "a" and tag.has_attr("class") and "item-linked" in tag.get("class")

        data = soup.findAll(custom_selector)

        product = []
        price = []

        for i in data:
            product.append(i.find("strong").text)
            price.append(i.find("span").text)
        
        shop = ["cellphoneS"] * len(product)

        return np.c_[shop, product, price]

    def Extract_Samcenter(url = None):
        page_to_scrape = requests.get(url, verify=False)
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")


        def price_selector(tag):
            return tag.name == "span" and tag.has_attr("class") and "new-price" in tag.get("class")
        
        def product_selector(tag):
            return tag.name == "span" and tag.has_attr("class") and "main-name" in tag.get("class")

        price = soup.find(price_selector)
        price = price.text

        product = soup.find(product_selector)
        product = product.text

        shop = "SamCenter"

        return [shop, product, price]

    TAB_S9_CELL = "https://cellphones.com.vn/samsung-galaxy-tab-s9-wifi.html"
    TAB_S9_PLUS_CELL = "https://cellphones.com.vn/samsung-galaxy-tab-s9-plus-wifi-512gb.html"
    IPAD_AIR_5_CELL = "https://cellphones.com.vn/ipad-air-5.html"
    TAB_S9_SAM = "https://samcenter.vn/vn/galaxy-tab-s9-wi-fi-128gb"
    TAB_S9_PLUS_SAM = "https://samcenter.vn/vn/galaxy-tab-s9-plus-wifi-256gb"

    # app = Flask(__name__)
    # app.register_blueprint(views, url_prefix = "/")
    def make_table(url = None):
        table = [["Shop", "Product", "Price"]]
        if "cellphone" in url:
            data = Extract_CellphoneS(url)
            for item in data:
                table.append(item)
        else:
            data = Extract_Samcenter(url)
            table.append(data)
        put_table(table)

    put_text("\nTab S9 cellphoneS")
    make_table(TAB_S9_CELL)
    put_text("\nTab S9+ cellphoneS")
    make_table(TAB_S9_PLUS_CELL)
    put_text("\niPad Air 5 cellphoneS")
    make_table(IPAD_AIR_5_CELL)
    put_text("\nTab S9 SamCenter")
    make_table(TAB_S9_SAM)
    put_text("\nTab S9+ SamCenter")
    make_table(TAB_S9_PLUS_SAM)

    session.hold()

if __name__ == '__main__':
	start_server(app, port=32420, debug=True)