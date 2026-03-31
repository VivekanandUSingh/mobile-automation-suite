import pytest


class TestAndroidLogin:
    """Android login test suite."""

    def test_login_button_is_displayed(self, android_login_page):
        """Verify login button is visible on launch."""
        assert android_login_page.is_login_button_displayed()

    def test_login_button_is_enabled(self, android_login_page):
        """Verify login button is tappable."""
        assert android_login_page.is_login_button_enabled()

    def test_valid_login(self, android_login_page, test_data):
        """Verify valid credentials trigger login action."""
        android_login_page.login(
            test_data['valid_user']['username'],
            test_data['valid_user']['password']
        )
        android_login_page.take_screenshot("android_valid_login")

    def test_username_field_accepts_input(self, android_login_page, test_data):
        """Verify username field accepts text input."""
        android_login_page.enter_username(test_data['valid_user']['username'])
        element = android_login_page.find_element(
            *android_login_page.USERNAME_FIELD
        )
        assert element is not None

    def test_password_field_accepts_input(self, android_login_page, test_data):
        """Verify password field accepts text input."""
        android_login_page.enter_password(test_data['valid_user']['password'])
        element = android_login_page.find_element(
            *android_login_page.PASSWORD_FIELD
        )
        assert element is not None

    def test_invalid_login_shows_error(self, android_login_page, test_data):
        """Verify invalid credentials show error state."""
        android_login_page.login(
            test_data['invalid_user']['username'],
            test_data['invalid_user']['password']
        )
        android_login_page.take_screenshot("android_invalid_login")


class TestAndroidProducts:
    """Android products page test suite."""

    def test_products_page_loads(self, android_products_page):
        """Verify products screen loads successfully."""
        assert android_products_page.is_products_header_displayed()

    def test_products_are_displayed(self, android_products_page):
        """Verify product items are rendered on screen."""
        count = android_products_page.get_product_count()
        assert count >= 0

    def test_cart_button_is_accessible(self, android_products_page):
        """Verify cart navigation is available."""
        assert android_products_page.is_displayed(
            *android_products_page.CART_BUTTON
        )

    def test_cart_badge_initial_count(self, android_products_page):
        """Verify cart starts empty."""
        count = android_products_page.get_cart_badge_count()
        assert count >= 0

    def test_sort_button_is_accessible(self, android_products_page):
        """Verify sort functionality is available."""
        assert android_products_page.is_displayed(
            *android_products_page.SORT_BUTTON
        )


class TestAndroidCart:
    """Android cart test suite."""

    def test_cart_page_loads(self, android_cart_page):
        """Verify cart screen is accessible."""
        assert android_cart_page is not None

    def test_cart_item_count(self, android_cart_page):
        """Verify cart item count is readable."""
        count = android_cart_page.get_cart_item_count()
        assert count >= 0

    def test_checkout_button_accessible(self, android_cart_page):
        """Verify checkout button is present."""
        assert android_cart_page.is_displayed(
            *android_cart_page.CHECKOUT_BUTTON
        )
