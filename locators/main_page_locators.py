from selenium.webdriver.common.by import By

class MainPageLocators:
    COOCKIE_BUTTON = (By.ID, "rcc-confirm-button")
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")

    @staticmethod
    def question_locator(item_number):
        return (By.ID, f"accordion__heading-{item_number}")

    @staticmethod
    def answer_locator(item_number):
        return (By.XPATH, f"//div[@data-accordion-component='AccordionItemPanel' and @id='accordion__panel-{item_number}']/p")
