import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

@allure.feature("Навигация")
@allure.story("Логотипы")
class TestLogo:
    @allure.title("Клик на логотип Самоката ведёт на главную страницу")
    def test_scooter_logo_redirects_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.click_scooter_logo()
        assert driver.current_url == BASE_URL

    @allure.title("Клик на логотип Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        original_window = driver.current_window_handle
        main_page.click_yandex_logo()

        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        for handle in driver.window_handles:
            if handle != original_window:
                driver.switch_to.window(handle)
                break

        WebDriverWait(driver, 10).until(lambda d: d.current_url != "about:blank")
        assert "dzen.ru" in driver.current_url