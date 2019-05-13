from selenpy.element.combo_box import ComboBox


class TAComboBox(ComboBox):
    
    def __init__(self, locator):
        super().__init__(locator)
        
    def select_by_visible_text(self, text):
        for opt in self._select.options:
            if text in opt.text:
                opt.click()
                break
