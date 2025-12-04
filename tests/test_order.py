import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

order_data = [
    {
        "name": "Иван",
        "surname": "Иванов",
        "address": "Москва, ул. Пушкина, д. 1",
        "metro": "Сокольники",
        "phone": "89991234567",
        "date": "01.01.2026",
        "comment": "Позвоните за час",
        "button_location": "top"
    },
    {
        "name": "Петр",
        "surname": "Петров",
        "address": "Санкт-Петербург, Невский пр., д. 2",
        "metro": "Первомайская",
        "phone": "89997654321",
        "date": "02.02.2026",
        "comment": "Домофон не работает",
        "button_location": "bottom"
    },
]


class TestOrder:
    @pytest.mark.parametrize("order", order_data)
    @allure.title("Оформление заказа")
    def test_order_scooter(self, driver, order):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.coockie_accept()

        if order["button_location"] == "top":
            order_page.click_order_button_top()
        else:
            order_page.click_order_button_bottom()
        order_page.fill_order_form_1(order["name"], order["surname"], order["address"], order["metro"], order["phone"])
        order_page.click_next_button()
        order_page.fill_order_form_2(order["date"], order["comment"])
        order_page.confirm_order()
        order_page.check_success_message()

    @allure.title("Проверка перехода на главную страницу по логотипу Самоката")
    def test_click_samokat_logo(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.coockie_accept()
        order_page.click_samokat_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Проверка перехода на страницу Дзена по логотипу Яндекса")
    def test_click_yandex_logo(self, driver):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.coockie_accept()
        order_page.click_yandex_logo()

        driver.switch_to.window(driver.window_handles[1])
        assert "dzen.ru" in driver.current_url
