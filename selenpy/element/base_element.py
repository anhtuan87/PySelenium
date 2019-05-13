from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenpy.common import config
from selenpy.helper.wait import wait_for
from selenpy.support import browser 


class BaseElement():
    __locator = None
    __strategies = None
    __element = None
    
    def __init__(self, locator):
        self.__strategies = {
            'id': self._find_by_id,
            'name': self._find_by_name,
            'xpath': self._find_by_xpath,
            'css': self._find_by_css_selector,
            'class': self._find_by_class_name
        }
        self.__locator = locator
        self.__dynamic_locator = locator
        self.__element = None

    @property
    def _driver(self):
        return browser.get_driver()

    def set_dynamic_value(self, *value):
        self.__locator = self.__dynamic_locator.format(*value)
        self.__element = None

    def find_element(self):
        if self.__element == None:
            prefix, criteria = self.__parse_locator(self.__locator)
            strategy = self.__strategies[prefix]
            self.__element = strategy(criteria)
            self.__locator = self.__dynamic_locator
        return self.__element

    def find_elements(self):
        if self.__element == None:
            prefix, criteria = self.__parse_locator(self.__locator)
            strategy = self.__strategies[prefix]
            self.__element = strategy(criteria, True)
            self.__locator = self.__dynamic_locator
        return self.__element
    
    def click(self):
        self.find_element()
        self.wait_for_visible().click() 
        
    def send_keys(self, *value):
        self.find_element().send_keys(value)
    
    def __parse_locator(self, locator):
        if locator.startswith(('//', '(//')):
            return 'xpath', locator
        index = self.__get_locator_separator_index(locator)
        if index != -1:
            prefix = locator[:index].strip()
            if prefix in self.__strategies:
                return prefix, locator[index + 1:].lstrip()
        return 'default', locator
    
    def __by(self, prefix):
        if prefix == "class": 
            return By.CLASS_NAME 
        elif prefix == "css" : 
            return By.CSS_SELECTOR 
        else:
            return prefix
    
    def __get_locator_separator_index(self, locator):
        if '=' not in locator:
            return locator.find(':')
        if ':' not in locator:
            return locator.find('=')
        return min(locator.find('='), locator.find(':'))
    
    def _find_by_id(self, criteria, match_all=False):
        if match_all:
            return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_all_elements_located((By.ID, criteria)))
        else:
            return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_element_located((By.ID, criteria)))        
    
    def _find_by_name(self, criteria, match_all=False):
        if match_all:
            return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_all_elements_located((By.NAME, criteria)))
        else:
            return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_element_located((By.NAME, criteria)))        
    
    def _find_by_xpath(self, criteria, match_all=False):
        if match_all:
            return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_all_elements_located((By.XPATH, criteria)) and EC.visibility_of_element_located((By.XPATH, criteria)))
        else:
            return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_element_located((By.XPATH, criteria)))       
    
    def _find_by_css_selector(self, criteria, match_all=False):
        if match_all:
            return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, criteria)))
        else:
            return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, criteria)))        
    
    def _find_by_class_name(self, criteria, match_all=False):
        if match_all:
            return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_all_elements_located((By.CLASS_NAME, criteria)))
        else:
            return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_element_located((By.CLASS_NAME, criteria)))        
    
    def is_displayed(self, timeout=None):
        try:
            self.wait_for_visible(timeout)
        except (TimeoutException): 
            return False
        return True
    
    def is_enabled(self):
        return self.find_element().is_enabled()
    
    def is_selected(self):
        return self.find_element().is_selected()
   
    def wait_for_visible(self, timeout=None):
        if timeout == None: timeout = config.timeout            
        prefix, criteria = self.__parse_locator(self.__locator)
        return WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located((self.__by(prefix), criteria)))
        
    def wait_for_invisible(self, timeout=None):
        if timeout == None: timeout = config.timeout            
        prefix, criteria = self.__parse_locator(self.__locator)
        WebDriverWait(self._driver, timeout).until(EC.invisibility_of_element_located((self.__by(prefix), criteria)))
    
    def wait_until(self, element_condition, timeout=None, polling=None):
        if timeout is None:
            timeout = config.timeout
        if polling is None:
            polling = config.poll_during_waits
    
        return wait_for(self.find_element(), element_condition, timeout, polling)
    
    def hover_mouse(self):
        self.wait_for_visible()
        hover = ActionChains(self._driver).move_to_element(self.find_element())
        hover.move_by_offset(1, 1)
        hover.perform()
    
    def get_text(self):
        return self.find_element().text
    
    def are_child_elements_disabled(self, tag_name="*"):
        for element in self.find_element().find_elements_by_tag_name(tag_name):
            if not element.is_enabled():
                return False
        return True
