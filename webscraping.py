from bs4 import BeautifulSoup
import requests
import numpy as np
from pywebio.output import *

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

def make_table(url = None):
        table = [["Shop", "Product", "Price"]]
        if "cellphone" in url:
            data = Extract_CellphoneS(url)
            for item in data:
                table.append([item[0], put_html('<a target = "_blank" href = "{}">{}</a>'.format(url, item[1])), item[2]])
        else:
            data = Extract_Samcenter(url)
            table.append([data[0], put_html('<a target = "_blank" href = "{}">{}</a>'.format(url, data[1])), data[2]])
        put_table(table)