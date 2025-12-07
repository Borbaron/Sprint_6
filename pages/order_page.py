import allure
from pages.base_page import BasePage
from locators.order_locators import OrderLocators
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        self.click_on_element(OrderLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        self.scroll_to_element(OrderLocators.ORDER_BUTTON_BOT)
        self.click_on_element(OrderLocators.ORDER_BUTTON_BOT)

    @allure.step("Заполнить форму заказа: Имя={name}, Фамилия={surname}, Адрес={address}, Метро={metro}, Телефон={phone}")
    def fill_order_form_1(self, name, surname, address, metro, phone):
        self.send_keys_to_input(OrderLocators.NAME_PLACEHOLDER, name)
        self.send_keys_to_input(OrderLocators.SURNAME_PLACEHOLDER, surname)
        self.send_keys_to_input(OrderLocators.ADDRESS_PLACEHOLDER, address)
        metro_element = self.wait_for_element(OrderLocators.METRO_PLACEHOLDER)
        metro_element.send_keys(metro)
        metro_element.send_keys(Keys.ARROW_DOWN)
        metro_element.send_keys(Keys.ENTER)
        self.send_keys_to_input(OrderLocators.PHONE_PLACEHOLDER, phone)


    @allure.step("Кликнуть кнопку 'Далее'")
    def click_next_button(self):
        self.click_on_element(OrderLocators.NEXT_BUTTON)

    @allure.step("Заполнить форму аренды: Дата={date}, Срок аренды=3 суток, Цвет, Комментарий={comment}")
    def fill_order_form_2(self, date, comment):
        self.send_keys_to_input(OrderLocators.WHEN_PLACEHOLDER, date)

        self.send_keys_to_input(OrderLocators.WHEN_PLACEHOLDER, Keys.ENTER)

        self.click_on_element(OrderLocators.RENTAL_PLACEHOLDER)
        self.click_on_element(OrderLocators.OPTION_TROE_SUTOK)
        self.click_on_element(OrderLocators.SAMAKAT_COLOR)
        self.send_keys_to_input(OrderLocators.COMMENT_PLACEHOLDER, comment)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_on_element(OrderLocators.YES_BUTTON)

    @allure.step("Проверить сообщение об успешном заказе")
    def check_success_message(self):
        self.wait_for_element(OrderLocators.ORDER_SUCCESS_MESSAGE)

    @allure.step("Кликнуть на логотип Самоката")
    def click_samokat_logo(self):
        self.click_on_element(OrderLocators.SAMOKAT_LOGO)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_on_element(OrderLocators.YANDEX_LOGO)

