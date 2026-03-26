from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    # Локаторы вопросов о важном
    QUESTION_LOCATORS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7"),
    ]
    ANSWER_LOCATORS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7"),
    ]

    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")

    # Логотипы
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # Cookie‑консент
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//div[contains(@class, 'App_CookieConsent')]//button[contains(text(), 'да все привыкли')]")

    def click_question(self, index):
        """Клик по вопросу с указанным индексом (0-7)"""
        self.click_element(self.QUESTION_LOCATORS[index])

    def get_answer_text(self, index):
        """Получить текст ответа для вопроса"""
        return self.get_text(self.ANSWER_LOCATORS[index])

    def click_order_button_top(self):
        """Клик по верхней кнопке 'Заказать'"""
        self.click_element(self.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        """Клик по нижней кнопке 'Заказать'"""
        self.click_element(self.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self.click_element(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.click_element(self.YANDEX_LOGO)

    def accept_cookies(self):
        """Закрыть всплывающее окно с согласием на cookie"""
        try:
            self.click_element(self.COOKIE_ACCEPT_BUTTON)
        except:
            pass  # Если окна нет, просто продолжаем