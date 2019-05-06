from selenpy.element.base_element import BaseElement
from selenpy.element.combo_box import ComboBox
from selenpy.element.text_box import TextBox
from selenpy.support.conditions import be
from tests.pages.general_page import GeneralPage


class LoginPage(GeneralPage):
    
    _cbb_repository = ComboBox("id=repository")
    _txt_username = TextBox("id=username")
    _txt_password = TextBox("id=password")
    _btn_login = BaseElement("css=.btn-login")

    def __init__(self):
        pass
    
    def login(self, repository, user, pwd):
        self._cbb_repository.wait_until(be.visible)
        self._cbb_repository.select_by_value(repository)
        self._txt_username.clear()
        self._txt_password.clear()
        self._txt_username.send_keys(user)
        self._txt_password.send_keys(pwd)
        self._btn_login.click()
