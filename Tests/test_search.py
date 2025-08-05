# test_search.py
import json
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_send_keys, safe_get_text

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\Orange_ARM\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
@pytest.mark.smoke
def test_search_bar(driver):
    driver.get("https://www.carandbike.com/")
    driver.maximize_window()
    safe_click(driver, Locators.SEARCH_INPUT)
    safe_send_keys(driver, Locators.SEARCH_INPUT, user_data["search_keyword"])
    time.sleep(2)
    search_result = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, Locators.SEARCH_RESULT))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", search_result)
    search_result.click()
    driver.get_screenshot_as_file("Kawasaki_650.png")

    print(safe_get_text(driver, Locators.OVERVIEW_SECTION))
    print(safe_get_text(driver, Locators.ABOUT_SECTION))
    print(safe_get_text(driver, Locators.EXPERT_REVIEW))
    print(safe_get_text(driver, Locators.QUICK_COMPARE))

    safe_click(driver, Locators.PERFORMANCE_TAB)
    safe_click(driver, Locators.COMFORT_TAB)
    safe_click(driver, Locators.FEATURES_TAB)
    safe_send_keys(driver, Locators.CITY_INPUT, user_data["city"])
    safe_click(driver, Locators.FIND_DEALER)
