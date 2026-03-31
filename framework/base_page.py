import yaml
import os
from framework.driver_factory import DriverFactory


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


class BasePage:
    """
    Base class for all mobile page objects.
    Provides shared driver utilities, waits, and config access.
    Works identically in mock, local, and cloud modes.
    """

    def __init__(self, driver):
        self.driver = driver
        self.config = load_config()
        self.timeout = self.config['timeouts']['explicit_wait']

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def enter_text(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, value):
        element = self.find_element(by, value)
        return element.text

    def is_displayed(self, by, value):
        try:
            element = self.find_element(by, value)
            return element.is_displayed()
        except Exception:
            return False

    def is_enabled(self, by, value):
        try:
            element = self.find_element(by, value)
            return element.is_enabled()
        except Exception:
            return False

    def take_screenshot(self, name):
        os.makedirs("reports/screenshots", exist_ok=True)
        try:
            self.driver.save_screenshot(f"reports/screenshots/{name}.png")
        except Exception:
            pass

    def swipe_up(self):
        try:
            size = self.driver.get_window_size()
            self.driver.swipe(
                size['width'] // 2, size['height'] * 0.8,
                size['width'] // 2, size['height'] * 0.2,
                500
            )
        except Exception:
            pass

    def switch_to_webview(self):
        try:
            contexts = self.driver.contexts
            for context in contexts:
                if "WEBVIEW" in context:
                    self.driver.switch_to.context(context)
                    return True
        except Exception:
            pass
        return False

    def switch_to_native(self):
        try:
            self.driver.switch_to.context("NATIVE_APP")
        except Exception:
            pass
