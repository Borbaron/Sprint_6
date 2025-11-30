import allure
import pytest

import data
from pages.main_page import MainPage

# Список вопросов и ожидаемых ответов
questions_and_answers = [
    ("Сколько это стоит? И как оплатить?", "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    ("Хочу сразу несколько самокатов! Так можно?", "Да, конечно!"),  # ... (добавьте остальные)
    ("Как рассчитывается время аренды?", "Когда привезёте самокат — в этот момент начинается расчёт.")
]


class TestFaq:
    @pytest.mark.parametrize("question, expected_answer", questions_and_answers)
    @allure.title("Проверка FAQ: {question}")
    def test_faq_question(self, driver, question, expected_answer):
        main_page = MainPage(driver)
        main_page.coockie_accept()
        main_page.scroll_to_questions()

        main_page.click_on_question(question)
        assert main_page.check_faq_text(expected_answer)
