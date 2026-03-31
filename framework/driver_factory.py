import os
import yaml
from unittest.mock import MagicMock


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


class DriverFactory:
    """
    Factory class for creating Appium driver instances.
    Supports three modes:
      - mock   : No device needed. Used for CI/CD and portfolio demo.
      - local  : Real device or emulator via local Appium server.
      - cloud  : BrowserStack or Sauce Labs device farm.
    """

    def __init__(self):
        self.config = load_config()
        self.mode = os.environ.get("EXECUTION_MODE", self.config.get("mode", "mock"))

    def get_driver(self, platform="android"):
        if self.mode == "mock":
            return self._create_mock_driver(platform)
        elif self.mode == "local":
            return self._create_local_driver(platform)
        elif self.mode == "cloud":
            provider = os.environ.get("CLOUD_PROVIDER", "browserstack")
            return self._create_cloud_driver(platform, provider)
        else:
            raise ValueError(f"Unknown execution mode: {self.mode}")

    def _create_mock_driver(self, platform):
        """
        Creates a mock Appium driver for CI/CD and demo purposes.
        Simulates all driver interactions without requiring a real device.
        """
        driver = MagicMock()
        driver.platform = platform

        # Simulate find_element returning a mock element
        mock_element = MagicMock()
        mock_element.text = self._get_mock_text(platform)
        mock_element.is_displayed.return_value = True
        mock_element.is_enabled.return_value = True
        driver.find_element.return_value = mock_element
        driver.find_elements.return_value = [mock_element, mock_element, mock_element]

        # Simulate driver properties
        driver.current_activity = ".MainActivity"
        driver.current_package = "com.saucelabs.mydemoapp.android"
        driver.capabilities = {
            "platformName": platform.capitalize(),
            "deviceName": "Mock Device",
            "platformVersion": "13.0" if platform == "android" else "16.0"
        }

        # Simulate context switching
        driver.contexts = ["NATIVE_APP", "WEBVIEW_com.saucelabs"]
        driver.current_context = "NATIVE_APP"

        return driver

    def _get_mock_text(self, platform):
        return f"Mock Element [{platform.upper()}]"

    def _create_local_driver(self, platform):
        """Creates driver connecting to local Appium server."""
        from appium import webdriver
        from appium.options import AppiumOptions

        config = self.config[platform]
        server_url = self.config['local']['appium_server_url']

        options = AppiumOptions()
        options.platform_name = config['platform_name']
        options.automation_name = config['automation_name']

        if platform == "android":
            options.set_capability("deviceName", config['device_name'])
            options.set_capability("appPackage", config['app_package'])
            options.set_capability("appActivity", config['app_activity'])
            options.set_capability("app", config['app'])
        else:
            options.set_capability("deviceName", config['device_name'])
            options.set_capability("bundleId", config['bundle_id'])
            options.set_capability("app", config['app'])

        return webdriver.Remote(server_url, options=options)

    def _create_cloud_driver(self, platform, provider="browserstack"):
        """Creates driver connecting to BrowserStack or Sauce Labs."""
        from appium import webdriver
        from appium.options import AppiumOptions

        platform_config = self.config[platform]
        cloud_config = self.config['cloud'][provider]

        username = os.environ.get(
            "BROWSERSTACK_USERNAME" if provider == "browserstack" else "SAUCE_USERNAME"
        )
        access_key = os.environ.get(
            "BROWSERSTACK_ACCESS_KEY" if provider == "browserstack" else "SAUCE_ACCESS_KEY"
        )

        server_url = f"https://{username}:{access_key}@{cloud_config['server_url'].replace('https://', '')}"

        options = AppiumOptions()
        options.platform_name = platform_config['platform_name']
        options.automation_name = platform_config['automation_name']

        if provider == "browserstack":
            options.set_capability("bstack:options", {
                "deviceName": cloud_config[f"{platform}_device"],
                "osVersion": platform_config['platform_version'],
                "projectName": "Mobile Automation Suite",
                "buildName": f"Build-{os.environ.get('GITHUB_RUN_NUMBER', 'local')}",
                "sessionName": f"{platform.capitalize()} Tests"
            })
        else:
            options.set_capability("appium:deviceName", cloud_config[f"{platform}_device"])
            options.set_capability("appium:platformVersion", platform_config['platform_version'])

        return webdriver.Remote(server_url, options=options)
