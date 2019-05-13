import time

from selenpy.support import browser
from tests import constant
from tests.pages import common
from tests.pages.dashboard_page import DashboardPage
from tests.pages.data_profiles_page import DataProfilesPage
from tests.pages.login_page import LoginPage
from tests.pages.panel_page import PanelPage
from tests.resources.aut import ui, message
from tests.testcases.test_base import TestBase


class PanelTest(TestBase):
    
    login_page          = LoginPage()
    dashboard_page      = DashboardPage()
    panel_page          = PanelPage()
    data_profiles_page  = DataProfilesPage()
   
    def test_PANEL_TC027(self):
        page_name = common.generate_random_string("Page1")
        panel_name = common.generate_random_string("zbox")
        self.dashboard_page.add_page(page_name) 
        self.dashboard_page.add_panel(panel_name)
        self.dashboard_page.open_choose_panels()
        for type, panel_list in ui.DEFAULT_PANELS.items():
            actual_panels = self.dashboard_page.get_list_panels(type)
            if type == "Charts":
                new_panel_list = panel_list
                new_panel_list.append(panel_name)
                assert common.is_list_contained(actual_panels, new_panel_list)
            else:
                assert common.is_list_contained(actual_panels, panel_list)
        self.dashboard_page.hide_choose_panels()
        self.dashboard_page.delete_page(page_name)
        self.dashboard_page.select_menu(self.dashboard_page.PANEL_MENU)
        self.panel_page.delete_panel(panel_name)
     
    def test_PANEL_TC028(self): 
        self.dashboard_page.select_menu(self.dashboard_page.PANEL_MENU)
        self.dashboard_page.click_link("Add New")
        assert self.dashboard_page.is_dashboard_locked()
        self.panel_page.cancel()
       
    def test_PANEL_TC030(self): 
        invalid_panel_name = "Logigear#$%"
        valid_panel_name = common.generate_random_string("Logigear@")
        self.dashboard_page.select_menu(self.dashboard_page.PANEL_MENU)
        self.panel_page.add_panel(invalid_panel_name)
        assert browser.get_alert_popup_text() == message.INVALID_DISPLAY_NAME_MSG
        browser.accept_alert_popup_text()
        self.panel_page.cancel()
        self.panel_page.add_panel(valid_panel_name, "Name")
        assert self.panel_page.is_panel_present(valid_panel_name)
        self.panel_page.delete_panel(valid_panel_name)
      
    def test_PANEL_TC031(self): 
        self.dashboard_page.select_menu(self.dashboard_page.PANEL_MENU)
        self.panel_page.click_link("Add New")
        assert self.panel_page.get_chart_panel_legend() == "Chart Settings"
        self.panel_page.select_type("Indicator")
        assert self.panel_page.get_chart_panel_legend() == "Indicator Settings"
        self.panel_page.select_type("Report")
        assert self.panel_page.is_chart_panel_present() == False
        self.panel_page.select_type("Heat Map")
        assert self.panel_page.get_chart_panel_legend() == "Heat Map Settings"
        self.panel_page.cancel()
     
    def test_PANEL_TC033(self):
        panel_name = common.generate_random_string() 
        self.dashboard_page.select_menu(self.dashboard_page.PANEL_MENU)
        self.panel_page.click_link("Add New")
        assert self.panel_page.is_data_profiles_sorted()
        self.panel_page.cancel()
        self.panel_page.add_panel(panel_name, "Name")
        self.panel_page.select_panel_action(panel_name, "Edit")
        assert self.panel_page.is_data_profiles_sorted()
        self.panel_page.cancel()
        self.panel_page.delete_panel(panel_name)
    
    def test_PANEL_TC034(self):
        profile_name = common.generate_random_string()
        panel_name = common.generate_random_string() 
        self.dashboard_page.select_menu(self.dashboard_page.DATA_PROFILES_MENU)
        self.data_profiles_page.add_profile(profile_name)
        self.dashboard_page.select_menu(self.dashboard_page.PANEL_MENU)
        self.panel_page.click_link("Add New")
        assert self.panel_page.is_data_profiles_contained(profile_name)
        assert self.panel_page.is_data_profiles_sorted()
        self.panel_page.cancel()
        self.panel_page.add_panel(panel_name, "Name")
        self.panel_page.select_panel_action(panel_name, "Edit")
        assert self.panel_page.is_data_profiles_contained(profile_name)
        assert self.panel_page.is_data_profiles_sorted()
        self.panel_page.cancel()
        self.panel_page.delete_panel(panel_name)
        self.dashboard_page.select_menu(self.dashboard_page.DATA_PROFILES_MENU)
        self.data_profiles_page.delete(profile_name)
