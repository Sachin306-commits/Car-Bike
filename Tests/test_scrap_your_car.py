import json
import time

import pytest
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_send_keys, safe_get_text

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\Car_Bike\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
@pytest.mark.smoke
def test_scrap_your_car(browserInstance):
    browserInstance.get("https://www.carandbike.com/")
    browserInstance.maximize_window()
    safe_click(browserInstance, Locators.car_service_main)
    safe_click(browserInstance, Locators.scrap_your_car)
    time.sleep(10)
    print(safe_get_text(browserInstance,Locators.scrap_your_car_steps))
    print(safe_get_text(browserInstance,Locators.why_choose_car))