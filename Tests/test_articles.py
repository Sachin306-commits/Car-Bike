import json
import pytest
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_get_text

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\Car_Bike\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]


@pytest.mark.smoke
def test_about_us(browserInstance):
    browserInstance.get("https://www.carandbike.com/")

    browserInstance.maximize_window()
    safe_click(browserInstance, Locators.About_us)

    browserInstance.execute_script("window.scrollBy(0, 200);")
    safe_click(browserInstance, Locators.AboutUs1)

    browserInstance.get_screenshot_as_file("AboutUs.png")

    print(safe_get_text(browserInstance, Locators.highlights))

    # print(safe_get_text(driver, Locators.NEW_BIKE_LIST))
