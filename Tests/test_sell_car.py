# test_sell_car.py
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
    safe_click(driver, Locators.SELL_CAR)
    safe_send_keys(driver, Locators.SELL_CAR_NAME, user_data["name"])
    safe_send_keys(driver, Locators.SELL_CAR_MOBILE, user_data["phone"])
    safe_click(driver, Locators.SELL_CAR_SUBMIT)
