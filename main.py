from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

list_home = []
p = []

page = int(input('Сколько страниц спарсить ? '))

for i in range(1, page+1):
    PAGENATOR = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/{page-i}/c37l1700273'
    r = requests.get(PAGENATOR)

    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.findAll('div', class_='info-container')
    link_img = soup.findAll('div', class_='image')

    for item in items:
        list_home.append({
            'Title': item.find('div', class_='title').get_text(strip=True),
            'Description': item.find('div', class_='description').get_text(strip=True),
            'Location': item.find('div', class_='location').get_text(strip=True),
            'Date': item.find('span', class_='date-posted').get_text(strip=True),
            'Price': item.find('div', class_='price').get_text(strip=True),
        })

    for a in link_img:
        col = a.find('img').get("src")
        if col:
            p.append(col)

df = pd.DataFrame(list_home)
df['Image'] = p
df.to_csv('canada_apartaments.csv',sep=';')


