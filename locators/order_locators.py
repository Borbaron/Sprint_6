from selenium.webdriver.common.by import By

class OrderLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOT = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']")

    NAME_PLACEHOLDER = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_PLACEHOLDER = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_PLACEHOLDER = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_PLACEHOLDER = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_PLACEHOLDER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    NEXT_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    WHEN_PLACEHOLDER = (By.XPATH, "//input[@type='text' and @placeholder='* Когда привезти самокат']")
    RENTAL_PLACEHOLDER = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    SAMAKAT_COLOR = (By.XPATH, "//input[@id='black']/parent::label")
    COMMENT_PLACEHOLDER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    OPTION_TROE_SUTOK = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ')]")
    SAMOKAT_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    YES_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")