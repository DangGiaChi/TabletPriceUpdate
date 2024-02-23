from flask import Flask
from pywebio.platform.flask import webio_view
from bs4 import BeautifulSoup
import requests
from pywebio.output import *
from pywebio import session
import numpy as np
from webscraping import make_table

app = Flask(__name__)

def main():
    session.set_env(title="Tablet Prices Update")
    

    TAB_S9_CELL = "https://cellphones.com.vn/samsung-galaxy-tab-s9-wifi.html"
    TAB_S9_PLUS_CELL = "https://cellphones.com.vn/samsung-galaxy-tab-s9-plus-wifi-512gb.html"
    IPAD_AIR_5_CELL = "https://cellphones.com.vn/ipad-air-5.html"
    TAB_S9_SAM = "https://samcenter.vn/vn/galaxy-tab-s9-wi-fi-128gb"
    TAB_S9_PLUS_SAM = "https://samcenter.vn/vn/galaxy-tab-s9-plus-wifi-256gb"
    TAB_S9_PLUS_5G = "https://samcenter.vn/vn/galaxy-tab-s9-plus-5g-256gb"

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
    put_text("\nTab S9+ 5G SamCenter")
    make_table(TAB_S9_PLUS_5G)

    session.hold()

app.add_url_rule("/", "webio_view", webio_view(main), methods = ["GET", "POST"])

if __name__ == '__main__':
    app.run(debug = True, port = 8000)