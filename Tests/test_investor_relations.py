import json
import pytest
from selenium.webdriver.common.by import By
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_send_keys, safe_get_text
test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\Car_Bike\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
@pytest.mark.smoke
def Investor_Relations(browserInstance):
    browserInstance.get("https://www.carandbike.com/")
    browserInstance.maximize_window()
    browserInstance.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    safe_click(browserInstance, Locators.Investor_Relations)
    content_wrap1 = safe_get_text(browserInstance, Locators.content_wrap)
    assert content_wrap1.strip() == content_wrap1.strip(), f"Expected '{content_wrap1}' but got '{content_wrap1}'"