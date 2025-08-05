# test_compare_vehicles.py
import json

import pytest
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_get_text
test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\Car_Bike\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
@pytest.mark.smoke
def test_compare_vehicles(browserInstance):
    browserInstance.get("https://www.carandbike.com/")
    browserInstance.maximize_window()
    print(safe_get_text(browserInstance, Locators.COMPARISON_CARD))
    safe_click(browserInstance, Locators.VIEW_ALL_COMPARISON)

    # Car 1
    safe_click(browserInstance, Locators.SELECT_CAR_1_MAKE)
    safe_click(browserInstance, Locators.LAND_ROVER_OPTION_1)
    safe_click(browserInstance, Locators.SELECT_CAR_1_MODEL)
    safe_click(browserInstance, Locators.CAR_MODEL_OPTION_1)
    safe_click(browserInstance, Locators.SELECT_CAR_1_VARIANT)
    safe_click(browserInstance, Locators.CAR_VARIANT_OPTION_1)

    # Car 2
    safe_click(browserInstance, Locators.SELECT_CAR_2_MAKE)
    safe_click(browserInstance, Locators.LAND_ROVER_OPTION_2)
    safe_click(browserInstance, Locators.SELECT_CAR_2_MODEL)
    safe_click(browserInstance, Locators.CAR_MODEL_OPTION_2)
    safe_click(browserInstance, Locators.SELECT_CAR_2_VARIANT)
    safe_click(browserInstance, Locators.CAR_VARIANT_OPTION_2)

    # Car 3
    safe_click(browserInstance, Locators.SELECT_CAR_3_MAKE)
    safe_click(browserInstance, Locators.LAND_ROVER_OPTION_3)
    safe_click(browserInstance, Locators.SELECT_CAR_3_MODEL)
    safe_click(browserInstance, Locators.CAR_MODEL_OPTION_3)
    safe_click(browserInstance, Locators.SELECT_CAR_3_VARIANT)
    safe_click(browserInstance, Locators.CAR_VARIANT_OPTION_3)

    safe_click(browserInstance, Locators.COMPARE_BUTTON)
    print(safe_get_text(browserInstance, Locators.COMPARE_RESULT))