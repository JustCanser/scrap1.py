from bs4 import BeautifulSoup
import requests

url = 'https://mainfin.ru/currency/tver'
headers = {'user_agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.42' }
req = requests.get(url, headers=headers)
src = req.text
#with open('index.html', 'w', encoding='utf-8') as file:
    #file.write(src)
#with open('index.html') as file:
    #src = file.read()

soup = BeautifulSoup(src, 'lxml')

all_val =soup.find_all('td', class_ = 'mark-text',)
all_name = soup.find_all('td', class_ = 'title usd')
lst = all_val[0:3]
name = all_name[0:3]
all_name = soup.find_all('td', )
lst_name = all_name[0:3]

for item, name in zip(lst, name):
    item_text = (item.text)
    item_name = name.text
    dicti = dict.fromkeys([item_name], item_text)
    print(dicti)
















