import json

import pytest
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_send_keys

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\Orange_ARM\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
@pytest.mark.smoke
def test_sell_car(driver):
    driver.get("https://www.carandbike.com/")
    driver.maximize_window()
    safe_click(driver,Locators.Royal)
    safe_click(driver,Locators.Royal_review)
    safe_click(driver,Locators.cross1)
    safe_click(driver,Locators.Varrient)
    safe_click(driver,Locators.cross2)
    safe_click(driver,Locators.Royal_compare)
    safe_click(driver,Locators.Royal_compare1)
    safe_click(driver, Locators.Royal_compare2)
    safe_click(driver, Locators.Royal_compare3)
    safe_click(driver,Locators.Royal_compare_button)

