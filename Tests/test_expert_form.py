
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
def test_expert_form_and_footer(browserInstance):
    browserInstance.get("https://www.carandbike.com/")
    browserInstance.maximize_window()
    safe_click(browserInstance, Locators.HOME_BUTTON)
    print(safe_get_text(browserInstance, Locators.QUESTION_LABEL))
    print(safe_get_text(browserInstance, Locators.HEAD_LABEL))

    safe_send_keys(browserInstance, Locators.QUESTION_BOX, "Please suggest a bike under 10 lakhs")
    safe_send_keys(browserInstance, Locators.NAME_FIELD, user_data["name"])
    safe_send_keys(browserInstance, Locators.EMAIL_FIELD, user_data["email"])
    safe_click(browserInstance, Locators.SUBMIT_BUTTON)
    #About Us
    print(safe_get_text(browserInstance,Locators.About_us))

