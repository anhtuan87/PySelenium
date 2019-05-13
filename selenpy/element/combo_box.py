import random

from selenium.webdriver.support.ui import Select

from selenpy.element.base_element import BaseElement


class ComboBox(BaseElement):
    
    def __init__(self, locator):
        super().__init__(locator)    
    
    @property
    def _select(self):
        return Select(self.find_element())
    
    @property
    def first_selected_text(self):        
        return self._select.first_selected_option.text
    
    @property
    def items(self):
        items = []
        for opt in self._select.options:
            items.append(opt.text)
        return items

    def select_by_value(self, value):        
        self._select.select_by_value(value)
        
    def select_by_index(self, idx):    
        self._select.select_by_index(idx)
        
    def select_by_visible_text(self, text):
        self._select.select_by_visible_text(text)
    
    def get_random_item(self):
        if type(self.items) == str:
            return self.items
        else:
            return random.choice(self.items)
