from selenium import webdriver

class VegaCalendario():

    def __init__(self,driver):
        self.driver =driver



#url = "https://www.kixeye.com/forum/discussion/715463"



ff= webdriver.Firefox()
#c = VegaCalendario(ff)
#c.navigate()
#c.get_all_data()
ff.get('https://www.kixeye.com/forum/discussion/715463')