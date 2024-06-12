import allure
import pytest
from pages.main_page import MainPage
from data import AnswerText
from conftest import driver

class TestQuestionOnPage:
    @allure.title('Тест что ответы на вопросы верны')
    @allure.description('Тест что ответы на восемь вопросов верны')
    @pytest.mark.parametrize(
        "num, expected",
        [
            (0, AnswerText.ANSWER_0),
            (1, AnswerText.ANSWER_1),
            (2, AnswerText.ANSWER_2),
            (3, AnswerText.ANSWER_3),
            (4, AnswerText.ANSWER_4),
            (5, AnswerText.ANSWER_5),
            (6, AnswerText.ANSWER_6),
            (7, AnswerText.ANSWER_7)
        ])
    def test_questions(self, driver, num, expected):
        main_page = MainPage(driver)

        main_page.click_to_cooke_accept()
        main_page.scroll_to_question()
        assert main_page.get_answer_text(num) == expected
