from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Метод для ожидания появления элемента
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    # Метод для нажатия на элемент
    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()

    # Метод для ввода текста
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # Метод для получения текста
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    # Метод для скролла до элемента
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element_with_wait(locator))

    # Метод для форматирования локатора
    def format_locators(self, locator_1, num):
        method,  locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    # Метод для ожидания загрузки сайта
    def wait_loading_site(self, url):
        WebDriverWait(self.driver,10).until(expected_conditions.url_to_be(url))

    # Метод для получения текущего URL
    def get_current_url(self):
        return self.driver.current_url

    # Метод для переключения на новую вкладку
    def switch_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])