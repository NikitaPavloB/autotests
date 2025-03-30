import time
from pages.analytics.report_constructor.form_page_f1 import OperationsHelper
import logging
import allure
import pytest_check as check
from tests.conftest import save_screenshot_on_check_fail
@allure.feature('Проверка чекбоксов в Настройки отображения')
@allure.story('Общие сведения')
def test_analytics_form1(browser, login):
    logging.info('Запустили тест')
    test_page = OperationsHelper(browser)
    with allure.step('Проверка успешной авторизации'):
        if not check.equal(test_page.get_menu_text(),
                           'Доступные для работы модули:', 'Проверка текста меню'):
            save_screenshot_on_check_fail(browser, 'Проверка авторизации')
    with allure.step("Переход к модулю 'Конструктор отчетов'"):
        test_page.click_icon_stat()
        time.sleep(3)
        test_page.click_icon_constructor()
        time.sleep(3)
    with allure.step("Выбор тестового шаблона"):
        test_page.template_selection()
        time.sleep(5)
    with allure.step("чекбокса Средний многолетний за 10 лет"):
        test_page.select_average_10_years()
        time.sleep(3)
    if __name__ == "main":
        import pytest
        pytest.main()