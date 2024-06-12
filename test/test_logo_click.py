import allure
from data import Data
from pages.main_page import MainPage
from conftest import driver

class TestHeaderLogoClick:

    @allure.title('Тест нажатия на логотип "Самокат" в хедере страницы')
    @allure.description('Тест, что при нажатии на логотип "Самокат" в хедере страницы открывается главная страница сайта')
    def test_header_logo_samokat_click(self, driver):
        main_page = MainPage(driver)

        main_page.click_to_cooke_accept()
        main_page.click_to_order_button_on_header()
        main_page.click_to_samokat_logo()
        assert "на пару дней" in main_page.get_heading_text()

    @allure.title('Тест нажатия на логотип "Яндекс" в хедере страницы')
    @allure.description('Тест, что при нажатии на логотип "Яндекс" в хедере страницы открывается главная страница Дзена')
    def test_header_logo_yandex_click(self, driver):
        main_page = MainPage(driver)

        main_page.click_to_cooke_accept()
        main_page.click_to_yandex_logo()
        main_page.switch_tab_on_browserer()
        main_page.wait_loading_site_Dzen()
        assert main_page.get_url_dzen() == Data.URL_DZEN