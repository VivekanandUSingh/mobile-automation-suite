import pytest
import yaml
import os
import logging
from unittest.mock import MagicMock

logger = logging.getLogger(__name__)


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def create_mock_driver(platform="android"):
    """Creates a fully self-contained mock Appium driver."""
    logger.info(f"Creating mock driver for platform: {platform.upper()}")

    driver = MagicMock()
    driver.platform = platform

    mock_element = MagicMock()
    mock_element.text = f"Mock Element [{platform.upper()}]"
    mock_element.is_displayed.return_value = True
    mock_element.is_enabled.return_value = True

    driver.find_element.return_value = mock_element
    driver.find_elements.return_value = [mock_element, mock_element, mock_element]
    driver.current_activity = ".MainActivity"
    driver.current_package = "com.saucelabs.mydemoapp.android"
    driver.contexts = ["NATIVE_APP", "WEBVIEW_com.saucelabs"]
    driver.current_context = "NATIVE_APP"
    driver.capabilities = {
        "platformName": platform.capitalize(),
        "deviceName": "Mock Device",
        "platformVersion": "13.0" if platform == "android" else "16.0"
    }

    logger.info(f"Mock driver created — platform: {platform.upper()}, "
                f"device: Mock Device, "
                f"version: {'13.0' if platform == 'android' else '16.0'}")
    return driver


@pytest.fixture(scope="session")
def config():
    return load_config()


@pytest.fixture(scope="session")
def test_data(config):
    return config['test_data']


@pytest.fixture
def android_driver():
    logger.info("Setting up Android driver")
    driver = create_mock_driver("android")
    yield driver
    logger.info("Tearing down Android driver")
    try:
        driver.quit()
    except Exception:
        pass


@pytest.fixture
def ios_driver():
    logger.info("Setting up iOS driver")
    driver = create_mock_driver("ios")
    yield driver
    logger.info("Tearing down iOS driver")
    try:
        driver.quit()
    except Exception:
        pass


@pytest.fixture
def android_login_page(android_driver):
    from pages.mobile_pages import LoginPage
    logger.info("Initializing Android LoginPage")
    return LoginPage(android_driver)


@pytest.fixture
def android_products_page(android_driver):
    from pages.mobile_pages import ProductsPage
    logger.info("Initializing Android ProductsPage")
    return ProductsPage(android_driver)


@pytest.fixture
def android_cart_page(android_driver):
    from pages.mobile_pages import CartPage
    logger.info("Initializing Android CartPage")
    return CartPage(android_driver)


@pytest.fixture
def ios_login_page(ios_driver):
    from pages.mobile_pages import LoginPage
    logger.info("Initializing iOS LoginPage")
    return LoginPage(ios_driver)


@pytest.fixture
def ios_products_page(ios_driver):
    from pages.mobile_pages import ProductsPage
    logger.info("Initializing iOS ProductsPage")
    return ProductsPage(ios_driver)


@pytest.fixture
def ios_cart_page(ios_driver):
    from pages.mobile_pages import CartPage
    logger.info("Initializing iOS CartPage")
    return CartPage(ios_driver)
