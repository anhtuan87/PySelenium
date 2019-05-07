from tests import constant
from tests.pages.dashboard_page import DashboardPage
from tests.pages.login_page import LoginPage
from tests.testcases.test_base import TestBase


class MPTest(TestBase):
    
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    
    def test_DA_MP_TC021(self): 
        self.dashboard_page.add_page("Page1", "Overview")
        self.dashboard_page.add_page("Page2", "Page1")
        self.dashboard_page.edit_page("Overview->Page1", "Page3")
        assert self.dashboard_page.is_page_present("Overview->Page3")
        self.dashboard_page.edit_page("Overview->Page3->Page2", "Page4")
        assert self.dashboard_page.is_page_present("Overview->Page3->Page4")
        self.dashboard_page.delete_page("Overview->Page3->Page4")
        self.dashboard_page.delete_page("Overview->Page3")
     
    def test_DA_MP_TC022(self): 
        self.dashboard_page.add_page("Test1")
        self.dashboard_page.add_page("TestChild1", "Test1")
        self.dashboard_page.add_page("TestChild1", "Test1")
        assert self.login_page.get_alert_popup_text() == constant.CHILD_ALREADY_EXIST_MSG.format("TestChild1")
        self.dashboard_page.accept_alert_popup_text()
        self.dashboard_page.cancel_add_page()
        self.dashboard_page.delete_page("Test1->TestChild1")
        self.dashboard_page.delete_page("Test1")
     
    def test_DA_MP_TC023(self): 
        self.dashboard_page.add_page("Page1", "Overview")
        self.dashboard_page.add_page("Page2", "Page1")
        self.dashboard_page.edit_page("Overview->Page1", "Page3")
        assert self.dashboard_page.is_page_present("Overview->Page3")
        self.dashboard_page.delete_page("Overview->Page3->Page2")
        self.dashboard_page.delete_page("Overview->Page3")
    
    def test_DA_MP_TC024(self): 
        self.dashboard_page.add_page("Page1", "Overview")
        self.dashboard_page.add_page("Page2", "Page1")
        self.dashboard_page.select_page("Overview->Page1")
        assert "Page1" in self.dashboard_page.get_title()
        self.dashboard_page.select_page("Overview->Page1->Page2")
        assert "Page2" in self.dashboard_page.get_title()
        self.dashboard_page.delete_page("Overview->Page1->Page2")
        self.dashboard_page.delete_page("Overview->Page1")
