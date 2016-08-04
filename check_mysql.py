#test de kanab car si un tombe tous tombe !
import bs4
import re
import urllib.request

website= 'http://kanab.fr/'
#website='http://littlewonders.fr/'

try:
    with urllib.request.urlopen(website) as f:
        data = f.read().decode('utf-8')
        soup = bs4.BeautifulSoup(data, 'html.parser')

    print(soup.title.string)
    if soup.title.string == ' Kanab':
        print("OK > ### Le site est en ligne ###")
    else:
        print("KO > ### Le titre du site ne correspond pas ###")

except :
    print ("Erreur 500")