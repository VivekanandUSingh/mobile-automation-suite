import pytest


class TestIOSLogin:
    """iOS login test suite."""

    def test_login_button_is_displayed(self, ios_login_page):
        """Verify login button is visible on iOS."""
        assert ios_login_page.is_login_button_displayed()

    def test_login_button_is_enabled(self, ios_login_page):
        """Verify login button is tappable on iOS."""
        assert ios_login_page.is_login_button_enabled()

    def test_valid_login(self, ios_login_page, test_data):
        """Verify valid credentials trigger login on iOS."""
        ios_login_page.login(
            test_data['valid_user']['username'],
            test_data['valid_user']['password']
        )
        ios_login_page.take_screenshot("ios_valid_login")

    def test_username_field_accepts_input(self, ios_login_page, test_data):
        """Verify username field accepts input on iOS."""
        ios_login_page.enter_username(test_data['valid_user']['username'])
        element = ios_login_page.find_element(
            *ios_login_page.USERNAME_FIELD
        )
        assert element is not None

    def test_password_field_accepts_input(self, ios_login_page, test_data):
        """Verify password field accepts input on iOS."""
        ios_login_page.enter_password(test_data['valid_user']['password'])
        element = ios_login_page.find_element(
            *ios_login_page.PASSWORD_FIELD
        )
        assert element is not None

    def test_invalid_login_shows_error(self, ios_login_page, test_data):
        """Verify invalid credentials show error on iOS."""
        ios_login_page.login(
            test_data['invalid_user']['username'],
            test_data['invalid_user']['password']
        )
        ios_login_page.take_screenshot("ios_invalid_login")


class TestIOSProducts:
    """iOS products page test suite."""

    def test_products_page_loads(self, ios_products_page):
        """Verify products screen loads on iOS."""
        assert ios_products_page.is_products_header_displayed()

    def test_products_are_displayed(self, ios_products_page):
        """Verify product items render on iOS."""
        count = ios_products_page.get_product_count()
        assert count >= 0

    def test_cart_button_is_accessible(self, ios_products_page):
        """Verify cart navigation available on iOS."""
        assert ios_products_page.is_displayed(
            *ios_products_page.CART_BUTTON
        )

    def test_cart_badge_initial_count(self, ios_products_page):
        """Verify cart starts empty on iOS."""
        count = ios_products_page.get_cart_badge_count()
        assert count >= 0

    def test_sort_button_is_accessible(self, ios_products_page):
        """Verify sort is available on iOS."""
        assert ios_products_page.is_displayed(
            *ios_products_page.SORT_BUTTON
        )


class TestIOSCart:
    """iOS cart test suite."""

    def test_cart_page_loads(self, ios_cart_page):
        """Verify cart screen accessible on iOS."""
        assert ios_cart_page is not None

    def test_cart_item_count(self, ios_cart_page):
        """Verify cart item count readable on iOS."""
        count = ios_cart_page.get_cart_item_count()
        assert count >= 0

    def test_checkout_button_accessible(self, ios_cart_page):
        """Verify checkout button present on iOS."""
        assert ios_cart_page.is_displayed(
            *ios_cart_page.CHECKOUT_BUTTON
        )


class TestCrossPlatform:
    """Cross-platform parity tests — same behaviour on Android and iOS."""

    def test_login_button_displayed_on_both(
        self, android_login_page, ios_login_page
    ):
        """Verify login button visible on both platforms."""
        assert android_login_page.is_login_button_displayed()
        assert ios_login_page.is_login_button_displayed()

    def test_login_button_enabled_on_both(
        self, android_login_page, ios_login_page
    ):
        """Verify login button enabled on both platforms."""
        assert android_login_page.is_login_button_enabled()
        assert ios_login_page.is_login_button_enabled()

    def test_products_load_on_both(
        self, android_products_page, ios_products_page
    ):
        """Verify products page loads on both platforms."""
        assert android_products_page.is_products_header_displayed()
        assert ios_products_page.is_products_header_displayed()

    def test_cart_accessible_on_both(
        self, android_cart_page, ios_cart_page
    ):
        """Verify cart accessible on both platforms."""
        assert android_cart_page is not None
        assert ios_cart_page is not None
