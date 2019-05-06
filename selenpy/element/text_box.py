from selenpy.element.base_element import BaseElement


class TextBox(BaseElement):
    
    def __init__(self, locator):
        super().__init__(locator)
        
    def clear(self):
        self.find_element().clear()
