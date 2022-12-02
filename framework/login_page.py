from framework.page import Page
from selenium.webdriver.common.by import By
import time


class LoginPage(Page):
    # локатори
    LOGIN = (By.ID, 'com.ajaxsystems:id/login')
    PASSWORD = (By.ID, 'com.ajaxsystems:id/password')
    NEXT = (By.ID, 'com.ajaxsystems:id/next')
    text = 'qa.ajax.app.automation@gmail.com'
    password = 'qa_automation_password'
    POPUP = (By.ID, 'com.ajaxsystems:id/cancel_button')
    SIDEBAR = (By.ID, 'com.ajaxsystems:id/menuDrawer')
    SETTINGS = (By.ID, 'com.ajaxsystems:id/settings')
    SIGNOUT = (By.ID, 'com.ajaxsystems:id/logoutText')

    def tap_login(self):
        self.click_element(*self.LOGIN)

    def input_login(self, text):
        self.click_element(*self.LOGIN)
        self.input(text, *self.LOGIN)

    def input_pass(self, text):
        self.click_element(*self.PASSWORD)
        self.input(text, *self.PASSWORD)

    def auth_tap(self):
        self.click_element(*self.NEXT)

    def popup_tap(self):
        self.click_element(*self.POPUP)

    def logout(self):
        time.sleep(0.5)
        self.click_element(*self.SIDEBAR)
        self.click_element(*self.SETTINGS)
        time.sleep(0.5)
        self.click_element(*self.SIGNOUT)
