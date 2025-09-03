import json
from email.headerregistry import Address

import pytest
from selenium.webdriver.common.by import By
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_send_keys, safe_get_text, safe_select

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\Car_Bike\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
@pytest.mark.smoke
def test_keep_in_touch(browserInstance):
    browserInstance.get("https://www.carandbike.com/")
    browserInstance.maximize_window()
    safe_click(browserInstance,Locators.city_location)
    safe_click(browserInstance,Locators.city_click)
    safe_send_keys(browserInstance,Locators.city_click,user_data["city"])
    safe_click(browserInstance,Locators.city_select)
