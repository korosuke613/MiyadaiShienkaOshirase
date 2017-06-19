import csv
import urllib.request
from bs4 import BeautifulSoup

def miyadaiOshirase():
    
    # URLの指定
    html = urllib.request.urlopen("http://gakumu.of.miyazaki-u.ac.jp/gakumu/allnews")
    soup = BeautifulSoup(html, "html.parser")
    
    # テーブルを指定
    ul = soup.findAll('ul', class_='category-module')
    
    i = 0
    
    for li_month in ul[0].findAll('li'):
        for li in li_month.findAll('li'):
            for span in li.findAll('span'):
                if span.string is not None:
                    print(span.string)
            for a in li.findAll('a'):
                if a.string is not None:
                    print(a.string.strip())
                    print('http:/' + a.get('href'))
            print("\n")
            i += 1 
            if i >= 5:
                return

import os
if __name__ == "__main__":
    miyadaiOshirase()