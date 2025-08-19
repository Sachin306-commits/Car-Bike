import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Utility functions
import os
import time



import os
import time

def capture_screenshot(driver, screenshot_name, folder_name="capture_screenshot"):
    """
    Captures a screenshot and saves it to the given folder.
    """
    base_dir = os.getcwd()
    screenshot_dir = os.path.join(base_dir, folder_name)
    os.makedirs(screenshot_dir, exist_ok=True)

    # Add timestamp to avoid overwriting
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(screenshot_dir, f"{screenshot_name}_{timestamp}.png")

    driver.get_screenshot_as_file(file_path)
    print(f"✅ Screenshot saved at: {file_path}")

    return file_path



def safe_click(driver, xpath, timeout=30):
    for _ in range(3):
        try:
            WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            ).click()
            break
        except StaleElementReferenceException:
            time.sleep(10)

def safe_send_keys(driver, xpath, value, timeout=30):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    ).send_keys(value)

def safe_get_text(driver, xpath, timeout=30):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    ).text
