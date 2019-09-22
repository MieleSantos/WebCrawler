from selenium import webdriver
from collections import namedtuple
from pprint import pprint

class Cult:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://www.cultcampinas.com.br'
        self.box = 'eventbox' #class
        self.type ='typeEventBox'#class
        self.title_box = 'titleEventBox'#titulo
        self.date = 'dateEvent'#class
        self.place='placeEvent'#class
        self.hour = 'hourEvent'#class
        self.descr='descEventBox'#class
        self.event = namedtuple('Event','title type date place hour descr')


    def navigate(self):
        self.driver.get(self.url)

    def _get_boxes(self):
        return self.driver.find_elements.by_class_name(self.box)

    def _get_title(self):
        return self.box.find_element_by_class_name(self.title_box)

    def _get_type(self,box):
        return self.box.find_element_by_class_name(self.type)

    def _get_date(self, box):
        return self.box.find_element_by_class_name(self.date)

    def _get_descr(self, box):
        return self.box.find_element_by_class_name(self.descr)

    def _get_hour(self, box):
        return self.box.find_element_by_class_name(self.hour)
    '''
    def get_all_data(self):
        boxes = self._get_boxs()
        for box in boxes:
            print(box)'''
    #exibindo o titulo
    def get_all_data(self):
        boxes = self._get_boxes()
        for box in boxes:
            yield self.event(self._get_title(box).text,
                             self._get_type(box).text,
                             self._get_date(box).text,
                             self._get_place(box).text,
                             self._get_hour(box).text,
                             self._get_descr(box).text)



ff= webdriver.Firefox()
c = Cult(ff)
c.navigate()
#c.get_all_data()

for event in c.get_all_data():
    print(event)