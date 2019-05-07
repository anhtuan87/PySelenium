from selenpy.element.base_element import BaseElement
from selenpy.element.check_box import CheckBox
from selenpy.element.ta_combo_box import TAComboBox
from selenpy.element.text_box import TextBox
from selenpy.support import browser
from tests.pages import common
from tests.pages.general_page import GeneralPage


class DataProfilesPage(GeneralPage):
    
    _txt_profile_name = TextBox("id=txtProfileName")
    _cbb_parent_page = TAComboBox("id=parent")
    _btn_dynamic = "css=input[type='button'][value='{}']"
    _btn_cancel = BaseElement("css=input[type='button'][value='Cancel']")

    def __init__(self):
        pass
    
    def click_button(self, text):
        button = BaseElement(self._btn_dynamic.format(text))
        button.click()
    
    def cancel_add_new(self):
        self._btn_cancel.click()
        self._btn_cancel.wait_for_invisible()
    
    def submit_add_new(self):
        self.click_button("Finish")
        common.wait(1)
    
    def enter_profile_name(self, value):
        self._txt_profile_name.enter(value)
    
    def add_profile_name(self, name):
        self.click_link("Add New")
        self._txt_profile_name.wait_for_visible()
        self.enter_profile_name(name)
        self.submit_add_new()
    
    def delete_profile_name(self, name):
        checkbox = CheckBox("//td[normalize-space()='{}']/preceding-sibling::td//input".format(name))
        checkbox.check()
        self.click_link("Delete")
        browser.accept_alert_popup_text()
        browser.wait_for_page_loaded()
