# test_new_bikes.py
import json

import pytest
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_get_text

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\Orange_ARM\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
@pytest.mark.smoke
def test_new_bikes(driver):
    driver.get("https://www.carandbike.com/")
    driver.maximize_window()
    safe_click(driver, Locators.NEW_BIKES)
    print(safe_get_text(driver, Locators.NEW_BIKE_LIST))
    safe_click(driver, Locators.BIKE_FILTER_BUTTON)
    safe_click(driver, Locators.SEARCH_BUTTON)
    #safe_click(driver, Locators.VIEW_ALL_NEW_BIKES)

    for _ in range(5):
        safe_click(driver, Locators.Bike_Stories)

    for _ in range(5):
        safe_click(driver, Locators.Commuter_arrow)
    safe_click(driver, Locators.Cruiser)
    for _ in range(5):
        safe_click(driver, Locators.Cruiser_arrow)
    safe_click(driver, Locators.Scooter)
    for _ in range(5):
        safe_click(driver, Locators.Scooter_arrow)

    for _ in range(5):
        safe_click(driver, Locators.Popular_Electric_Bikes)
    for _ in range(5):
        safe_click(driver, Locators.Newly_Launched_Bikes_arrow)

    safe_click(driver, Locators.Popular_Bikes)
    for _ in range(5):
        safe_click(driver, Locators.Popular_Bikes_arrow)
    safe_click(driver, Locators.Upcoming_Bikes)
    for _ in range(5):
        safe_click(driver, Locators.Upcoming_Bikes_arrow)

    safe_click(driver, Locators.One_lakh_to_half_lakh)
    for _ in range(5):
        safe_click(driver, Locators.One_lakh_to_half_lakh_arrow)
    safe_click(driver, Locators.Between_one_half_lakh_to_three_lakh)
    for _ in range(5):
        safe_click(driver, Locators.Between_one_half_lakh_to_three_lakh_arrow)

    print(safe_get_text(driver, Locators.Top_Brands))
