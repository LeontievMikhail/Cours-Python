# pip freeze
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

def get_html(url):
    r= requests.get(url)
    return r.text
def main():
    # https: // www.avito.ru / rossiya?s_trg = 3 & q = macbook



if __name__=="__main__":
    main()
