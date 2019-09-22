import requests
from bs4 import BeautifulSoup

url = "http://www.sjc.sp.gov.br/secretarias/mobilidade_urbana/horario-e-itinerario.aspx?acao=p&opcao=1&txt="
r = requests.get(url)


soup = BeautifulSoup(r.text,'lxml')
#obtendo informacoes das tabelas
lista_itinerarios = soup.find_all('table', class_='textosm')
'''
for lista_td in lista_itinerarios:
    print(lista_td.find_all('td'))'''


#exibindo o conteudo de cada tabela
'''for lista_td in lista_itinerarios:
    lista =lista_td.find_all('td')
    for lista_dados in lista:
        print(lista_dados.next_element)'''

for lista_td in lista_itinerarios:
    lista =lista_td.find_all('td')
    for lista_dados in lista:
        if(lista_dados.next_element.name == 'a'):
            url_it = '{0}{1}'.format(url, lista_dados.next_element.get('href'))
            print(url_it)
        else:
            print(lista_dados.next_element)