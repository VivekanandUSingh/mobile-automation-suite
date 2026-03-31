from appium.webdriver.common.appiumby import AppiumBy
from framework.base_page import BasePage


class LoginPage(BasePage):
    """Page object for mobile login screen."""

    USERNAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Password input field")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login button")
    ERROR_MESSAGE = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='generic-error-message']")

    def enter_username(self, username):
        self.enter_text(*self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.enter_text(*self.PASSWORD_FIELD, password)

    def tap_login(self):
        self.click(*self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.tap_login()

    def is_login_button_displayed(self):
        return self.is_displayed(*self.LOGIN_BUTTON)

    def is_login_button_enabled(self):
        return self.is_enabled(*self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)

    def is_error_displayed(self):
        return self.is_displayed(*self.ERROR_MESSAGE)


class ProductsPage(BasePage):
    """Page object for mobile products/catalog screen."""

    PRODUCTS_HEADER = (AppiumBy.ACCESSIBILITY_ID, "Products header")
    PRODUCT_ITEMS = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='store item']")
    FIRST_PRODUCT = (AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='store item'])[1]")
    CART_BADGE = (AppiumBy.ACCESSIBILITY_ID, "Cart badge count")
    CART_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Cart button")
    SORT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Sort button")

    def is_products_header_displayed(self):
        return self.is_displayed(*self.PRODUCTS_HEADER)

    def get_product_count(self):
        return len(self.find_elements(*self.PRODUCT_ITEMS))

    def tap_first_product(self):
        self.click(*self.FIRST_PRODUCT)

    def tap_cart(self):
        self.click(*self.CART_BUTTON)

    def get_cart_badge_count(self):
        try:
            text = self.get_text(*self.CART_BADGE)
            return int(text)
        except Exception:
            return 0

    def tap_sort(self):
        self.click(*self.SORT_BUTTON)


class CartPage(BasePage):
    """Page object for mobile shopping cart screen."""

    CART_HEADER = (AppiumBy.ACCESSIBILITY_ID, "Cart header")
    CART_ITEMS = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='cart item']")
    CHECKOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Proceed To Checkout button")
    REMOVE_BUTTON = (AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='remove item'])[1]")

    def is_cart_displayed(self):
        return self.is_displayed(*self.CART_HEADER)

    def get_cart_item_count(self):
        return len(self.find_elements(*self.CART_ITEMS))

    def tap_checkout(self):
        self.click(*self.CHECKOUT_BUTTON)

    def remove_first_item(self):
        self.click(*self.REMOVE_BUTTON)

    def is_empty(self):
        return self.get_cart_item_count() == 0
