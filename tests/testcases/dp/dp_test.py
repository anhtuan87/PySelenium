from tests import constant
from tests.pages.dashboard_page import DashboardPage
from tests.pages.data_profiles_page import DataProfilesPage
from tests.pages.login_page import LoginPage
from tests.testcases.test_base import TestBase
from tests.pages import common
from selenpy.support import browser


class DPTest(TestBase):
    
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    data_profiles_page = DataProfilesPage()
    
    def test_DA_DP_TC069(self): 
        self.dashboard_page.select_menu("Administer->Data Profiles")
        self.dashboard_page.click_link("Add New")
        self.data_profiles_page.click_button("Next")
        assert browser.get_alert_popup_text() == constant.MISSING_PROFILE_NAME_MSG
        browser.accept_alert_popup_text()
        self.data_profiles_page.click_button("Finish")
        assert browser.get_alert_popup_text() == constant.MISSING_PROFILE_NAME_MSG
        browser.accept_alert_popup_text()
        self.data_profiles_page.cancel_add_new()
  
    def test_DA_DP_TC070(self): 
        self.dashboard_page.select_menu("Administer->Data Profiles")
        self.dashboard_page.click_link("Add New")
        self.data_profiles_page.enter_profile_name(constant.SPECIAL_CHARS)
        self.data_profiles_page.click_button("Finish")
        assert browser.get_alert_popup_text() == constant.INVALID_PROFILE_NAME_MSG
        browser.accept_alert_popup_text()
        self.data_profiles_page.cancel_add_new()

    def test_DA_DP_TC071(self): 
        tc_profile_name = common.generate_random_string()
        self.dashboard_page.select_menu("Administer->Data Profiles")
        self.data_profiles_page.add_profile_name(tc_profile_name)
        self.data_profiles_page.add_profile_name(tc_profile_name)
        assert browser.get_alert_popup_text() == constant.PROFILE_ALREADY_EXIST_MSG
        browser.accept_alert_popup_text()
        self.data_profiles_page.cancel_add_new()
        self.data_profiles_page.delete_profile_name(tc_profile_name)
