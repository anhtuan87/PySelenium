from selenpy.element.base_element import BaseElement
from selenpy.support import browser
from tests import constant


class GeneralPage():
    
    _div_dashboard_header   = BaseElement("id=header")
    
    _btn_by_value           = BaseElement("css=input[type='button'][value='{}']")
    _lnk_by_text            = BaseElement("//a[text()='{}']")
    
    def __init__(self):
        pass
    
    def wait_for_dashboard_page(self):
        self._div_dashboard_header.wait_for_visible(constant.LOADING_TIME)
        browser.wait_for_page_loaded(constant.LOADING_TIME)
    
    def get_title(self):
        return browser.get_driver().title
    
    def click_link(self, text):
        link = self._lnk_by_text
        link.set_dynamic_value(text)
        link.click()
    
    def click_button_by_value(self, value):
        button = self._btn_by_value
        button.set_dynamic_value(value)
        button.click()
    
    def select_menu(self, dynamic_menu, delimiter="->"):
        items = dynamic_menu.split(delimiter)
        for item in items:
            link = self._lnk_by_text
            link.set_dynamic_value(item.strip())
            link.click()
    
    def hover_select_menu(self, dynamic_menu, delimiter="->"):
        items = dynamic_menu.split(delimiter)
        for item in items:
            element = self._lnk_by_text
            element.set_dynamic_value(item.strip())
            element.hover_mouse()
        element.click()
    
    def is_menu_present(self, dynamic_menu, delimiter="->"):
        items = dynamic_menu.split(delimiter)
        try:
            for item in items:
                element = self._lnk_by_text
                element.set_dynamic_value(item.strip())
                element.hover_mouse()
        except Exception:
            return False
        return element.is_displayed(0)
