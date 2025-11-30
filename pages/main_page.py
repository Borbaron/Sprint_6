import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Принять куки")
    def coockie_accept(self):
        self.click_on_element(MainPageLocators.COOCKIE_BUTTON)

    @allure.step("Кликнуть на выпадающий список")
    def click_on_list(self):
        self.click_on_element(MainPageLocators.QUESTION_0)

    @allure.step("Получить текст в открывающимся списке")
    def get_list_text(self):
        self.get_text_on_element(MainPageLocators.QUESTION_0_TEXT)

    @allure.step("Сравни текст в списке вопросов")
    def check_faq_text(self, expected_text):
        actual_text = self.get_text_on_element(MainPageLocators.QUESTION_LIST_TEXT)
        return actual_text == expected_text

    @allure.step("Подождать загрузки заголовка")
    def wait_for_title(self):
        self.wait_for_element(MainPageLocators.TITUL_SAMOKAT)

    @allure.step("Проскроллить до Вопросов о важном")
    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.QUESTION_0)

    @allure.step("Кликнуть на вопрос по его тексту")
    def click_on_question(self, question_text):
        question_locator = MainPageLocators.question_button(question_text)
        self.click_on_element(question_locator)

    @allure.step("Проверяем, что текст ответа соответствует ожидаемому")
    def check_faq_text(self, expected_text):
        actual_text = self.get_text_on_element(MainPageLocators.FAQ_TEXT)
        return expected_text in actual_text 



