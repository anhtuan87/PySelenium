import logging
import unittest

import pytest

from selenpy.support import browser
from tests.pages.login_page import LoginPage
from tests.resources import profile


class TestBase(unittest.TestCase):
    
    login_page = LoginPage()

    def base_setup(self):
        logging.info("Starting the test on " + str(pytest.browser_name))                
        browser.start_driver(pytest.browser_name, pytest.remote_host)
        browser.maximize_browser()
        browser.open_url(profile.DASHBOARD_URL)
        self.login_page.login(profile.REPOSITORY, profile.VALID_USERNAME, profile.VALID_PASSWORD)

    def base_tear(self):
        browser.quit_all_browsers() 
        
    @pytest.fixture(scope="session", autouse=True)
    def setup(self):
        self.base_setup()
        # Close all browsers when tests have been finished
        yield        
        self.base_tear()
