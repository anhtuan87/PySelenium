import unittest
import pytest

from selenpy.support import browser
import logging

from tests import constant

class LoginBase(unittest.TestCase):

    @pytest.fixture(scope="session", autouse=True)
    def setup(self):
        logging.info("Starting the test on " + str(pytest.browser_name))                
        browser.start_driver(pytest.browser_name, pytest.remote_host)
        browser.maximize_browser()
        browser.open_url(constant.DASHBOARD_URL)
        # Close all browsers when tests have been finished
        yield        
        browser.quit_all_browsers()        
