# test_news_reviews.py
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
def test_news_and_reviews(driver):
    driver.get("https://www.carandbike.com/")
    driver.maximize_window()
    safe_click(driver, Locators.NEWS_REVIEWS_TAB)
    print(safe_get_text(driver, Locators.CATEGORY_SECTION))