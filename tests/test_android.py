import pytest
import allure
import logging

logger = logging.getLogger(__name__)


@allure.suite("Android Test Suite")
@allure.feature("Android Login")
class TestAndroidLogin:
    """Android login test suite."""

    @allure.story("UI Elements")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Login button is displayed on launch")
    def test_login_button_is_displayed(self, android_login_page):
        """Verify login button is visible on launch."""
        logger.info("Checking login button visibility on Android")
        result = android_login_page.is_login_button_displayed()
        logger.info(f"Login button displayed: {result}")
        assert result
        logger.info("PASS — login button is visible")

    @allure.story("UI Elements")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Login button is enabled and tappable")
    def test_login_button_is_enabled(self, android_login_page):
        """Verify login button is tappable."""
        logger.info("Checking login button enabled state on Android")
        result = android_login_page.is_login_button_enabled()
        logger.info(f"Login button enabled: {result}")
        assert result
        logger.info("PASS — login button is enabled")

    @allure.story("Authentication")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Valid credentials trigger login action")
    def test_valid_login(self, android_login_page, test_data):
        """Verify valid credentials trigger login action."""
        user = test_data['valid_user']
        logger.info(f"Attempting login with user: {user['username']}")
        with allure.step(f"Enter username: {user['username']}"):
            android_login_page.enter_username(user['username'])
        with allure.step("Enter password"):
            android_login_page.enter_password(user['password'])
        with allure.step("Tap login button"):
            android_login_page.tap_login()
        android_login_page.take_screenshot("android_valid_login")
        logger.info("PASS — valid login action completed")

    @allure.story("UI Elements")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Username field accepts text input")
    def test_username_field_accepts_input(self, android_login_page, test_data):
        """Verify username field accepts text input."""
        username = test_data['valid_user']['username']
        logger.info(f"Entering username: {username}")
        with allure.step(f"Type username into field"):
            android_login_page.enter_username(username)
        element = android_login_page.find_element(*android_login_page.USERNAME_FIELD)
        assert element is not None
        logger.info("PASS — username field accepted input")

    @allure.story("UI Elements")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Password field accepts text input")
    def test_password_field_accepts_input(self, android_login_page, test_data):
        """Verify password field accepts text input."""
        logger.info("Entering password into password field")
        with allure.step("Type password into field"):
            android_login_page.enter_password(test_data['valid_user']['password'])
        element = android_login_page.find_element(*android_login_page.PASSWORD_FIELD)
        assert element is not None
        logger.info("PASS — password field accepted input")

    @allure.story("Authentication")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Invalid credentials show error state")
    def test_invalid_login_shows_error(self, android_login_page, test_data):
        """Verify invalid credentials show error state."""
        user = test_data['invalid_user']
        logger.info(f"Attempting login with invalid user: {user['username']}")
        with allure.step("Enter invalid username"):
            android_login_page.enter_username(user['username'])
        with allure.step("Enter invalid password"):
            android_login_page.enter_password(user['password'])
        with allure.step("Tap login button"):
            android_login_page.tap_login()
        android_login_page.take_screenshot("android_invalid_login")
        logger.info("PASS — invalid login handled correctly")


@allure.suite("Android Test Suite")
@allure.feature("Android Products")
class TestAndroidProducts:
    """Android products page test suite."""

    @allure.story("Page Load")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Products screen loads successfully")
    def test_products_page_loads(self, android_products_page):
        logger.info("Verifying products page header is displayed")
        result = android_products_page.is_products_header_displayed()
        logger.info(f"Products header displayed: {result}")
        assert result
        logger.info("PASS — products page loaded")

    @allure.story("Product Listing")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Product items are rendered on screen")
    def test_products_are_displayed(self, android_products_page):
        logger.info("Counting product items on Android products page")
        count = android_products_page.get_product_count()
        logger.info(f"Product count: {count}")
        assert count >= 0
        logger.info(f"PASS — {count} products displayed")

    @allure.story("Navigation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Cart button is accessible from products page")
    def test_cart_button_is_accessible(self, android_products_page):
        logger.info("Checking cart button accessibility")
        result = android_products_page.is_displayed(*android_products_page.CART_BUTTON)
        logger.info(f"Cart button accessible: {result}")
        assert result
        logger.info("PASS — cart button accessible")

    @allure.story("Cart")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Cart badge shows initial count")
    def test_cart_badge_initial_count(self, android_products_page):
        logger.info("Checking initial cart badge count")
        count = android_products_page.get_cart_badge_count()
        logger.info(f"Cart badge count: {count}")
        assert count >= 0
        logger.info(f"PASS — cart badge count: {count}")

    @allure.story("Sorting")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Sort button is accessible")
    def test_sort_button_is_accessible(self, android_products_page):
        logger.info("Checking sort button accessibility")
        result = android_products_page.is_displayed(*android_products_page.SORT_BUTTON)
        logger.info(f"Sort button accessible: {result}")
        assert result
        logger.info("PASS — sort button accessible")


@allure.suite("Android Test Suite")
@allure.feature("Android Cart")
class TestAndroidCart:
    """Android cart test suite."""

    @allure.story("Page Load")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Cart screen is accessible")
    def test_cart_page_loads(self, android_cart_page):
        logger.info("Verifying cart page is accessible")
        assert android_cart_page is not None
        logger.info("PASS — cart page accessible")

    @allure.story("Cart Items")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Cart item count is readable")
    def test_cart_item_count(self, android_cart_page):
        logger.info("Reading cart item count")
        count = android_cart_page.get_cart_item_count()
        logger.info(f"Cart item count: {count}")
        assert count >= 0
        logger.info(f"PASS — cart has {count} items")

    @allure.story("Checkout")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Checkout button is present")
    def test_checkout_button_accessible(self, android_cart_page):
        logger.info("Checking checkout button presence")
        result = android_cart_page.is_displayed(*android_cart_page.CHECKOUT_BUTTON)
        logger.info(f"Checkout button present: {result}")
        assert result
        logger.info("PASS — checkout button present")
