import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента с локатором: {locator}")
    def wait_for_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

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

    @allure.step("Ожидание открытия нового окна и загрузки URL, содержащего '{url_contains}'")
    def wait_for_new_window_and_url(self, url_contains, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_contains))

        return True
    
    @allure.step("Получение текущего URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на окно с номером: {window_number}")
    def switch_to_window(self, window_number):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step("Получение URL страницы по индексу вкладки: {index}")
    def get_url_by_tab_index(self, index):
        self.switch_to_window(index)
        return self.driver.current_url
