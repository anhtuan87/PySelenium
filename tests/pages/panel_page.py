import random

from selenpy.element.base_element import BaseElement
from selenpy.element.check_box import CheckBox
from selenpy.element.ta_combo_box import TAComboBox
from selenpy.element.text_box import TextBox
from selenpy.support import browser
from tests.pages import common
from tests.pages.general_page import GeneralPage


class PanelPage(GeneralPage):
    
    _txt_display_name           = TextBox("id=txtDisplayName")
    _btn_cancel                 = BaseElement("css=div#div_panelPopup input[type='button'][value='Cancel']")
    _btn_ok                     = BaseElement("css=div#div_panelPopup input[type='button'][value='OK']")
    _cbb_series                 = TAComboBox("id=cbbSeriesField")
    _cbb_data_profiles          = TAComboBox("id=cbbProfile")
    _link_delete                = BaseElement("//div/a[text()='Delete']")
    _lnk_panel_name_by_text     = BaseElement("//td[a[normalize-space()='{}']]")
    _lnk_panel_action_by_text   = BaseElement("//td[a[normalize-space()='{}']]/following-sibling::td//a[text()='{}']")
    _cbk_panel_by_text          = CheckBox("//td[a[normalize-space()='{}']]/preceding-sibling::td//input")
    _lbl_chart_panel_setting    = BaseElement("css=fieldset#fdSettings legend")
    _rdo_type_by_text           = BaseElement("//table[@id='infoSettings']//label[input and normalize-space()='{}']")
    _dlg_add_new_panel          = BaseElement("css=.ui-dialog-container #ui-dialog-title-div_panelPopup")
    _dlg_panel_config           = BaseElement("css=.ui-dialog-container #ui-dialog-title-div_panelConfigurationDlg")

    def __init__(self):
        pass
    
    def cancel(self):
        self._btn_cancel.click()
        self._btn_cancel.wait_for_invisible()
    
    def submit(self):
        self._btn_ok.click()
        common.wait(1)
    
    def enter_display_name(self, value):
        self._txt_display_name.enter(value)
    
    def add_panel(self, name, series=None):
        self.click_link("Add New")
        self._dlg_add_new_panel.wait_for_visible()
        self.enter_display_name(name)
        if series == None: series = self._cbb_series.get_random_item()
        self._cbb_series.select_by_visible_text(series)
        self.submit()
    
    def delete_panel(self, name):
        checkbox = self._cbk_panel_by_text.set_dynamic_value(name)
        checkbox.check()
        self._link_delete.click()
        browser.accept_alert_popup_text()
        browser.wait_for_page_loaded()
    
    def select_panel_action(self, name, action):
        action_link = self._lnk_panel_action_by_text.set_dynamic_value(name, action)
        action_link.click()
    
    def is_panel_present(self, name):
        panel_link = self._lnk_panel_name_by_text.set_dynamic_value(name)
        return panel_link.is_displayed()
    
    def select_type(self, type):
        self._rdo_type_by_text.set_dynamic_value(type).click()
        common.wait(1)
    
    def get_chart_panel_legend(self):
        return self._lbl_chart_panel_setting.get_text()
    
    def is_chart_panel_present(self):
        return self._lbl_chart_panel_setting.is_displayed(1)
    
    def is_data_profiles_sorted(self, ascending=True):
        items = self._cbb_data_profiles.items
        return common.is_list_sorted(items,ascending)
    
    def is_data_profiles_contained(self, data_profiles):
        exp_lst = []
        if type(data_profiles) == str:
            exp_lst.append(data_profiles)
        else:
            exp_lst = data_profiles
        return common.is_list_contained(self._cbb_data_profiles.items, exp_lst)
