from bs4 import BeautifulSoup
import requests
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

    return product, price

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

    return product, price

product_tab_s9, price_tab_s9 = Extract_CellphoneS("https://cellphones.com.vn/samsung-galaxy-tab-s9-wifi.html")
for pro, pri in zip(product_tab_s9, price_tab_s9):
    print(pro + " - " + pri)

print("-------------------------------")

product_tab_s9_plus, price_tab_s9_plus = Extract_CellphoneS("https://cellphones.com.vn/samsung-galaxy-tab-s9-plus-wifi-512gb.html")
for pro, pri in zip(product_tab_s9_plus, price_tab_s9_plus):
    print(pro + " - " + pri)   

print("-------------------------------")

product_ipad_air_5, price_ipad_air_5 = Extract_CellphoneS("https://cellphones.com.vn/ipad-air-5.html")
for pro, pri in zip(product_ipad_air_5, price_ipad_air_5):
    print(pro + " - " + pri)   

print("-------------------------------")

sproduct_tab_s9, sprice_tab_s9 = Extract_Samcenter("https://samcenter.vn/vn/galaxy-tab-s9-wi-fi-128gb")
print(sproduct_tab_s9 + " - " + sprice_tab_s9)

print("-------------------------------")

sproduct_tab_s9_plus, sprice_tab_s9_plus = Extract_Samcenter("https://samcenter.vn/vn/galaxy-tab-s9-plus-wifi-256gb")
print(sproduct_tab_s9_plus + " - " + sprice_tab_s9_plus)