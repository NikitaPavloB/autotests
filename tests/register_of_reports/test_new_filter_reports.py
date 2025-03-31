import time
import logging
import allure
import pytest
import pytest_check as check
from base.BaseApp import BasePage
from tests.conftest import save_screenshot_on_check_fail
from pages.register_of_reports.filter_new_reports_page import RegisterNewOperationsHelper

pytestmark = pytest.mark.order(2)


@allure.feature('Фильтрация в реестре отчетов - новая логика')
@allure.story('1. Фильтрация на районном уровне')
def test_new_filter_district_level(browser, login):
    logging.info('Запустили тест проверки фильтрации на районном уровне')
    test_page = RegisterNewOperationsHelper(browser)
    with allure.step("Переход к модулю 'Отчёты организаций Роспотребнадзора'"):
        test_page.click_icon_stat()
        time.sleep(2)
        test_page.click_reports_rospotrebnadzor_organizations()
    with allure.step("Выбор формы №12-23"):
        test_page.click_form_12_23()
        time.sleep(2)
    with allure.step("Выбор уровня видимости 'Районный'"):
        test_page.click_level()
        test_page.click_level_district()
        if not check.equal(test_page.get_check_district_lvl(),'Район', 'Проверка, что находимся на районном уровне'):
            save_screenshot_on_check_fail(browser, 'Проверка районного уровня')
    time.sleep(7)
    with allure.step("Выбор территории, региона и района"):
        test_page.click_territory_field()
        test_page.click_rf_btn()
        time.sleep(2)
        test_page.click_new_region_field()
        time.sleep(1)
        test_page.click_msk_btn()
        time.sleep(2)
        test_page.click_new_district_field()
        test_page.click_vostok_btn()
    with allure.step("Проверка успешной фильтрации на районном уровне"):
        if not check.equal(test_page.get_check_filter_district(), "Восточный", "Проверка успешной фильтрации района"):
            save_screenshot_on_check_fail(browser,'Проверка фильтрации по району')
    with allure.step("Проверка фильтрации по состоянию, периодичности и периоду"):
        test_page.click_new_status_btn()
        test_page.click_approved_btn()
        test_page.click_new_periodicity_btn()
        test_page.click_quarterly_btn()
        time.sleep(2)
        test_page.click_period_year_btn()
        test_page.click_year_calendar_btn()
        test_page.enter_starting_year_calendar('2054')
        test_page.enter_end_year_calendar('2054')
    with allure.step("Проверка успешной сортировки по состоянию и периоду"):
        if not check.equal(test_page.get_check_sort_status(), "Утвержден", "Выбран статус 'Утвержден'"):
            save_screenshot_on_check_fail(browser, "Проверка состояния")
        if not check.is_true("2054" in test_page.get_check_sort_period()):
            save_screenshot_on_check_fail(browser, "Проверка сортировки года")
    logging.info('Закончили тест проверки фильтрации на районном уровне')
    with allure.step("Перезагружаем страницу для очистки полей в реестре"):
        test_page.reload_page()
        time.sleep(2)


@allure.feature('Фильтрация в реестре отчетов - новая логика')
@allure.story('2. Фильтрация на региональном уровне')
def test_new_filter_region_level(browser):
    logging.info('Запустили тест проверки фильтрации на региональном уровне')
    test_page = RegisterNewOperationsHelper(browser)
    with allure.step("Выбор уровня видимости 'Региональный'"):
        test_page.click_level()
        test_page.click_level_region()
        if not check.equal(test_page.get_new_check_region_lvl(),'Регион', 'Проверка, что находимся на региональном уровне'):
            save_screenshot_on_check_fail(browser, 'Проверка регионального уровня')
    time.sleep(2)
    with allure.step("Выбор территории и региона"):
        test_page.click_territory_field()
        test_page.click_rf_btn()
        time.sleep(2)
        test_page.click_new_region_field()
        time.sleep(1)
        test_page.click_msk_btn()
        time.sleep(2)
    with allure.step("Проверка успешной фильтрации на региональном уровне"):
        if not check.equal(test_page.get_check_filter_region(), "г. Москва", "Проверка успешной фильтрации региона"):
            save_screenshot_on_check_fail(browser,'Проверка фильтрации по региону')
    with allure.step("Проверка фильтрации по состоянию, периодичности и периоду"):
        test_page.click_new_status_btn()
        test_page.click_approved_btn()
        test_page.click_new_periodicity_btn()
        test_page.click_quarterly_btn()
        time.sleep(2)
        test_page.click_period_year_btn()
        test_page.click_year_calendar_btn()
        test_page.enter_starting_year_calendar('2054')
        test_page.enter_end_year_calendar('2054')
    with allure.step("Проверка успешной сортировки по состоянию и периоду"):
        if not check.equal(test_page.get_check_sort_status(), "Утвержден", "Выбран статус 'Утвержден'"):
            save_screenshot_on_check_fail(browser, "Проверка состояния")
        if not check.is_true("2054" in test_page.get_check_sort_period()):
            save_screenshot_on_check_fail(browser, "Проверка сортировки года")
    logging.info('Закончили тест проверки фильтрации на региональном уровне')
    with allure.step("Перезагружаем страницу для очистки полей в реестре"):
        test_page.reload_page()
        time.sleep(2)


@allure.feature('Фильтрация в реестре отчетов - новая логика')
@allure.story('3. Фильтрация на федеральном уровне')
def test_new_filter_federal_level(browser):
    logging.info('Запустили тест проверки фильтрации на федерального уровне')
    test_page = RegisterNewOperationsHelper(browser)
    with allure.step("Выбор уровня видимости 'Федерального'"):
        test_page.click_level()
        test_page.click_level_federal()
    with allure.step("Проверка фильтрации по состоянию, периодичности и периоду"):
        test_page.click_new_status_btn()
        test_page.click_approved_btn()
        test_page.click_new_periodicity_btn()
        test_page.click_quarterly_btn()
        time.sleep(2)
        test_page.click_period_year_btn()
        test_page.click_year_calendar_btn()
        test_page.enter_starting_year_calendar('2054')
        test_page.enter_end_year_calendar('2054')
    with allure.step("Проверка успешной сортировки по состоянию и периоду"):
        if not check.equal(test_page.get_check_sort_status(), "Утвержден", "Выбран статус 'Утвержден'"):
            save_screenshot_on_check_fail(browser, "Проверка состояния")
        if not check.is_true("2054" in test_page.get_check_sort_period()):
            save_screenshot_on_check_fail(browser, "Проверка сортировки года")
    logging.info('Закончили тест проверки фильтрации на федеральном уровне')





