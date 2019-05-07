from selenpy.element.base_element import BaseElement
from selenpy.support import browser
from tests import constant
from tests.pages import common


class GeneralPage():
    
    _div_dashboard_header = BaseElement("id=header")
    _link_xpath = "//a[text()='{}']"

    def __init__(self):
        pass
    
    def wait_for_dashboard_page(self):
        self._div_dashboard_header.wait_for_visible(constant.LOADING_TIME)
        browser.wait_for_page_loaded()
    
    def get_title(self):
        return browser.get_driver().title
    
    def click_link(self, text):
        link = BaseElement(self._link_xpath.format(text))
        link.click()
    
    def select_menu(self, dynamic_menu, delimiter="->"):
        items = dynamic_menu.split(delimiter)
        for item in items:
            element = BaseElement(self._link_xpath.format(item.strip()))
            element.click()
    
    def hover_select_menu(self, dynamic_menu, delimiter="->"):
        items = dynamic_menu.split(delimiter)
        for item in items:
            element = BaseElement(self._link_xpath.format(item.strip()))
            element.hover_mouse()
        element.click()
    
    def is_menu_present(self, dynamic_menu, delimiter="->"):
        items = dynamic_menu.split(delimiter)
        try:
            for item in items:
                element = BaseElement(self._link_xpath.format(item.strip()))
                element.hover_mouse()
        except Exception:
            return False
        return element.is_displayed(0)
