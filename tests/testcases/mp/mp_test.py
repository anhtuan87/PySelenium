from selenpy.support import browser
from tests import constant
from tests.pages import common
from tests.pages.dashboard_page import DashboardPage
from tests.pages.login_page import LoginPage
from tests.testcases.test_base import TestBase
from tests.resources.aut import message


class MPTest(TestBase):
    
    login_page      = LoginPage()
    dashboard_page  = DashboardPage()
    
    def test_DA_MP_TC021(self):
        page_name_l1 = "Overview" 
        page_name_l2 = common.generate_random_string("Page1_")
        page_name_l3 = common.generate_random_string("Page2_")
        page_name_l2_new = common.generate_random_string("Page3_")
        page_name_l3_new = common.generate_random_string("Page4_")
        self.dashboard_page.add_page(page_name_l2, page_name_l1)
        self.dashboard_page.add_page(page_name_l3, page_name_l2)
        self.dashboard_page.edit_page(constant.PATH_L2_FORMAT.format(page_name_l1, page_name_l2), page_name_l2_new)
        assert self.dashboard_page.is_page_present(constant.PATH_L2_FORMAT.format(page_name_l1, page_name_l2_new))
        self.dashboard_page.edit_page(constant.PATH_L3_FORMAT.format(page_name_l1, page_name_l2_new, page_name_l3), page_name_l3_new)
        assert self.dashboard_page.is_page_present(constant.PATH_L3_FORMAT.format(page_name_l1, page_name_l2_new, page_name_l3_new))
        self.dashboard_page.delete_page(constant.PATH_L3_FORMAT.format(page_name_l1, page_name_l2_new, page_name_l3_new))
        self.dashboard_page.delete_page(constant.PATH_L2_FORMAT.format(page_name_l1, page_name_l2_new))
     
    def test_DA_MP_TC022(self): 
        page_name_l1 = common.generate_random_string("Test1_")
        page_name_l2 = common.generate_random_string("TestChild1_")
        page_path_l2 = constant.PATH_L2_FORMAT.format(page_name_l1, page_name_l2)
        self.dashboard_page.add_page(page_name_l1)
        self.dashboard_page.add_page(page_name_l2, page_name_l1)
        self.dashboard_page.add_page(page_name_l2, page_name_l1)
        assert browser.get_alert_popup_text() == message.CHILD_ALREADY_EXIST_MSG.format(page_name_l2)
        browser.accept_alert_popup_text()
        self.dashboard_page.cancel_add_page()
        self.dashboard_page.delete_page(page_path_l2)
        self.dashboard_page.delete_page(page_name_l1)
      
    def test_DA_MP_TC023(self): 
        page_name_l1 = "Overview" 
        page_name_l2 = common.generate_random_string("Page1_")
        page_name_l3 = common.generate_random_string("Page2_")
        page_name_l2_new = common.generate_random_string("Page3_")
        self.dashboard_page.add_page(page_name_l2, page_name_l1)
        self.dashboard_page.add_page(page_name_l3, page_name_l2)
        self.dashboard_page.edit_page(constant.PATH_L2_FORMAT.format(page_name_l1, page_name_l2), page_name_l2_new)
        assert self.dashboard_page.is_page_present(constant.PATH_L2_FORMAT.format(page_name_l1, page_name_l2_new))
        self.dashboard_page.delete_page(constant.PATH_L3_FORMAT.format(page_name_l1, page_name_l2_new, page_name_l3))
        self.dashboard_page.delete_page(constant.PATH_L2_FORMAT.format(page_name_l1, page_name_l2_new))
     
    def test_DA_MP_TC024(self): 
        page_name_l1 = "Overview" 
        page_name_l2 = common.generate_random_string("Page1_")
        page_name_l3 = common.generate_random_string("Page2_")
        self.dashboard_page.add_page(page_name_l2, page_name_l1)
        self.dashboard_page.add_page(page_name_l3, page_name_l2)
        self.dashboard_page.select_page(constant.PATH_L2_FORMAT.format(page_name_l1, page_name_l2))
        assert page_name_l2 in self.dashboard_page.get_title()
        self.dashboard_page.select_page(constant.PATH_L3_FORMAT.format(page_name_l1, page_name_l2, page_name_l3))
        assert page_name_l3 in self.dashboard_page.get_title()
        self.dashboard_page.delete_page(constant.PATH_L3_FORMAT.format(page_name_l1, page_name_l2, page_name_l3))
        self.dashboard_page.delete_page(constant.PATH_L2_FORMAT.format(page_name_l1, page_name_l2))
