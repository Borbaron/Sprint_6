import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Принять куки")
    def coockie_accept(self):
        self.click_on_element(MainPageLocators.COOCKIE_BUTTON)

    @allure.step("Проскроллить до Вопросов о важном")
    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    @allure.step("Кликнуть на вопрос номер {item_number}")
    def click_on_question(self, item_number):
        locator = MainPageLocators.question_locator(item_number)
        self.click_on_element(locator)

    @allure.step("Получить текст ответа для вопроса номер {item_number}")
    def get_faq_text(self, item_number):
        locator = MainPageLocators.answer_locator(item_number)
        return self.get_text_on_element(locator)

