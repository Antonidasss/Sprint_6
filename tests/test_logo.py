import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

@allure.feature("Навигация")
@allure.story("Логотипы")
class TestLogo:
    @allure.title("Клик на логотип Самоката ведёт на главную страницу")
    def test_scooter_logo_redirects_to_main(self, driver):
        """Тест: клик по логотипу Самоката возвращает на главную страницу"""
        main_page = MainPage(driver)
        main_page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Клик на логотип Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo_opens_dzen(self, driver):
        """Тест: клик по логотипу Яндекса открывает новое окно с Дзеном"""
        main_page = MainPage(driver)
        original_window = driver.current_window_handle
        main_page.click_yandex_logo()

        # Ждём появления второго окна
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        # Переключаемся на новое окно
        for handle in driver.window_handles:
            if handle != original_window:
                driver.switch_to.window(handle)
                break

        # Ждём, пока URL не станет отличным от about:blank (страница загрузится)
        WebDriverWait(driver, 10).until(lambda d: d.current_url != "about:blank")

        # Проверяем, что URL содержит dzen.ru (после редиректа)
        assert "dzen.ru" in driver.current_url