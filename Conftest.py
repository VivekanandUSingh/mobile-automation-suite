import pytest
import yaml
import os
from framework.driver_factory import DriverFactory
from pages.mobile_pages import LoginPage, ProductsPage, CartPage


@pytest.fixture(scope="session")
def config():
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def test_data(config):
    return config['test_data']


@pytest.fixture
def android_driver():
    """Android driver fixture — mock, local, or cloud based on EXECUTION_MODE."""
    factory = DriverFactory()
    driver = factory.get_driver(platform="android")
    yield driver
    try:
        driver.quit()
    except Exception:
        pass


@pytest.fixture
def ios_driver():
    """iOS driver fixture — mock, local, or cloud based on EXECUTION_MODE."""
    factory = DriverFactory()
    driver = factory.get_driver(platform="ios")
    yield driver
    try:
        driver.quit()
    except Exception:
        pass


@pytest.fixture
def android_login_page(android_driver):
    return LoginPage(android_driver)


@pytest.fixture
def android_products_page(android_driver):
    return ProductsPage(android_driver)


@pytest.fixture
def android_cart_page(android_driver):
    return CartPage(android_driver)


@pytest.fixture
def ios_login_page(ios_driver):
    return LoginPage(ios_driver)


@pytest.fixture
def ios_products_page(ios_driver):
    return ProductsPage(ios_driver)


@pytest.fixture
def ios_cart_page(ios_driver):
    return CartPage(ios_driver)
