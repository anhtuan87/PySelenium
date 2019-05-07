from selenpy.element.base_element import BaseElement


class TAComboBox(BaseElement):
    
    def __init__(self, locator):
        super().__init__(locator)
        
    def select_by_visible_text(self, text):
        element = self.find_element()
        element.click()
        element_item = element.find_element_by_xpath("//option[contains(text(),'" + text + "')]")
        element_item.click()
