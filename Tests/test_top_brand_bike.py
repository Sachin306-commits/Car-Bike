import json
import time

import pytest
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_send_keys

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\Car_Bike\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
@pytest.mark.smoke
def test_sell_car(browserInstance):
    browserInstance.get("https://www.carandbike.com/")
    browserInstance.maximize_window()
    safe_click(browserInstance,Locators.Royal)
    safe_click(browserInstance,Locators.Royal_review)
    safe_click(browserInstance,Locators.cross1)
    safe_click(browserInstance,Locators.Varrient)
    safe_click(browserInstance,Locators.cross2)
    safe_click(browserInstance,Locators.Royal_compare)
    safe_click(browserInstance,Locators.Royal_compare1)
    safe_click(browserInstance, Locators.Royal_compare2)
    safe_click(browserInstance, Locators.Royal_compare3)
    safe_click(browserInstance,Locators.Royal_compare_button)
    time.sleep(5)
    browserInstance.execute_script("window.scrollBy(0,725);")
    safe_click(browserInstance, Locators.royal_color)
    safe_click(browserInstance, Locators.expert_rating)
    safe_click(browserInstance, Locators.Engine_Performance)
    safe_click(browserInstance, Locators.Dimension_Weight)
    safe_click(browserInstance, Locators.Fuel_Efficiency)
    safe_click(browserInstance, Locators.Suspension_Brakes)
    safe_click(browserInstance, Locators.Standard_Features)



