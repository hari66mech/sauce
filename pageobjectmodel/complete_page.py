from selenium.webdriver.common.by import By
from constant.constant import Constant


class Complete:
    def __init__(self, driver):
        self.driver = driver

    thank_you_message_loc = (By.XPATH, "//h2[@class='complete-header']")

    @property
    def thank_you_message(self):
        return self.driver.find_element(*self.thank_you_message_loc)

    def validate_thank_you_message(self):
        assert self.thank_you_message.text == Constant.THANK_YOU_MESSAGE
