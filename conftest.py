import pytest

from selenium import webdriver
from capture_screenshot.screenshot import take_screenshot

import os


driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser name: chrome or firefox"
    )

@pytest.fixture(scope="function")
def driver(request):
    global driver
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when in ("call", "setup"):
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'Reports')
            os.makedirs(reports_dir, exist_ok=True)
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")

            take_screenshot(driver, file_name)

            html = (
                '<div><img src="%s" style="width:304px; height:228px;" '
                'onclick="window.open(this.src)" align="right"/></div>' % file_name
            )
            extra.append(pytest_html.extras.html(html))
        report.extra = extra



