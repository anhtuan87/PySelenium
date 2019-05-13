from selenpy.element.base_element import BaseElement
from selenpy.element.check_box import CheckBox
from selenpy.element.combo_box import ComboBox
from selenpy.element.ta_combo_box import TAComboBox
from selenpy.element.text_box import TextBox
from selenpy.support import browser
from tests import constant
from tests.pages import common
from tests.pages.general_page import GeneralPage


class DataProfilesPage(GeneralPage):
    
    _txt_profile_name       = TextBox("id=txtProfileName")
    _cbb_parent_page        = TAComboBox("id=parent")
    _btn_cancel             = BaseElement("css=input[type='button'][value='Cancel']")
    _cbb_item_type          = ComboBox("id=cbbEntityType")
    _cbb_related_data       = ComboBox("id=cbbSubReport")
    _td_data_profile        = BaseElement("css=#ccontent table td:nth-of-type(2)")
    _lnk_profile_by_text    = BaseElement("//td[a[normalize-space()='{}']]")
    _lnk_field              = BaseElement("//li[text()='{}']")
    _div_field_header       = BaseElement("css=#profilesettings .profilesettingheader")

    def __init__(self):
        pass
    
    def cancel(self):
        self._btn_cancel.click()
        self._btn_cancel.wait_for_invisible()
    
    def submit(self):
        self.click_button_by_value("Finish")
        common.wait(1)
    
    def enter_profile_name(self, value):
        self._txt_profile_name.enter(value)
    
    def add_profile(self, name, profile_data=None):
        self.click_link("Add New")
        self.enter_profile_name(name)
        if profile_data != None:
            txt_element = TextBox("//td[contains(normalize-space(),'{}')]/following-sibling::td//input")
            cbb_element = ComboBox("//td[contains(normalize-space(),'{}')]/following-sibling::td//select")
            cbk_element = CheckBox("//label[normalize-space()='{}']/input")
            for field, data in profile_data.items():
                self.select_field(field)
                for item in data:
                    if item["type"] == "EDITABLE":
                        txt_element.set_dynamic_value(item["field"])
                        txt_element.enter(item["value"])  
                    elif item["type"] == "SELECTABLE":
                        cbb_element.set_dynamic_value(item["field"])
                        cbb_element.select_by_visible_text(item["value"])  
                    elif item["type"] == "CHECKBOX":
                        cbk_element.set_dynamic_value(item["field"])
                        cbk_element.set(item["value"]) 
        self.submit()
    
    def open(self, name):
        profile_link = self._lnk_profile_by_text
        profile_link.set_dynamic_value(name)
        profile_link.click()
    
    def delete(self, name):
        checkbox = CheckBox("//td[normalize-space()='{}']/preceding-sibling::td//input".format(name))
        checkbox.check()
        self.click_link("Delete")
        browser.accept_alert_popup_text()
        browser.wait_for_page_loaded()
    
    def select_field(self, field):
        field_link = self._lnk_field
        field_link.set_dynamic_value(field)
        field_link.click()
        browser.wait_for_page_loaded()
    
    def is_field_page_displayed(self, field):
        if self._div_field_header.is_displayed():
            return self._div_field_header.get_text() == field
        else:
            return False 
        
    def select_item_type(self, type):
        self._cbb_item_type.select_by_visible_text(type.lower())
        common.wait(0.5)
    
    def get_item_type(self):
        return self._cbb_item_type.items
    
    def get_related_data(self):
        return self._cbb_related_data.items
    
    def get_data_profiles_list(self):
        dps = []
        for dp in self._td_data_profile.find_elements():
            dps.append(dp.text)
        return dps
