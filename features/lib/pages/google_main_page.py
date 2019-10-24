from selenium.webdriver.common.by import By
from .base_page import BasePage


class GoogleMainPage(BasePage):
    locator_dictionary = {"search_line": (By.NAME, "q"),
                          "Поиск в Google": (By.XPATH, "//*[@class='FPdoLc VlcLAe']/center/input[@class='gNO89b']"),
                          "req": "Perfect World russia"}

    def __init__(self, context):
        BasePage.__init__(self, context, base_url='https://www.google.ru/')

    def input_search_req(self, req):
        self.find_element(*self.locator_dictionary["search_line"]).send_keys(req)

    def search(self, text):
        self.find_element(*self.locator_dictionary[text]).click()
