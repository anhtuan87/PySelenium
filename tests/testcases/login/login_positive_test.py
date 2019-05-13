from tests.pages.dashboard_page import DashboardPage
from tests.pages.login_page import LoginPage
from tests.resources.aut import ui
from tests.testcases.login.login_base import LoginBase
from tests.resources import profile


class LoginTest(LoginBase):
    
    login_page      = LoginPage()
    dashboard_page  = DashboardPage()
    
    def test_DA_LOGIN_TC001(self): 
        self.login_page.login(profile.REPOSITORY, profile.VALID_USERNAME, profile.VALID_PASSWORD)
        self.dashboard_page.wait_for_dashboard_page()
        assert ui.EXECUTION_DASHBOARD_TITLE in self.dashboard_page.get_title()
