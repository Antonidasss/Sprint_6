import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.order_modal import OrderModal

@allure.feature("Заказ самоката")
@allure.story("Позитивный сценарий")
class TestOrder:
    @allure.title("Оформление заказа с разными наборами данных и разными кнопками")
    @pytest.mark.parametrize("button_locator, order_data", [
        ("top", {
            "name": "Иван",
            "surname": "Иванов",
            "address": "Москва, Красная площадь, 1",
            "metro_station": "1",
            "phone": "+79001234567",
            "delivery_date": "01.12.2024",
            "rental_period": "сутки",
            "color": "чёрный жемчуг",
            "comment": "Позвонить за час"
        }),
        ("bottom", {
            "name": "Петр",
            "surname": "Петров",
            "address": "Санкт-Петербург, Невский проспект, 2",
            "metro_station": "2",
            "phone": "+79109876543",
            "delivery_date": "02.12.2024",
            "rental_period": "двое суток",
            "color": "серая безысходность",
            "comment": "Оставить у двери"
        })
    ])
    def test_order_scooter(self, driver, button_locator, order_data):
        """Тест оформления заказа"""
        main_page = MainPage(driver)
        main_page.accept_cookies()

        if button_locator == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        order_page = OrderPage(driver)
        order_page.fill_first_form(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro_station"],
            order_data["phone"]
        )
        order_page.fill_second_form(
            order_data["delivery_date"],
            order_data["rental_period"],
            order_data["color"],
            order_data["comment"]
        )

        order_modal = OrderModal(driver)
        order_modal.confirm_order()

        success_message = order_modal.get_success_message()
        assert "Заказ оформлен" in success_message