from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, "//div[@aria-controls='accordion__panel-{}']"  # выпадающее поле с вопросами
    ANSWER_LOCATOR = By.ID, "accordion__panel-{}"  # выпадающее поле с ответами
    BUTTON_COOKE_ACCEPT_LOCATOR = By.XPATH, "//button[text()='да все привыкли']"  # кнопка "да все привыкли"
    QUESTION_SECTION = By.XPATH, "//div[text()='Вопросы о важном']/parent::div"  # раздел "Вопросы о важном"
    BASE_BUTTON_ORDER_HEADER_LOCATOR = By.XPATH, "//button[@class='Button_Button__ra12g']"  # кнопка "Заказать" в хедере
    BUTTON_DOWN_ORDER_LOCATOR = By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/child::button"  # кнопка "Заказать" внизу экрана
    LOGO_YANDEX_LOCATOR = By.XPATH, "//a[@href='//yandex.ru']"  # логотип "Яндекс" в хедере
    LOGO_SAMOKAT_LOCATOR = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"  # логотип "Самокат" в хедере
    HEADING_TEXT_LOCATOR = By.CLASS_NAME, "Home_Header__iJKdX"  # заголовок страницы "Самокат на пару дней"


class OrderPageLocators:
    TITLE_WHO_IS_THE_SCOOTER_FOR_LOCATOR = By.XPATH, "//div[@class='Order_Header__BZXOb']"  # заголовок страницы "Для кого самокат"
    NAME_LOCATOR = By.XPATH, "//input[@placeholder='* Имя']"  # поле ввода "Имя"
    SURNAME_LOCATOR = By.XPATH, "//input[@placeholder='* Фамилия']"  # поле ввода "Фамилия"
    ADDRESS_LOCATOR = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"  # поле ввода "Адрес"
    PHONE_LOCATOR = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"  # поле ввода "Телефон"
    KEY_SUBWAY_LOCATOR = By.XPATH, "//input[@placeholder='* Станция метро']/parent::div[@class='select-search__value']"  # поле "Станция метро"
    SUBWAY_LOCATOR = By.XPATH, "//input[@placeholder='* Станция метро']"  # поле ввода "Станция метро"
    SELECTION_STATION_LOCATOR = By.XPATH, "//ul[@class='select-search__options']" # выпадающий список станций метро
    BUTTON_NEXT_LOCATOR = By.XPATH, "//button[text()='Далее']"  # кнопка "Далее"
    TITLE_ABOUT_RENT_LOCATOR = By.XPATH, "//div[text()='Про аренду']"  # заголовок страницы "Про аренду"
    DATE_LOCATOR = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"  # поле "Когда привезти самокат"
    DROPDOWN_TODAY_LOCATOR = By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]"  # сегодняшний день в выпадающем календаре
    LIST_PERIOD_LOCATOR = By.XPATH, "//div[text()='* Срок аренды']"  # выпадающий список "Срок аренды"
    CHECK_THREE_DAYS_PERIOD_LOCATOR = By.XPATH, "//*[@class='Dropdown-option' and contains(text(), 'трое суток')]"  # элемент "трое суток" выпадающего списка "Срок аренды"
    CHECK_SEVEN_DAYS_PERIOD_LOCATOR = By.XPATH, "//*[@class='Dropdown-option' and contains(text(), 'семеро суток')]"  # элемент "семеро суток" выпадающего списка "Срок аренды"
    CHECK_COLOR_BLACK_LOCATOR = By.XPATH, "//label[@for='black']"  # чекбокс "Черный жемчуг"
    CHECK_COLOR_GREY_LOCATOR = By.XPATH, "//label[@for='grey']"  # чекбокс "Серая безысходность"
    COMMENT_LOCATOR = By.XPATH, "//input[@placeholder='Комментарий для курьера']"  # поле "Комментарий для курьера"
    BUTTON_ORDER_LOCATOR = By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"  # кнопка "Заказать"
    POPUP_CONFIRM_LOCATOR = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"  # всплывающее окно "Хотите оформить заказ?"
    POPUP_BUTTON_YES_LOCATOR = By.XPATH, "//button[text()='Да']"  # кнопка "Да" в всплывающем окне "Хотите оформить заказ?"
    POPUP_ORDER_COMPLETE_LOCATOR = By.XPATH, "//div[text()='Заказ оформлен']"  # надпись в попапе "Заказ оформлен"
    BUTTON_CHECK_STATUS = By.XPATH, "//button[text()='Посмотреть статус']"  # кнопка "Посмотреть статус" в попапе "Заказ оформлен"


