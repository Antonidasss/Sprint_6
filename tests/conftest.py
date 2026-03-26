import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    driver.maximize_window()
    # Попытка закрыть cookie сразу после загрузки страницы
    try:
        cookie_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'App_CookieConsent')]//button[contains(text(), 'да все привыкли')]"))
        )
        cookie_button.click()
    except:
        pass  # если окна нет, просто продолжаем
    yield driver
    driver.quit()