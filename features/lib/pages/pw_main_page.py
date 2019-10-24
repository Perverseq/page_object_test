from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PWMainPage(BasePage):
    locators_dictionary = {"Новости": (By.XPATH, "//*[@class='menu_news']"),
                           "Об игре": (By.XPATH, "//*[@class='menu_about']"),
                           "Медиа": (By.XPATH, "//*[@class='menu_media']"),
                           "Скачать": (By.XPATH, "//*[@class='menu_download']"),
                           "Сообщество": (By.XPATH, "//*[@class='menu_community']"),}

    assertion_locators = {"Новости": "news.php",
                          "Об игре": "game.php",
                          "Медиа": "media.php",
                          "Скачать": "download.php",
                          "Сообщество": "community.php"}

    buttons_locators = {"ВОЙТИ": (By.XPATH, "//*[@class='enter']/a[@value='Войти']"),
                        "Войти": (By.XPATH, "//*[@class='gmrSignin__actions']/button[@id='js_kit_signin__submit']"),
                        "Пополнить счет": (By.XPATH, "//*[@class='bill_link hv']")}

    fields_locators = {"E-mail": (By.XPATH, "//*[@name='Login']"),
                       "Пароль": (By.XPATH, "//*[@name='Password']")}

    data = {"Логин": "login",
            "Пароль": "password"}

    def __init__(self, context):
        BasePage.__init__(self, context, base_url='https://pw.mail.ru/')

    def go_menu(self, text):
        self.find_element(*self.locators_dictionary[text]).click()

    def assert_page(self, context, text):
        assert self.assertion_locators[text] in context.browser.current_url

    def press_button(self, context, text):
        WebDriverWait(context.browser, 3).until(EC.element_to_be_clickable(self.buttons_locators[text]))
        self.find_element(*self.buttons_locators[text]).click()

    def input_data(self, context, text, text1):
        WebDriverWait(context.browser, 3).until(EC.presence_of_element_located(self.fields_locators[text]))
        self.find_element(*self.fields_locators[text]).send_keys(self.data[text1])
