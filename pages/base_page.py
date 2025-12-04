import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента с локатором: {locator}")
    def wait_for_element(self, locator, timeout=20):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"DEBUG: Элемент с локатором {locator} не появился после {timeout} секунд!")
            raise

    @allure.step("Скролл до элемента c локатором: {locator}")
    def scroll_to_element(self, locator, timeout=20):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент c локатором: {locator}")
    def click_on_element(self, locator, timeout=20):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Получить текст элемента c локатором: {locator}")
    def get_text_on_element(self, locator, timeout=20):
        element = self.wait_for_element(locator)
        return element.text
    
    @allure.step("Ввести текст '{keys}' в поле ввода  c локатором: {locator}")
    def send_keys_to_input(self, locator, keys, timeout=20):
        element = self.wait_for_element(locator, timeout)
        element.send_keys(keys)