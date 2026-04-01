# Mobile Automation Suite

![Tests](https://github.com/VivekanandUsingh/mobile-automation-suite/actions/workflows/mobile-tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Appium](https://img.shields.io/badge/Appium-3.1-purple)
![Platforms](https://img.shields.io/badge/Platforms-Android%20%7C%20iOS-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

[![Allure Report](https://img.shields.io/badge/Allure-Report-orange)](https://vivekanandusingh.github.io/mobile-automation-suite/)

A production-grade mobile test automation framework built with Python and Appium. Covers Android and iOS with a unified Page Object Model, supports three execution modes (mock, local device, cloud farm), and includes cross-platform parity tests.

---

## Framework Architecture

```
mobile-automation-suite/
├── config/
│   └── config.yaml              # Platform caps, devices, cloud credentials
├── framework/
│   ├── driver_factory.py        # Multi-mode driver: mock / local / cloud
│   └── base_page.py             # Shared mobile page utilities
├── pages/
│   └── mobile_pages.py          # Login, Products, Cart page objects
├── tests/
│   ├── test_android.py          # Android test suite (14 tests)
│   ├── test_ios.py              # iOS test suite (18 tests)
│   └── (cross-platform in iOS) # Cross-platform parity tests (4 tests)
├── reports/                     # HTML reports + screenshots
├── .github/
│   └── workflows/
│       └── mobile-tests.yml     # GitHub Actions CI/CD
├── conftest.py                  # Android + iOS fixtures
├── pytest.ini                   # pytest configuration
└── requirements.txt             # Dependencies
```

---

## Three Execution Modes

| Mode | When To Use | Requires |
|---|---|---|
| `mock` | CI/CD, portfolio demo, development | Nothing — runs anywhere |
| `local` | Real device or emulator testing | Appium server + device/emulator |
| `cloud` | Full device farm regression | BrowserStack or Sauce Labs account |

Switch modes via environment variable — no code changes needed:

```bash
# Mock mode (default — no device needed)
EXECUTION_MODE=mock pytest

# Local device/emulator
EXECUTION_MODE=local pytest

# BrowserStack cloud
EXECUTION_MODE=cloud CLOUD_PROVIDER=browserstack pytest
```

---

## Test Coverage

| Suite | Tests | Platform |
|---|---|---|
| Android Login | 6 tests | Android |
| Android Products | 5 tests | Android |
| Android Cart | 3 tests | Android |
| iOS Login | 6 tests | iOS |
| iOS Products | 5 tests | iOS |
| iOS Cart | 3 tests | iOS |
| Cross-Platform Parity | 4 tests | Android + iOS |
| **Total** | **32 tests** | |

---

## What This Framework Demonstrates

- **Unified Page Object Model** — single page class works across Android and iOS
- **Driver Factory pattern** — cleanly separates driver creation from test logic
- **Multi-mode execution** — mock for CI/CD, local for dev, cloud for regression
- **Cross-platform parity testing** — explicitly validates consistent behaviour across OS
- **Screenshot on action** — captures device state at key test points
- **Context switching** — native app and WebView context support built in
- **Cloud-ready config** — BrowserStack and Sauce Labs pre-configured, secrets-managed

---

## Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/VivekanandUsingh/mobile-automation-suite.git
cd mobile-automation-suite
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run in mock mode (no device needed)**
```bash
EXECUTION_MODE=mock pytest -v
```

**4. Run Android tests only**
```bash
EXECUTION_MODE=mock pytest tests/test_android.py -v
```

**5. Run iOS tests only**
```bash
EXECUTION_MODE=mock pytest tests/test_ios.py -v
```

**6. Run with local Appium server**
```bash
# Start Appium server first
appium

# Then run tests
EXECUTION_MODE=local pytest -v
```

---

## Cloud Device Farm Configuration

### BrowserStack
```bash
export EXECUTION_MODE=cloud
export CLOUD_PROVIDER=browserstack
export BROWSERSTACK_USERNAME=your_username
export BROWSERSTACK_ACCESS_KEY=your_key
pytest -v
```

### Sauce Labs
```bash
export EXECUTION_MODE=cloud
export CLOUD_PROVIDER=saucelabs
export SAUCE_USERNAME=your_username
export SAUCE_ACCESS_KEY=your_key
pytest -v
```

---

## CI/CD Pipeline

Runs automatically on every push and pull request in mock mode. To enable cloud execution, add BrowserStack credentials as GitHub Secrets and uncomment the `test-cloud` job in the workflow file.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Core language |
| Appium 3.1 | Mobile automation driver |
| pytest | Test runner |
| pytest-mock | Mock driver support |
| GitHub Actions | CI/CD pipeline |
| BrowserStack / Sauce Labs | Cloud device farm (optional) |

---

## Author

**Vivekanand Singh** — QA Architect with 20 years across Web, Mobile, API, and Platform Migration
[LinkedIn](https://www.linkedin.com/in/vivekanand09/) · [GitHub](https://github.com/VivekanandUsingh)
