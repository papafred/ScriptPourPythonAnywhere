import bs4
import re
import urllib.request

website= 'https://fr.cryptonator.com/rates/ETC-EUR'

with urllib.request.urlopen(website) as f:
    data = f.read().decode('utf-8')
    soup = bs4.BeautifulSoup(data, 'html.parser')

ma_soupe=soup.find(class_="liverate")
print (ma_soupe)
for tag in ma_soupe:
    if tag =='EUR':
        print (tag.string)