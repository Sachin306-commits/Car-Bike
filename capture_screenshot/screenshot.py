# capture_screenshot/screenshot.py

def take_screenshot(driver, file_path):
    try:
        driver.get_screenshot_as_file(file_path)
    except Exception as e:
        print(f"[ERROR] Failed to capture screenshot: {e}")
