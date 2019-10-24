from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class PwPayment(BasePage):
    sums_dictionary = {"5": "66,90",
                       "10": "133,80",
                       "20": "267,60",
                       "50": "669",
                       "75": "1003,50",
                       "100": "1338",
                       "300": "4014"}

    locators_dictionary = {"Сумма платежа": (By.ID, "xform-sum"),
                           "Выпадающий список": (By.XPATH, '//*[@id="xform-bonus"]')}

    def switch_frames(self, context):
        context.browser.switch_to.frame(context.browser.find_element_by_id('payment_iframe'))
        WebDriverWait(context.browser, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='xform-bonus']")))

    def select_value(self, text, text1):
        Select(self.find_element(*self.locators_dictionary[text])).select_by_value(text1)

    def sum_assert(self, context, text, text1):
        WebDriverWait(context.browser, 1).until(EC.text_to_be_present_in_element_value((By.ID, "xform-sum"), text1))
        assert text1 in self.find_element(*self.locators_dictionary[text]).get_attribute('value')
