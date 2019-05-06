from tests import constant
from tests.pages.dashboard_page import DashboardPage
from tests.pages.login_page import LoginPage
from tests.testcases.test_base import TestBase


class LoginTest(TestBase):
    
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    
    def test_DA_MP_TC021(self): 
        self.dashboard_page.add_page("Page 1", "Overview")
        self.dashboard_page.add_page("Page 2", "Page 1")
#         assert constant.EXECUTION_DASHBOARD_TITLE in self.dashboard_page.get_title()
