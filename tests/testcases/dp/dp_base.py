import pytest

from tests.pages.dashboard_page import DashboardPage
from tests.testcases.test_base import TestBase


class DPBase(TestBase):
    
    dashboard_page      = DashboardPage()

    @pytest.fixture(scope="session", autouse=True)
    def setup(self):
        self.base_setup()
        self.dashboard_page.select_menu(self.dashboard_page.DATA_PROFILES_MENU)
        # Close all browsers when tests have been finished
        yield        
#         self.base_tear()