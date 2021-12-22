from selenium.webdriver.common.by import By
from constant.constant import Constant


class Cart:
    def __init__(self, driver):
        self.driver = driver

    checkout_button_loc = (By.XPATH, "//button[@id='checkout']")
    cart_page_heading_loc = (By.XPATH, "//span[@class='title']")

    @property
    def checkout_button(self):
        return self.driver.find_element(*self.checkout_button_loc)

    @property
    def cart_page_heading(self):
        return self.driver.find_element(*self.cart_page_heading_loc)

    def validate_cart_page(self):
        assert self.cart_page_heading.text == Constant.CART_PAGE_HEADING
