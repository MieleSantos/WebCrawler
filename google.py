"""Exemplo de Page Object(PO) no google.com"""

from selenium import webdriver

class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url='http://google.com.br'
        self.search_bar= 'lst-ib'#id
        self.btn_search = 'btnK'#nome
        self.btn_lucky = 'btnI'#nome

    def navigate(self):
        self.driver.get(self.url)
    #fazendo busca no google e clicando no buscar
    def search(self, word='None'):
        self.driver.find_element_by_id(self.search_bar).send_keys(word)
        self.driver.find_element_by_name(self.btn_search).click()

    def lucky(self, word='None'):
        self.driver.find_element_by_id(self.search_bar).send_keys(word)
        self.driver.find_element_by_name(self.btn_lucky).click()


ff=webdriver.Firefox()
g = Google(ff)
g.navigate()
#g.search('Live de python')
g.lucky('Live de Pyhotn')#clica no botao estou com sorte



