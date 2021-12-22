from pytest_bdd import given, when, then, scenarios
from constant.constant import Constant
from pageobjectmodel.login_page import Login
from pageobjectmodel.cart_page import Cart
from pageobjectmodel.checkout_overview_page import CheckoutOverview
from pageobjectmodel.checkout_page import Checkout
from pageobjectmodel.complete_page import Complete
from pageobjectmodel.products_page import Products


scenarios("C:/Users/harikrishna.manokara/PycharmProjects/sauce/tests/features/saucedemo/shopping.feature")


@given("The saucedemo login_page is displayed")
def get_login_page(driver):
    driver.get(Constant.LOGIN_PAGE_URL)


@when("I login as a standard user")
def login(driver):
    Login(driver).login_user()


@when("I shop an item from products_page")
def shop_item(driver):
    products = Products(driver)
    products.validate_products_page()
    products.select_product()
    products.shopping_bucket.click()


@when("I click the checkout button from cart_page")
def click_checkout_button(driver):
    cart = Cart(driver)
    cart.validate_cart_page()
    cart.checkout_button.click()


@when("I fill the user information in checkout_page")
def enter_user_details(driver):
    Checkout(driver).fill_user_details()


@when("I click the finish button from checkout_overview_page")
def click_finish_button(driver):
    checkout = CheckoutOverview(driver)
    checkout.validate_checkout_overview_page_heading()
    checkout.finish_button.click()


@then("I validate thank you message from complete_page")
def verify_thank_you_message(driver):
    Complete(driver).validate_thank_you_message()
