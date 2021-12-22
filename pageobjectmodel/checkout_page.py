from faker import Faker
from selenium.webdriver.common.by import By


class Checkout:
    def __init__(self, driver):
        self.driver = driver

    fake = Faker()

    first_name_loc = (By.XPATH, "//input[@id='first-name']")
    last_name_loc = (By.XPATH, "//input[@id='last-name']")
    postal_code_loc = (By.XPATH, "//input[@id='postal-code']")
    continue_button_loc = (By.XPATH, "//input[@id='continue']")

    @property
    def first_name(self):
        return self.driver.find_element(*self.first_name_loc)

    @property
    def last_name(self):
        return self.driver.find_element(*self.last_name_loc)

    @property
    def postal_code(self):
        return self.driver.find_element(*self.postal_code_loc)

    @property
    def continue_button(self):
        return self.driver.find_element(*self.continue_button_loc)

    def fill_user_details(self):
        self.first_name.send_keys(self.fake.first_name())
        self.last_name.send_keys(self.fake.last_name())
        self.postal_code.send_keys("63201")
        self.continue_button.click()
