from tests import constant
from tests.pages.dashboard_page import DashboardPage
from tests.pages.login_page import LoginPage
from tests.testcases.login.login_base import LoginBase


class LoginTest(LoginBase):
    
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    
    def test_DA_LOGIN_TC001(self): 
        self.login_page.login(constant.REPOSITORY, constant.VALID_USERNAME, constant.VALID_PASSWORD)
        self.dashboard_page.wait_for_dashboard_page()
        assert constant.EXECUTION_DASHBOARD_TITLE in self.dashboard_page.get_title()
