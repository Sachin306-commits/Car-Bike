# test_search.py
import json
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_send_keys, safe_get_text, capture_screenshot

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\Car_Bike\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
@pytest.mark.smoke
def test_search_bar(browserInstance):
    browserInstance.get("https://www.carandbike.com/")
    browserInstance.maximize_window()
    safe_click(browserInstance, Locators.SEARCH_INPUT)
    safe_send_keys(browserInstance, Locators.SEARCH_INPUT, user_data["search_keyword"])
    safe_click(browserInstance,Locators.SEARCH_RESULT)

    capture_screenshot(browserInstance, "Kawasaki_6501")


    print(safe_get_text(browserInstance, Locators.OVERVIEW_SECTION))
    print(safe_get_text(browserInstance, Locators.ABOUT_SECTION))
    print(safe_get_text(browserInstance, Locators.EXPERT_REVIEW))
    print(safe_get_text(browserInstance, Locators.QUICK_COMPARE))

    safe_click(browserInstance, Locators.PERFORMANCE_TAB)
    safe_click(browserInstance, Locators.COMFORT_TAB)
    safe_click(browserInstance, Locators.FEATURES_TAB)
    safe_send_keys(browserInstance, Locators.CITY_INPUT, user_data["city"])
    safe_click(browserInstance, Locators.FIND_DEALER)
