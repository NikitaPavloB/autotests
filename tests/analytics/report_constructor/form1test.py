import time
from pages.analytics.report_constructor.form_page_f1 import OperationsHelper
import logging
import allure
import pytest_check as check
from tests.conftest import save_screenshot_on_check_fail


@allure.feature('Формирование отчета по Форма №1')
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
    with allure.step('Поле Форма'):
        test_page.click_form_field()
        test_page.enter_form_name("Форма 1")
        time.sleep(3)
    with allure.step("Поле Периодичность"):
        test_page.select_periodicity()
        if not check.equal(test_page.select_periodicity(), 'Ежемесячная'):
            save_screenshot_on_check_fail(browser, 'Поле Периодичность')
    with allure.step("Поле Вкладка"):
        test_page.select_tab()
        if not check.equal(test_page.select_tab(), 'Форма №1'):
            save_screenshot_on_check_fail(browser, 'Поле Вкладка')
    with allure.step("Атрибут Территории"):
        test_page.click_add_new_row()
        test_page.select_territory()
        time.sleep(2)
    with allure.step("Атрибут Зарегистрировано заболеваний..."):
        test_page.click_add_new_row()
        test_page.select_registered_diseases()
        time.sleep(2)
    with allure.step("Атрибута Год(а)"):
        test_page.click_add_new_column()
        test_page.select_year()
        test_page.click_yars_2022()
        time.sleep(2)
    with allure.step("Атрибут Месяц"):
        test_page.click_add_new_column()
        test_page.select_month()
        test_page.click_months()
        time.sleep(2)
    with allure.step("Атрибут Группы заболеваний"):
        test_page.click_new_condition()
        test_page.select_group_of_diseases()
        time.sleep(1)
        test_page.select_diagnosis()
    with allure.step("Атрибут Возрастные группы"):
        test_page.click_new_condition()
        test_page.select_age_groups()
        time.sleep(1)
        test_page.select_all_age()
        # if not check.equal(test_page.select_all_age(), 'Все возраста'):
        #     save_screenshot_on_check_fail(browser, 'Проверка значений атрибута Возрастные группы')
    with allure.step("Формирование отчета"):
        test_page.click_generate_report()
        time.sleep(5)
    with allure.step("Проверка таблицы"):
        test_page.get_table_data()
        time.sleep(2)

    with allure.step("Создание Пользовательского шаблона"):
        test_page.click_create_template()
        test_page.enter_template_name("Автотест 123456")
        test_page.click_save_template()
        time.sleep(5)
    with allure.step("Удаление существующего Пользовательского шаблона"):
        test_page.delete_template()
        time.sleep(2)
    if __name__ == "main":
        import pytest
        pytest.main()
