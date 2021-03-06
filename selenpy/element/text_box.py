from selenpy.element.base_element import BaseElement


class TextBox(BaseElement):
    
    def __init__(self, locator):
        super().__init__(locator)
        
    def clear(self):
        self.find_element().clear()
        
    def enter(self, value):
        self.find_element()
        element = self.wait_for_visible()
        element.clear()
        element.send_keys(value)
