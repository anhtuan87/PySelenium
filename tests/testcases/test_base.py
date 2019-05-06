import logging
import unittest

import pytest

from selenpy.support import browser
from tests import constant
from tests.pages.login_page import LoginPage


class TestBase(unittest.TestCase):
    
    login_page = LoginPage()

    @pytest.fixture(scope="session", autouse=True)
    def setup(self):
        logging.info("Starting the test on " + str(pytest.browser_name))                
        browser.start_driver(pytest.browser_name, pytest.remote_host)
        browser.maximize_browser()
        browser.open_url(constant.DASHBOARD_URL)
        self.login_page.login(constant.REPOSITORY, constant.VALID_USERNAME, constant.VALID_PASSWORD)
        # Close all browsers when tests have been finished
#         yield        
#         browser.quit_all_browsers()        
