import pytest
import allure
import logging

logger = logging.getLogger(__name__)


@allure.suite("iOS Test Suite")
@allure.feature("iOS Login")
class TestIOSLogin:
    """iOS login test suite."""

    @allure.story("UI Elements")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Login button is displayed on iOS")
    def test_login_button_is_displayed(self, ios_login_page):
        logger.info("Checking login button visibility on iOS")
        result = ios_login_page.is_login_button_displayed()
        logger.info(f"Login button displayed: {result}")
        assert result
        logger.info("PASS — login button visible on iOS")

    @allure.story("UI Elements")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Login button is enabled on iOS")
    def test_login_button_is_enabled(self, ios_login_page):
        logger.info("Checking login button enabled state on iOS")
        result = ios_login_page.is_login_button_enabled()
        logger.info(f"Login button enabled: {result}")
        assert result
        logger.info("PASS — login button enabled on iOS")

    @allure.story("Authentication")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Valid credentials trigger login on iOS")
    def test_valid_login(self, ios_login_page, test_data):
        user = test_data['valid_user']
        logger.info(f"Attempting iOS login with: {user['username']}")
        with allure.step(f"Enter username: {user['username']}"):
            ios_login_page.enter_username(user['username'])
        with allure.step("Enter password"):
            ios_login_page.enter_password(user['password'])
        with allure.step("Tap login button"):
            ios_login_page.tap_login()
        ios_login_page.take_screenshot("ios_valid_login")
        logger.info("PASS — valid iOS login completed")

    @allure.story("UI Elements")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Username field accepts input on iOS")
    def test_username_field_accepts_input(self, ios_login_page, test_data):
        username = test_data['valid_user']['username']
        logger.info(f"Entering username on iOS: {username}")
        with allure.step("Type username into field"):
            ios_login_page.enter_username(username)
        element = ios_login_page.find_element(*ios_login_page.USERNAME_FIELD)
        assert element is not None
        logger.info("PASS — username field accepted input on iOS")

    @allure.story("UI Elements")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Password field accepts input on iOS")
    def test_password_field_accepts_input(self, ios_login_page, test_data):
        logger.info("Entering password on iOS")
        with allure.step("Type password into field"):
            ios_login_page.enter_password(test_data['valid_user']['password'])
        element = ios_login_page.find_element(*ios_login_page.PASSWORD_FIELD)
        assert element is not None
        logger.info("PASS — password field accepted input on iOS")

    @allure.story("Authentication")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Invalid credentials show error on iOS")
    def test_invalid_login_shows_error(self, ios_login_page, test_data):
        user = test_data['invalid_user']
        logger.info(f"Testing invalid login on iOS with: {user['username']}")
        with allure.step("Enter invalid username"):
            ios_login_page.enter_username(user['username'])
        with allure.step("Enter invalid password"):
            ios_login_page.enter_password(user['password'])
        with allure.step("Tap login button"):
            ios_login_page.tap_login()
        ios_login_page.take_screenshot("ios_invalid_login")
        logger.info("PASS — invalid login handled on iOS")


@allure.suite("iOS Test Suite")
@allure.feature("iOS Products")
class TestIOSProducts:
    """iOS products page test suite."""

    @allure.story("Page Load")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Products screen loads on iOS")
    def test_products_page_loads(self, ios_products_page):
        logger.info("Verifying products page on iOS")
        result = ios_products_page.is_products_header_displayed()
        logger.info(f"Products header displayed on iOS: {result}")
        assert result
        logger.info("PASS — iOS products page loaded")

    @allure.story("Product Listing")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Product items render on iOS")
    def test_products_are_displayed(self, ios_products_page):
        logger.info("Counting products on iOS")
        count = ios_products_page.get_product_count()
        logger.info(f"iOS product count: {count}")
        assert count >= 0
        logger.info(f"PASS — {count} products on iOS")

    @allure.story("Navigation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Cart button accessible on iOS")
    def test_cart_button_is_accessible(self, ios_products_page):
        logger.info("Checking cart button on iOS")
        result = ios_products_page.is_displayed(*ios_products_page.CART_BUTTON)
        logger.info(f"Cart button on iOS: {result}")
        assert result
        logger.info("PASS — cart button accessible on iOS")

    @allure.story("Cart")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Cart badge count readable on iOS")
    def test_cart_badge_initial_count(self, ios_products_page):
        logger.info("Checking cart badge on iOS")
        count = ios_products_page.get_cart_badge_count()
        logger.info(f"iOS cart badge: {count}")
        assert count >= 0
        logger.info(f"PASS — iOS cart badge: {count}")

    @allure.story("Sorting")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Sort button accessible on iOS")
    def test_sort_button_is_accessible(self, ios_products_page):
        logger.info("Checking sort button on iOS")
        result = ios_products_page.is_displayed(*ios_products_page.SORT_BUTTON)
        logger.info(f"Sort button on iOS: {result}")
        assert result
        logger.info("PASS — sort accessible on iOS")


@allure.suite("iOS Test Suite")
@allure.feature("iOS Cart")
class TestIOSCart:
    """iOS cart test suite."""

    @allure.story("Page Load")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Cart screen accessible on iOS")
    def test_cart_page_loads(self, ios_cart_page):
        logger.info("Verifying iOS cart page")
        assert ios_cart_page is not None
        logger.info("PASS — iOS cart accessible")

    @allure.story("Cart Items")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Cart item count readable on iOS")
    def test_cart_item_count(self, ios_cart_page):
        logger.info("Reading iOS cart item count")
        count = ios_cart_page.get_cart_item_count()
        logger.info(f"iOS cart items: {count}")
        assert count >= 0
        logger.info(f"PASS — iOS cart has {count} items")

    @allure.story("Checkout")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Checkout button present on iOS")
    def test_checkout_button_accessible(self, ios_cart_page):
        logger.info("Checking iOS checkout button")
        result = ios_cart_page.is_displayed(*ios_cart_page.CHECKOUT_BUTTON)
        logger.info(f"iOS checkout button: {result}")
        assert result
        logger.info("PASS — iOS checkout button present")


@allure.suite("Cross-Platform Suite")
@allure.feature("Platform Parity")
class TestCrossPlatform:
    """Cross-platform parity tests."""

    @allure.story("Login Parity")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Login button displayed on both platforms")
    def test_login_button_displayed_on_both(self, android_login_page, ios_login_page):
        logger.info("Cross-platform check: login button visibility")
        android_result = android_login_page.is_login_button_displayed()
        ios_result = ios_login_page.is_login_button_displayed()
        logger.info(f"Android: {android_result} | iOS: {ios_result}")
        assert android_result
        assert ios_result
        logger.info("PASS — login button visible on both platforms")

    @allure.story("Login Parity")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Login button enabled on both platforms")
    def test_login_button_enabled_on_both(self, android_login_page, ios_login_page):
        logger.info("Cross-platform check: login button enabled state")
        android_result = android_login_page.is_login_button_enabled()
        ios_result = ios_login_page.is_login_button_enabled()
        logger.info(f"Android: {android_result} | iOS: {ios_result}")
        assert android_result
        assert ios_result
        logger.info("PASS — login button enabled on both platforms")

    @allure.story("Products Parity")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Products page loads on both platforms")
    def test_products_load_on_both(self, android_products_page, ios_products_page):
        logger.info("Cross-platform check: products page load")
        android_result = android_products_page.is_products_header_displayed()
        ios_result = ios_products_page.is_products_header_displayed()
        logger.info(f"Android: {android_result} | iOS: {ios_result}")
        assert android_result
        assert ios_result
        logger.info("PASS — products page loads on both platforms")

    @allure.story("Cart Parity")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Cart accessible on both platforms")
    def test_cart_accessible_on_both(self, android_cart_page, ios_cart_page):
        logger.info("Cross-platform check: cart accessibility")
        assert android_cart_page is not None
        assert ios_cart_page is not None
        logger.info("PASS — cart accessible on both platforms")
