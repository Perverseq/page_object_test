from selenium.webdriver.common.by import By
from .base_page import BasePage


class GoogleSearchPage(BasePage):
    locator_dictionary = {"pw_link": (By.PARTIAL_LINK_TEXT, "pw.mail.ru")}

    def __init__(self, context):
        BasePage.__init__(self, context, base_url='https://www.google.ru/')

    def go_link(self):
        self.find_element(*self.locator_dictionary["pw_link"]).click()
        window_after = self.browser.window_handles[1]
        self.browser.switch_to_window(window_after)
