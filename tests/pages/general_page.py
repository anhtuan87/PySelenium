import logging
import time

from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenpy.common import config
from selenpy.element.base_element import BaseElement
from selenpy.support import browser
from tests import constant
from tests.pages import common


class GeneralPage():
    
    _div_dashboard_header = BaseElement("id=header")

    def __init__(self):
        pass
    
    def wait_for_dashboard_page(self):
        self._div_dashboard_header.wait_for_visible(constant.LOADING_TIME)
        self.wait_for_page_loaded()
    
    def get_title(self):
#         time.sleep(1)
        return browser.get_driver().title
    
    def select_menu(self, dynamic_menu):
        items = dynamic_menu.split("/")
        str = "//a[text()='%']"
        for item in items:
            str_replace = str.replace("%", item)
            element = browser.get_driver().find_element_by_xpath(str_replace)
            element.click()
   
    def wait_for_alert_popup(self, timeout=None):
        if timeout is None:
            timeout = config.timeout
        try:
            WebDriverWait(browser.get_driver(), timeout).until(EC.alert_is_present())
            return browser.get_driver().switch_to.alert
        except TimeoutException:
            return False 

    def get_alert_popup_text(self):
        try:
            alertPopup = self.wait_for_alert_popup()
            return alertPopup.text
        except NoAlertPresentException:
            logging.warning("Alert does not exist")

    def accept_alert_popup_text(self):
        try:
            alertPopup = self.wait_for_alert_popup()
            alertPopup.accept()
        except NoAlertPresentException:
            logging.warning("Alert does not exist")

    def wait_for_page_loaded(self):
        pageLoaded = ""
        count = 0
        while (pageLoaded != "complete" and count <= constant.LOADING_TIME):
            common.wait(0.5)
            pageLoaded = browser.get_driver().execute_script("return document.readyState")
            count += 1
        if (count > constant.LOADING_TIME):
            logging.warning("Page is not loaded completely in " + str(constant.LOADING_TIME) + " seconds")
