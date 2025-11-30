from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_0 = {By.ID, "accordion__heading-0"}
    QUESTION_1 = {By.ID, "accordion__heading-1"}
    QUESTION_2 = {By.ID, "accordion__heading-2"}
    QUESTION_3 = {By.ID, "accordion__heading-3"}
    QUESTION_4 = {By.ID, "accordion__heading-4"}
    QUESTION_5 = {By.ID, "accordion__heading-5"}
    QUESTION_6 = {By.ID, "accordion__heading-6"}
    QUESTION_7 = {By.ID, "accordion__heading-7"}
    QUESTION_0_TEXT = {By.XPATH, "//div[@data-accordion-component='AccordionItemPanel' and @id='accordion__panel-0']/p"}
    QUESTION_LIST_TEXT = {By.XPATH, "//div[@data-accordion-component='AccordionItemPanel' and contains(., 'Сутки — 400 рублей')]"}
    TITUL_SAMOKAT = {By.CLASS_NAME, "Home_Header__iJKdX"}
    COOCKIE_BUTTON = {By.XPATH, "//button[contains(text(), 'все привыкли')]"}
    FAQ_SECTION = {By.CLASS_NAME, "Home_FAQ__3uVm4"}

    @staticmethod
    def question_button(question_text):
        return (By.XPATH, f"//div[contains(text(), '{question_text}') and @class='accordion__button']/ancestor::div[@data-accordion-component='AccordionItem']//button")

    @staticmethod
    def card_number(card):
        return By.XPATH, f'//*[@id="root"]/div/main/section[2]/ul/li[{card}]'