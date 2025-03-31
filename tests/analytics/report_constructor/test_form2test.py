import time
from pages.analytics.report_constructor.form_page_f1 import OperationsHelper
from pages.analytics.report_constructor.form_page_f2 import OperationsHelper2
import logging
import allure
import pytest_check as check
from tests.conftest import save_screenshot_on_check_fail
@allure.feature('Формирование отчета по Форма №2')
@allure.story('Общие сведения')
def test_analytics_form1(browser, login):
    logging.info('Запустили тест')
    test_page = OperationsHelper(browser)
    test_page2 = OperationsHelper2(browser)
    with allure.step('Проверка успешной авторизации'):
        if not check.equal(test_page.get_menu_text(),
                           'Доступные для работы модули:', 'Проверка текста меню'):
            save_screenshot_on_check_fail(browser, 'Проверка авторизации')
    with allure.step("Переход к модулю 'Конструктор отчетов'"):
        test_page.click_icon_stat()
        time.sleep(3)
        test_page.click_icon_constructor()
        time.sleep(3)
    with allure.step('Поле Форма'):
        test_page.click_form_field()
        test_page2.enter_form_name('Форма 2')
    with allure.step("Поле Периодичность"):
        test_page.select_periodicity()
        if not check.equal(test_page.select_periodicity(), 'Ежемесячная'):
            save_screenshot_on_check_fail(browser, 'Поле Периодичность')
    # with allure.step("Поле Вкладка"):

    if __name__ == "main":
        import pytest
        pytest.main()