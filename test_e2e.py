# test_e2e.py
import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json



from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    TimeoutException,
)
from Utils.selenium_helpers import safe_click, safe_send_keys, safe_get_text
from Utils.locators import Locators

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\Car_Bike\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]


def run_all():
    pytest.main([
        "tests/test_homepage.py",
        "tests/test_compare_vehicles.py",
        "tests/test_search.py",
        "tests/test_sell_car.py",
        "tests/test_new_bikes.py",
        "tests/test_expert_form.py",
        "tests/test_news_reviews.py"
        "tests/test_articles.py"
        "tests/test_budget_bike_button_check.py"
        "tests/test_first_look.py"
        "tests/test_investor_relations.py"
        "tests/test_keep_in_touch.py"
        "tests/test_scrap_your_car.py"
        "tests/test_social_media.py"
        "tests/test_top_brand_bike.py"

    ])

if __name__ == "__main__":
    run_all()
