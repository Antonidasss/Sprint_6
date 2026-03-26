from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class OrderModal(BasePage):
    # Локатор модального окна (класс может меняться, используем частичное совпадение)
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ')]")

    def confirm_order(self):
        """Подтверждение заказа: ждём появления окна, затем кликаем 'Да'"""
        # Ждём, пока модальное окно станет видимым
        self.wait.until(EC.visibility_of_element_located(self.MODAL_WINDOW))
        # Ждём, пока кнопка 'Да' станет кликабельной, и кликаем
        self.click_element(self.CONFIRM_BUTTON)

    def get_success_message(self):
        """Получение текста об успешном создании заказа"""
        return self.get_text(self.SUCCESS_MESSAGE)