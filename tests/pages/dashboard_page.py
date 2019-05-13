import random

from selenpy.element.base_element import BaseElement
from selenpy.element.ta_combo_box import TAComboBox
from selenpy.element.text_box import TextBox
from selenpy.support import browser
from tests.pages import common
from tests.pages.general_page import GeneralPage
from tests.pages.panel_page import PanelPage
from tests.resources.aut import ui


class DashboardPage(PanelPage):
    
    DATA_PROFILES_MENU  = "Administer->Data Profiles"
    PANEL_MENU          = "Administer->Panels"
    
    _btn_global_setting = BaseElement("css=li.mn-setting > a")
    _btn_choose_panels  = BaseElement("id=btnChoosepanel")
    _txt_page_name      = TextBox("id=name")
    _cbb_parent_page    = TAComboBox("id=parent")
    _btn_ok             = BaseElement("id=OK")
    _btn_ok_config      = BaseElement("css=#div_panelConfigurationDlg #OK")
    _btn_cancel         = BaseElement("id=Cancel")
    _btn_hide           = BaseElement("id=btnHidePanel")
    _div_main_body      = BaseElement("id=div_main_body")
    _lnk_panel_by_type  = BaseElement("//div[@class='pitem']/div[text()='{}']/following-sibling::table//a")

    def __init__(self):
        pass
    
    def select_global_setting(self, setting):
        self._btn_global_setting.click()
        self.hover_select_menu(setting)
    
    def open_choose_panels(self):
        self._btn_choose_panels.click()
        self._btn_hide.wait_for_visible()
    
    def hide_choose_panels(self):
        self._btn_hide.click()
        self._btn_hide.wait_for_invisible()
    
    def cancel_add_page(self):
        self._btn_cancel.click()
        self._btn_cancel.wait_for_invisible()
    
    def submit_add_page(self):
        self._btn_ok.click()
        common.wait(1)
    
    def add_page(self, page_name, parent_page=None):
        self.select_global_setting(ui.GLOBAL_SETTING_MENU["add"])
        self._txt_page_name.enter(page_name)
        if parent_page != None:
            self._cbb_parent_page.select_by_visible_text(parent_page)
        self.submit_add_page()
    
    def select_page(self, page_path):
        self.hover_select_menu(page_path)
        browser.wait_for_page_loaded()
    
    def edit_page(self, page_path, page_name_new, parent_page_new=None):
        self.select_page(page_path)
        self.select_global_setting(ui.GLOBAL_SETTING_MENU["edit"])
        self._txt_page_name.enter(page_name_new)
        if parent_page_new != None:
            self._cbb_parent_page.select_by_visible_text(parent_page_new)
        self.submit_add_page()
    
    def delete_page(self, page_path):
        self.select_page(page_path)
        self.select_global_setting(ui.GLOBAL_SETTING_MENU["del"])
        browser.accept_alert_popup_text()
    
    def is_page_present(self, page_path):
        return self.is_menu_present(page_path)
    
    def is_dashboard_locked(self):
        return self._div_main_body.are_child_elements_disabled()
    
    def add_panel(self, name, series=None):
        self.select_global_setting(ui.GLOBAL_SETTING_MENU["cre_panel"])
        self._dlg_add_new_panel.wait_for_visible()
        self.enter_display_name(name)
        if series == None: series = self._cbb_series.get_random_item()
        self._cbb_series.select_by_visible_text(series)
        self.submit()
        self._dlg_panel_config.wait_for_visible()
        self._btn_ok_config.click()
        common.wait(1)
        
    def get_list_panels(self, type):
        panels = []
        for panel_element in self._lnk_panel_by_type.set_dynamic_value(type).find_elements():
            panels.append(panel_element.text)
        return panels
