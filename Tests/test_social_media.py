import json
import time

import pytest
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_send_keys, safe_get_text

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\Car_Bike\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
@pytest.mark.smoke
def test_social_media(browserInstance):
    browserInstance.get("https://www.carandbike.com/")
    browserInstance.maximize_window()
    browserInstance.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    safe_click(browserInstance, Locators.youtube)
    browserInstance.switch_to.window(browserInstance.window_handles[0])
    safe_click(browserInstance, Locators.Twitter)
    browserInstance.switch_to.window(browserInstance.window_handles[0])
    safe_click(browserInstance, Locators.Instagram)
    browserInstance.switch_to.window(browserInstance.window_handles[0])
    safe_click(browserInstance, Locators.facebook)
    browserInstance.switch_to.window(browserInstance.window_handles[0])
    safe_click(browserInstance, Locators.Linkedin)
    browserInstance.switch_to.window(browserInstance.window_handles[0])
    safe_click(browserInstance, Locators.whatsup)
    browserInstance.switch_to.window(browserInstance.window_handles[0])
    print(safe_get_text(browserInstance,Locators.office_add))
