import logging
import time

from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenpy.common import config
from selenpy.helper.wait import wait_for
from selenpy.support import factory


def get_driver():
    return factory.get_shared_driver()


def maximize_browser():
    get_driver().maximize_window()

        
def open_url(url):
    get_driver().get(url)    


def switch_to_driver(driver_key="default"):
    factory.switch_to_driver(driver_key)


def close_browser():
    factory.close_browser()


def quit_all_browsers():
    factory.quit_all_browsers()


def start_driver(name, remote_host, key="default"):
    factory.start_driver(name, remote_host, key)


def wait_until(webdriver_condition, timeout=None, polling=None):
    if timeout is None:
        timeout = config.timeout
    if polling is None:
        polling = config.poll_during_waits

    return wait_for(get_driver(), webdriver_condition, timeout, polling)


def wait_for_alert_popup(timeout=None):
    if timeout is None:
        timeout = config.timeout
    try:
        WebDriverWait(get_driver(), timeout).until(EC.alert_is_present())
        return get_driver().switch_to.alert
    except TimeoutException:
        return False 


def get_alert_popup_text():
    try:
        alertPopup = wait_for_alert_popup()
        return alertPopup.text
    except NoAlertPresentException:
        logging.warning("Alert does not exist")


def accept_alert_popup_text():
    try:
        alertPopup = wait_for_alert_popup()
        alertPopup.accept()
        time.sleep(1)
    except NoAlertPresentException:
        logging.warning("Alert does not exist")

    
def is_page_complete():
    page_status = get_driver().execute_script('return document.readyState=="complete";')
    jquery_status = get_driver().execute_script('return jQuery.active == 0;')
    return page_status and jquery_status


def wait_for_page_loaded(timeout=None):
    if timeout == None: timeout = config.timeout 
    count = 0
    while (not is_page_complete() and count <= timeout):
        time.sleep(1)
        count += 1
