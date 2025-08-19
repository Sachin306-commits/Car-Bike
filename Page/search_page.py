# search_page.py
from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_send_keys, safe_get_text

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_search_keyword(self, keyword):
        safe_click(self.driver, (By.XPATH, "//input[@id='globalSearch']"))
        safe_send_keys(self.driver, (By.XPATH, "//input[@id='globalSearch']"), keyword)

    def click_search_result(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        result = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='search-results']//a"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", result)
        result.click()

    def capture_result_screenshot(self, filename="Kawasaki_6501.png"):
        self.driver.get_screenshot_as_file(filename)

    def get_overview_text(self):
        return safe_get_text(self.driver, (By.XPATH, "//h2[contains(text(),'Overview')]"))

    def get_about_text(self):
        return safe_get_text(self.driver, (By.XPATH, "//div[contains(text(),'About')]"))

    def get_expert_review(self):
        return safe_get_text(self.driver, (By.XPATH, "//div[contains(text(),'Expert Review')]"))

    def get_quick_compare(self):
        return safe_get_text(self.driver, (By.XPATH, "//h3[contains(text(),'Quick Compare')]"))

    def click_performance_tab(self):
        safe_click(self.driver, (By.XPATH, "//li[text()='Performance']"))

    def click_comfort_tab(self):
        safe_click(self.driver, (By.XPATH, "//li[text()='Comfort']"))

    def click_features_tab(self):
        safe_click(self.driver, (By.XPATH, "//li[text()='Features']"))

    def enter_city_and_find_dealer(self, city):
        safe_send_keys(self.driver, (By.XPATH, "//input[@placeholder='Enter city']"), city)
        safe_click(self.driver, (By.XPATH, "//button[contains(text(),'Find Dealer')]"))
