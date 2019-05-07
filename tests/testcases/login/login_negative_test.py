from tests import constant
from tests.pages.login_page import LoginPage
from tests.testcases.login.login_base import LoginBase


class LoginTest(LoginBase):
    
    login_page = LoginPage()
    
    def test_DA_LOGIN_TC002(self): 
        self.login_page.login(constant.REPOSITORY, constant.INVALID_USERNAME, constant.INVALID_PASSWORD)
        assert self.login_page.get_alert_popup_text() == constant.INVALID_USER_AND_PASS_MSG
     
    def test_DA_LOGIN_TC003(self): 
        self.login_page.login(constant.REPOSITORY, constant.VALID_USERNAME, constant.INVALID_PASSWORD)
        assert self.login_page.get_alert_popup_text() == constant.INVALID_USER_AND_PASS_MSG
 
    def tearDown(self):
        self.login_page.accept_alert_popup_text()
