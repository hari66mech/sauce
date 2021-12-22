from selenium.webdriver.common.by import By
from constant.constant import Constant


class CheckoutOverview:
    def __init__(self, driver):
        self.driver = driver

    finish_button_loc = (By.XPATH, "//button[@id='finish']")
    checkout_overview_page_heading_loc = (By.XPATH, "//span[@class='title']")

    @property
    def finish_button(self):
        return self.driver.find_element(*self.finish_button_loc)

    @property
    def checkout_overview_page_heading(self):
        return self.driver.find_element(*self.checkout_overview_page_heading_loc)

    def validate_checkout_overview_page_heading(self):
        assert self.checkout_overview_page_heading.text == Constant.CHECKOUT_OVERVIEW_PAGE_HEADING
