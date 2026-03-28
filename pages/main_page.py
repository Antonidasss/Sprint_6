import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    # Вопросы о важном (8 штук)
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

    # Кнопки заказа (уточнённые)
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//div[contains(@class, 'App_CookieConsent')]//button[contains(text(), 'да все привыкли')]")

    @allure.step("Клик по вопросу {index}")
    def click_question(self, index):
        question = self.find_element(self.QUESTION_LOCATORS[index])
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        self.click_element(self.QUESTION_LOCATORS[index])

    @allure.step("Получение текста ответа на вопрос {index}")
    def get_answer_text(self, index):
        return self.get_text(self.ANSWER_LOCATORS[index])

    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_order_button_top(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_order_button_bottom(self):
        self.click_element(self.ORDER_BUTTON_BOTTOM)

    @allure.step("Клик по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    @allure.step("Закрытие cookie‑консента")
    def accept_cookies(self):
        try:
            self.click_element(self.COOKIE_ACCEPT_BUTTON)
        except:
            pass