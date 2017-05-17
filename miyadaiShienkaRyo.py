import csv
import urllib.request
from bs4 import BeautifulSoup

# URLの指定
html = urllib.request.urlopen("http://gakumu.of.miyazaki-u.ac.jp/gakumu/allnews")
soup = BeautifulSoup(html, "html.parser")

# テーブルを指定
ul = soup.findAll('ul', class_='category-module')

csvFile = open("miyadai.csv", 'wt', newline = '', encoding = 'utf-8-sig')
writer = csv.writer(csvFile)

try:
    for li_month in ul[0].findAll('li'):
        for month in li_month.findAll('h3'):
            if month.string is not None:
                csvRow = []
                writer.writerow(csvRow)
                csvRow = []
                csvRow.append(month.string)
                writer.writerow(csvRow)
        for li in li_month.findAll('li'):
            csvRow = []
            for span in li.findAll('span'):
                if span.string is not None:
                    csvRow.append(span.string)
            for a in li.findAll('a'):
                if a.string is not None:
                    csvRow.append(a.string)
                    csvRow.append('http:/' + a.get('href'))
                    writer.writerow(csvRow)
finally:
    csvFile.close()
