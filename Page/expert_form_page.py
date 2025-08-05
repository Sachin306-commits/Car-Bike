# expert_form_page.py
from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_send_keys, safe_get_text

class ExpertFormPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_home_and_capture_labels(self):
        safe_click(self.driver, (By.XPATH, "//a[contains(text(),'Home')]"))
        question_label = safe_get_text(self.driver, (By.XPATH, "//label[@for='question']"))
        head_label = safe_get_text(self.driver, (By.XPATH, "//h2[contains(text(),'Ask the Expert')]"))
        return question_label, head_label

    def submit_question(self, question, name, email):
        safe_send_keys(self.driver, (By.ID, "question"), question)
        safe_send_keys(self.driver, (By.ID, "name"), name)
        safe_send_keys(self.driver, (By.ID, "email"), email)
        safe_click(self.driver, (By.XPATH, "//button[contains(text(),'Submit')]"))

    def print_footer_links(self):
        for i in range(1, 7):
            footer_text = self.driver.find_element(By.XPATH, f"//footer//li[{i}]").text
            print(footer_text)
