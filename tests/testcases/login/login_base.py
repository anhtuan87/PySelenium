import logging

import pytest

from selenpy.support import browser
from tests.resources import profile
from tests.testcases.test_base import TestBase


class LoginBase(TestBase):

    @pytest.fixture(scope="session", autouse=True)
    def setup(self):
        logging.info("Starting the test on " + str(pytest.browser_name))                
        browser.start_driver(pytest.browser_name, pytest.remote_host)
        browser.maximize_browser()
        browser.open_url(profile.DASHBOARD_URL)
        # Close all browsers when tests have been finished
        yield        
        self.base_tear()   
