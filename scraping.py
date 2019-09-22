#Baixando arquivos e ,amipulando datas/web scraping

from requests import get

x =get('http://www.google.com')

print(x.headers)

