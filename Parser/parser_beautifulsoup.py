# pip freeze
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

def get_html(url):
    r= requests.get(url)
    return r.text

def get_total_pages(html):
    soup=BeautifulSoup(html, 'lxml')
    pages=soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages=pages.split('=')[1].split('&')[0]
    return int(total_pages)

def get_page_data(html):
    soup=BeautifulSoup(html, 'lxml')

    ads=soup.find('div', class_='catalog-main catalog_table').find_all('div', class_='item_table-header')

    for ad in ads:
        try:
            title = ad.find('div', class_='title item-description-title').find('h3').text.strip()
        except:
            title=''
        print('title', title)

def main():
    url='https://www.avito.ru/rossiya?s_trg=3&q=macbook'
    base_url="https://www.avito.ru/rossiya?"
    page_part='p='
    query_part='&q=macbook'

    total_pages=get_total_pages(get_html(url))

    for i in range(1, 3):
        url_gen=base_url+page_part+str(i)+query_part
        print(url_gen)
        html=get_html(url_gen)
        get_page_data(html)



    # return url



if __name__=="__main__":
    main()
    # url=main()
    # aaa=get_html(url)
    # # print(aaa)
    # total_pages=get_total_pages(aaa)
    # print(total_pages)