import random
from constant.constant import Constant
from selenium.webdriver.common.by import By


class Products:
    def __init__(self, driver):
        self.driver = driver

    products_page_heading_loc = (By.XPATH, "//span[@class='title']")
    products_loc = (By.XPATH, "//div[@class='inventory_list']/div")
    product_loc = "//div[@class='inventory_list']/div[{0}]//button"
    shopping_bucket_loc = (By.XPATH, "//a[@class='shopping_cart_link']")

    @property
    def products_page_heading(self):
        return self.driver.find_element(*self.products_page_heading_loc)

    @property
    def products(self):
        return self.driver.find_elements(*self.products_loc)

    @property
    def total_products(self):
        return len(self.products)

    @property
    def shopping_bucket(self):
        return self.driver.find_element(*self.shopping_bucket_loc)

    def select_product(self):
        self.driver.find_element_by_xpath(self.product_loc.format(random.randint(1, self.total_products))).click()

    def validate_products_page(self):
        assert self.products_page_heading.text == Constant.PRODUCTS_PAGE_HEADING
