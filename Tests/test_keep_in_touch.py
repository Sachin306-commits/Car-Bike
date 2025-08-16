import json
from email.headerregistry import Address

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
def test_keep_in_touch(browserInstance):
    browserInstance.get("https://www.carandbike.com/")
    browserInstance.maximize_window()
    browserInstance.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    text_1 = safe_get_text(browserInstance,Locators.address)
    print(f"Address: {text_1}")

    text = safe_get_text(browserInstance, Locators.contact)
    print(f"contact: {text}")
    expected_contact = safe_get_text(browserInstance, Locators.contact)
    assert expected_contact.strip() == expected_contact.strip(), f"Expected '{expected_contact}' but got '{expected_contact}'"

    ''''.strip() in Python is a string method that removes whitespace 
    (or other specified characters) from both the beginning and the end of a string.
    Example:

           s = "   hello world   "
        print(s.strip())   #output -> "hello world"
'''
    text_2 = safe_get_text(browserInstance, Locators.email)
    print(f"email: {text_2}")
    text_3 = safe_get_text(browserInstance, Locators.copyright)
    print(f"copyright: {text_3}")






