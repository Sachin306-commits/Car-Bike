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
def test_used_cars(browserInstance):
    browserInstance.get("https://www.carandbike.com/")
    browserInstance.maximize_window()
    safe_click(browserInstance,Locators.used_cars_button)
    safe_click(browserInstance,Locators.used_cars_button_2)
    #safe_click(browserInstance, Locators.first_button)
    #safe_click(browserInstance, Locators.below_3_Lakh)
    safe_click(browserInstance, Locators.three_to_6_lakh)
    safe_click(browserInstance, Locators.six_to_9_lakh)
    safe_click(browserInstance, Locators.nine_to_12_lakh)
    safe_click(browserInstance, Locators.twelve_to_18_Lakh)
    safe_click(browserInstance, Locators.Above_25_Lakh)
@pytest.mark.smoke
def body_type(browserInstance):
    safe_click(browserInstance,Locators.arrow_button_25)
    safe_click(browserInstance, Locators.Hatchback)
    safe_click(browserInstance, Locators.suv)
    safe_click(browserInstance, Locators.sedan)
    safe_click(browserInstance, Locators.muv)
    safe_click(browserInstance, Locators.Crossover)

@pytest.mark.smoke
def show_only(browserInstance):
    safe_click(browserInstance,Locators.arrow_button_26)
    safe_click(browserInstance, Locators.Rated_8_0)
    safe_click(browserInstance, Locators.Warranty_Available)
    safe_click(browserInstance, Locators.Financing_Available)
    safe_click(browserInstance, Locators.Discounted_Price)
    safe_click(browserInstance, Locators.Great_Deals)
@pytest.mark.smoke
def Manufactured_Year(browserInstance):
    safe_click(browserInstance, Locators.Manufactured_Year)
    safe_click(browserInstance, Locators.two_And_Newer)
    safe_click(browserInstance, Locators.three_And_Newer)
    safe_click(browserInstance, Locators.four)
    safe_click(browserInstance, Locators.five)
    safe_click(browserInstance, Locators.six)
    safe_click(browserInstance, Locators.seven)


