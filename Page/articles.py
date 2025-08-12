from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_get_text

class articles:
    def __init__(self, driver):
        self.driver = driver


    def get_about_us1(self):
        return safe_click(self.driver, (By.XPATH, "(//span[@class='uppercase'])[8]"))

    def get_about_us(self):
        return safe_get_text(self.driver, (By.XPATH, "(//a[contains(@href, 'buying-a-new-car-full-payment-vs-emis-which-is-smarter-for-your-money')])[2]"))


    def capture_article_screenshot(self, filename="AboutUs.png"):
        self.driver.get_screenshot_as_file(filename)

    def scroll_to_take_img(self):
        self.driver.execute_script("window.scrollBy(0, 200);")

    def highlights(self):
        return safe_get_text(self.driver,"//div[@class='mb30']")


