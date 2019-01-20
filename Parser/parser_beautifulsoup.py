# pip freeze
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

def get_html(url):
    r= requests.get(url)
    return r.text

def get_total_pages(html):
    soup=BeautifulSoup(html, 'lxml')
    pages=soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-pages')[-1].get('href')
    tatal_pages=pages.split('=')[1].split('&')[0]
    return int(pages)



def main():
    url="https://www.avito.ru/rossiya?s_trg=3&q=macbook"
    return url



if __name__=="__main__":
    url=main()
    aaa=get_html(url)
    print(aaa)
    total_pages=get_total_pages(aaa)
    print(total_pages)