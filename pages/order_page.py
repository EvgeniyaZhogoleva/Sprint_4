import allure
from pages.base_page import BasePage
from locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Заполнение всех полей формы "Для кого самокат" и нажатие на кнопку "Далее"')
    def set_who_is_the_scooter_for(self,  name, surname, address, subway, phone):
        self.add_text_to_element(OrderPageLocators.NAME_LOCATOR, name)
        self.add_text_to_element(OrderPageLocators.SURNAME_LOCATOR, surname)
        self.add_text_to_element(OrderPageLocators.ADDRESS_LOCATOR, address)
        self.click_to_element(OrderPageLocators.KEY_SUBWAY_LOCATOR)
        self.add_text_to_element(OrderPageLocators.SUBWAY_LOCATOR, subway)
        self.click_to_element(OrderPageLocators.SELECTION_STATION_LOCATOR)
        self.add_text_to_element(OrderPageLocators.PHONE_LOCATOR, phone)
        self.click_to_element(OrderPageLocators.BUTTON_NEXT_LOCATOR)

    @allure.step('Проверка загрузки страницы "Оформление аренды"')
    def check_title_about_rent(self):
        return self.find_element_with_wait(OrderPageLocators.TITLE_ABOUT_RENT_LOCATOR)

    @allure.step('Заполнение полей формы "Когда привезти самокат"')
    def set_when_to_bring_scooter(self, date):
        self.add_text_to_element(OrderPageLocators.DATE_LOCATOR, date)
        self.click_to_element(OrderPageLocators.TITLE_ABOUT_RENT_LOCATOR)

    @allure.step('Выбор срока аренды "трое суток"')
    def choose_period_three_days(self):
        self.click_to_element(OrderPageLocators.LIST_PERIOD_LOCATOR)
        self.click_to_element(OrderPageLocators.CHECK_THREE_DAYS_PERIOD_LOCATOR)

    @allure.step('Выбор срока аренды "семеро суток"')
    def choose_period_seven_days(self):
        self.click_to_element(OrderPageLocators.LIST_PERIOD_LOCATOR)
        self.click_to_element(OrderPageLocators.CHECK_SEVEN_DAYS_PERIOD_LOCATOR)

    @allure.step('Выбор цвета самоката "Серая безысходность"')
    def choose_color_scooter_black(self):
        self.click_to_element(OrderPageLocators.CHECK_COLOR_BLACK_LOCATOR)

    @allure.step('Добавление комментария к заказу')
    def add_comment_to_order(self, comment):
        self.add_text_to_element(OrderPageLocators.COMMENT_LOCATOR, comment)

    @allure.step('Нажатие на кнопку "Заказать"')
    def click_to_order_button(self):
        self.click_to_element(OrderPageLocators.BUTTON_ORDER_LOCATOR)

    @allure.step('Проверка появление всплывающего окна подтверждения заказа')
    def check_popup_confirmation(self):
        return self.find_element_with_wait(OrderPageLocators.POPUP_CONFIRM_LOCATOR)

    @allure.step('Нажатие на кнопку "Да" во всплывающем окне подтверждения заказа')
    def click_to_yes_button(self):
        self.click_to_element(OrderPageLocators.POPUP_BUTTON_YES_LOCATOR)

    @allure.step('Проверка всплывающего окна офрмления заказа')
    def check_order_confirmation(self):
        return self.get_text_from_element(OrderPageLocators.POPUP_ORDER_COMPLETE_LOCATOR)