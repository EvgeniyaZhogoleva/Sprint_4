import allure
from data import OrderInfo
from pages.order_page import OrderPage
from pages.main_page import MainPage
from conftest import driver


class TestOrderPage:

    @allure.title('Тест оформления заказа через кнопку в хедере страницы')
    @allure.description('Оформляем заказ через кнопку "Заказать" в хедере страницы, '
                        'с заполнением всех полей')
    def test_order_scooter_from_header_button(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        order_data = OrderInfo.ORDER_INFO_DICT

        main_page.click_to_cooke_accept()
        main_page.click_to_order_button_on_header()
        order_page.set_who_is_the_scooter_for(order_data['name'], order_data['surname'],
                                              order_data['address'], order_data['subway'],
                                              order_data['phone'])
        order_page.check_title_about_rent()
        order_page.set_when_to_bring_scooter(order_data['date'])
        order_page.choose_period_three_days()
        order_page.choose_color_scooter_black()
        order_page.add_comment_to_order(order_data['comment'])
        order_page.click_to_order_button()
        order_page.check_popup_confirmation()
        order_page.click_to_yes_button()
        assert 'Заказ оформлен' in order_page.check_order_confirmation()

    @allure.title('Тест оформления заказа через кнопку в нижней части страницы')
    @allure.description('Оформляем заказ через кнопку "Заказать" в нижней части страницы, с заполнением только обязательных полей')
    def test_order_scooter_from_down_button(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        order_data = OrderInfo.ORDER_INFO_DICT_DOWN_BUTTON

        main_page.click_to_cooke_accept()
        main_page.scroll_and_click_to_down_order_button()
        order_page.set_who_is_the_scooter_for(order_data['name'], order_data['surname'],
                                              order_data['address'], order_data['subway'],
                                              order_data['phone'])
        order_page.check_title_about_rent()
        order_page.set_when_to_bring_scooter(order_data['date'])
        order_page.choose_period_seven_days()
        order_page.click_to_order_button()
        order_page.check_popup_confirmation()
        order_page.click_to_yes_button()
        assert 'Заказ оформлен' in order_page.check_order_confirmation()