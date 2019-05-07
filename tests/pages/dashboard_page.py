from selenpy.element.base_element import BaseElement
from selenpy.element.ta_combo_box import TAComboBox
from selenpy.element.text_box import TextBox
from tests import constant
from tests.pages.general_page import GeneralPage
from tests.pages import common


class DashboardPage(GeneralPage):
    
    _btn_global_setting = BaseElement("css=li.mn-setting > a")
    _txt_page_name = TextBox("id=name")
    _cbb_parent_page = TAComboBox("id=parent")
    _btn_ok = BaseElement("id=OK")
    _btn_cancel = BaseElement("id=Cancel")

    def __init__(self):
        pass
    
    def select_global_setting(self, setting):
        self._btn_global_setting.click()
        self.select_menu(setting)
    
    def cancel_add_page(self):
        self._btn_cancel.click()
        self._btn_cancel.wait_for_invisible()
    
    def submit_add_page(self):
        self._btn_ok.click()
        common.wait(1)
    
    def add_page(self, page_name, parent_page=None):
        self.select_global_setting(constant.GLOBAL_SETTING["add"])
        self._txt_page_name.enter(page_name)
        if parent_page != None:
            self._cbb_parent_page.select_by_visible_text(parent_page)
        self.submit_add_page()
    
    def select_page(self, page_path):
        self.hover_select_menu(page_path)
        self.wait_for_page_loaded()
    
    def edit_page(self, page_path, page_name_new, parent_page_new=None):
        self.select_page(page_path)
        self.select_global_setting(constant.GLOBAL_SETTING["edit"])
        self._txt_page_name.enter(page_name_new)
        if parent_page_new != None:
            self._cbb_parent_page.select_by_visible_text(parent_page_new)
        self.submit_add_page()
    
    def delete_page(self, page_path):
        self.select_page(page_path)
        self.select_global_setting(constant.GLOBAL_SETTING["del"])
        self.accept_alert_popup_text()
    
    def is_page_present(self, page_path):
        return self.is_menu_present(page_path)
