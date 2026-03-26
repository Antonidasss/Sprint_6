from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class OrderPage(BasePage):
    # Первая форма: Для кого самокат
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая форма: Про аренду
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")
    COLOR_CHECKBOX = (By.XPATH, "//label[contains(text(), '{}')]/input")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")

    def fill_first_form(self, name, surname, address, metro_station, phone):
        """Заполнение первой формы заказа"""
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.SURNAME_INPUT, surname)
        self.send_keys(self.ADDRESS_INPUT, address)
        self.click_element(self.METRO_STATION_INPUT)
        metro_option = (By.XPATH, f"//button[@value='{metro_station}']")
        self.click_element(metro_option)
        self.send_keys(self.PHONE_INPUT, phone)
        self.click_element(self.NEXT_BUTTON)

    def fill_second_form(self, delivery_date, rental_period, color, comment):
        """Заполнение второй формы заказа"""
        self.send_keys(self.DELIVERY_DATE_INPUT, delivery_date)
        # Закрываем календарь нажатием Escape
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        self.click_element(self.RENTAL_PERIOD_DROPDOWN)
        period_locator = (self.RENTAL_PERIOD_OPTION[0], self.RENTAL_PERIOD_OPTION[1].format(rental_period))
        self.click_element(period_locator)
        if color:
            color_locator = (self.COLOR_CHECKBOX[0], self.COLOR_CHECKBOX[1].format(color))
            self.click_element(color_locator)
        self.send_keys(self.COMMENT_INPUT, comment)
        self.click_element(self.ORDER_BUTTON)