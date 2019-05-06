from selenpy.element.base_element import BaseElement
from selenpy.element.combo_box import ComboBox
from selenpy.element.text_box import TextBox
from tests.pages.general_page import GeneralPage


class DashboardPage(GeneralPage):
    
    _btn_global_setting = BaseElement("css=li.mn-setting > a")
    _txt_page_name = TextBox("id=name")
    _cbb_parent_page = ComboBox("id=parent")
    _btn_ok = BaseElement("id=OK")

    def __init__(self):
        pass
    
    def select_global_setting(self, setting):
        self._btn_global_setting.click()
        self.select_menu(setting)
    
    def add_page(self, page_name, parent_page):
        self.select_global_setting("Add Page")
        self._txt_page_name.send_keys(page_name)
        self._cbb_parent_page.select_by_value(parent_page)
        self._btn_ok.click()
