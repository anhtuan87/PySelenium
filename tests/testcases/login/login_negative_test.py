from selenpy.support import browser
from tests.pages.login_page import LoginPage
from tests.testcases.login.login_base import LoginBase
from tests.resources.aut import message
from tests.resources import profile


class LoginTest(LoginBase):
    
    login_page      = LoginPage()
    invalid_user    = "abc"
    invalid_pass    = "abc"
    
    def test_DA_LOGIN_TC002(self): 
        self.login_page.login(profile.REPOSITORY, self.invalid_user, self.invalid_pass)
        assert browser.get_alert_popup_text() == message.INVALID_USER_AND_PASS_MSG

    def test_DA_LOGIN_TC003(self): 
        self.login_page.login(profile.REPOSITORY, profile.VALID_USERNAME, self.invalid_pass)
        assert browser.get_alert_popup_text() == message.INVALID_USER_AND_PASS_MSG
 
    def tearDown(self):
        browser.accept_alert_popup_text()
