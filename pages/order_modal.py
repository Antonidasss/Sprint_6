import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class OrderModal(BasePage):
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ')]")

    @allure.step("Подтверждение заказа (кнопка 'Да')")
    def confirm_order(self):
        # Ждём появления модального окна
        self.wait.until(EC.visibility_of_element_located(self.MODAL_WINDOW))
        # Ждём, пока кнопка 'Да' станет кликабельной
        self.click_element(self.CONFIRM_BUTTON)

    @allure.step("Получение текста сообщения об успешном создании заказа")
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)