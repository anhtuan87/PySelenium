from selenpy.support import browser
from tests import constant
from tests.pages import common
from tests.pages.dashboard_page import DashboardPage
from tests.pages.data_profiles_page import DataProfilesPage
from tests.pages.login_page import LoginPage
from tests.resources.aut import ui, message
from tests.testcases.dp.dp_base import DPBase
from tests.resources.data import data_profiles


class DPTest(DPBase):
    
    login_page          = LoginPage()
    dashboard_page      = DashboardPage()
    data_profiles_page  = DataProfilesPage()
    
#     def test_DA_DP_TC069(self): 
#         self.dashboard_page.click_link("Add New")
#         self.data_profiles_page.click_button("Next")
#         assert browser.get_alert_popup_text() == message.MISSING_PROFILE_NAME_MSG
#         browser.accept_alert_popup_text()
#         self.data_profiles_page.click_button("Finish")
#         assert browser.get_alert_popup_text() == message.MISSING_PROFILE_NAME_MSG
#         browser.accept_alert_popup_text()
#         self.data_profiles_page.cancel()
#    
#     def test_DA_DP_TC070(self):
#         self.dashboard_page.click_link("Add New")
#         self.data_profiles_page.enter_profile_name(constant.SPECIAL_CHARS)
#         self.data_profiles_page.click_button("Finish")
#         assert browser.get_alert_popup_text() == message.INVALID_PROFILE_NAME_MSG
#         browser.accept_alert_popup_text()
#         self.data_profiles_page.cancel()
#  
#     def test_DA_DP_TC071(self): 
#         profile_name = common.generate_random_string()
#         self.data_profiles_page.add_profile(profile_name)
#         self.data_profiles_page.add_profile(profile_name)
#         assert browser.get_alert_popup_text() == message.PROFILE_ALREADY_EXIST_MSG
#         browser.accept_alert_popup_text()
#         self.data_profiles_page.cancel()
#         self.data_profiles_page.delete(profile_name)
# 
#     def test_DA_DP_TC072_073(self): 
#         self.dashboard_page.click_link("Add New")
#         assert common.is_list_contained(self.data_profiles_page.get_item_type(), ui.GENERAL_SETTINGS_DROPDOWN["Item Type"])
#         self.data_profiles_page.cancel()
#  
#     def test_DA_DP_TC065_067(self):        
#         data_profiles = self.data_profiles_page.get_data_profiles_list()
#         assert common.is_list_contained(data_profiles, ui.DEFAULT_DATA_PROFILES)
#         assert common.is_list_sorted(data_profiles)
#  
#     def test_DA_DP_TC074(self): 
#         self.dashboard_page.click_link("Add New")
#         for type, data in ui.GENERAL_SETTINGS_DROPDOWN["Related Data"].items():
#             self.data_profiles_page.select_item_type(type)
#             assert common.is_list_contained(self.data_profiles_page.get_related_data(), data)
#         self.data_profiles_page.cancel()
#   
    def test_DA_DP_TC076(self): 
        profile_name = common.generate_random_string()
        self.data_profiles_page.add_profile(profile_name, data_profiles.DA_DP_TC076)
        self.data_profiles_page.open(profile_name)
        for field in ui.DATA_PROFILE_FIELDS:
            self.data_profiles_page.select_field(field)
            assert self.data_profiles_page.is_field_page_displayed(field)
        self.data_profiles_page.cancel()
        self.data_profiles_page.delete(profile_name)
#   
#     def test_DA_DP_TC081(self): 
#         profile_name = common.generate_random_string()
#         self.data_profiles_page.add_profile(profile_name)
#         self.data_profiles_page.open(profile_name)
#         for field in ui.DATA_PROFILE_FIELDS:
#             self.data_profiles_page.select_field(field)
#             assert self.data_profiles_page.is_field_page_displayed(field)
#         self.data_profiles_page.cancel()
