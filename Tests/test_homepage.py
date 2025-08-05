# test_homepage.py
import json

import pytest
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_get_text

test_data_path =r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\Car_Bike\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
@pytest.mark.smoke
def test_navigate_and_scroll(browserInstance):
    browserInstance.get("https://www.carandbike.com/")
    browserInstance.maximize_window()
    browserInstance.execute_script("window.scrollBy(0,720);")
    print(safe_get_text(browserInstance, Locators.COVER_STORY_TEXT))
    safe_click(browserInstance, Locators.BIKE_BUTTON)

    for _ in range(5):
        safe_click(browserInstance, Locators.RIGHT_ARROW_SECTION_2)

    for _ in range(5):
        safe_click(browserInstance, Locators.RIGHT_ARROW_SECTION_4)

    print(safe_get_text(browserInstance, Locators.FIRST_CAR_BRAND))