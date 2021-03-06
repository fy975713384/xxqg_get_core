# -*- coding: utf-8 -*-

from page.base_page import BasePage
from page.page_av import AVPage
from page.page_read import StudyPage
from page.page_user import UserPage


class MainPage(BasePage):

    def __init__(self):
        self._message = (self.MB.ID, 'home_bottom_tab_button_message')
        self._ding = (self.MB.ID, 'home_bottom_tab_button_ding')
        self._article = (self.MB.ID, 'home_bottom_tab_button_work')
        self._av = (self.MB.ID, 'home_bottom_tab_button_contact')
        self._user = (self.MB.ID, 'home_bottom_tab_button_mine')

    def switch_message(self):
        self.find(self._message).click()
        return

    def switch_ding(self):
        self.find(self._ding).click()
        return

    def switch_study(self):
        self.find(self._article).click()
        return StudyPage()

    def switch_av(self):
        self.find(self._av).click()
        return AVPage()

    def switch_user(self):
        self.find(self._user).click()
        return UserPage()
