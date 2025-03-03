import time
from pages.register_of_reports.filter_reports_page import OperationsHelper
import logging
import allure
import pytest_check as check
from tests.conftest import save_screenshot_on_check_fail


@allure.feature('Фильтрация в реестре отчетов')
@allure.story('1. Фильтрация на организационном уровне')
def test_filter_organization_level(browser, login):
    logging.info('Запустили тест проверки фильтрации на организационном уровне')
    test_page = OperationsHelper(browser)
    with allure.step('Проверка успешной авторизации'):
        # assert test_page.get_menu_text() == 'Доступные для работы модули:'
        if not check.equal(test_page.get_menu_text(),'Доступные для работы модули:', 'Проверка текста меню'):
            save_screenshot_on_check_fail(browser, 'Проверка авторизации')
    with allure.step("Переход к модулю 'Мониторинг здоровья'"):
        test_page.click_icon_stat()
        test_page.click_health_monitoring()
    with allure.step("Выбор формы №1"):
        test_page.click_form_1()
    with allure.step("Выбор уровня видимости 'Организация'"):
        test_page.click_level()
        test_page.click_level_organization()
        # assert test_page.get_check_organization_lvl() == 'Организация'
        if not check.equal(test_page.get_check_organization_lvl(),'Организация', 'Проверка, что находимся на орг.уровне'):
            save_screenshot_on_check_fail(browser, 'Проверка уровня организации')
    time.sleep(4)
    with allure.step("Выбор региона и района"):
        test_page.click_region_field()
        test_page.click_msk_btn()
        test_page.click_district_field()
        test_page.click_vostok_btn()
    with allure.step("Ввод и выбор организации 'Альбион'"):
        test_page.click_organization_field()
        test_page.enter_org_name('альбион')
        test_page.click_albion_btn()
    with allure.step("Проверка выбранной организации"):
        # assert test_page.get_check_organization_albion() == 'ООО "АЛЬБИОН"'
        if not check.equal(test_page.get_check_organization_albion(), 'ООО "АЛЬБИОН"', 'Проверка успешной фильтрации орг.'):
            save_screenshot_on_check_fail(browser, 'Проверка Альбиона')
    with allure.step("Проверка фильтрации по состоянию, периодичности и периоду"):
        test_page.click_status_btn()
        test_page.click_approved_btn()
        test_page.click_periodicity_btn()
        test_page.click_monthly_btn()
        test_page.click_period_btn()
        test_page.click_year_calendar_btn()
        test_page.enter_starting_year_calendar('2054')
        test_page.enter_end_year_calendar('2054')
    with allure.step("Проверка успешной фильтрации по состоянию и периоду"):
        if not check.equal(test_page.get_check_sort_status(), "Утвержден", "Выбран статус 'Утвержден'"):
            save_screenshot_on_check_fail(browser, "Проверка состояния")
        if not check.is_true("2054" in test_page.get_check_sort_period()):
            save_screenshot_on_check_fail(browser, "Проверка сортировки года")
    logging.info('Закончили тест проверки фильтрации на орг. уровне')
    with allure.step("Сбросить все фильтры в реестре"):
        test_page.click_reset_filters_btn()
        if not check.equal(test_page.get_check_all_reg(), "РФ", "Проверка сброса всех фильтров"):
            save_screenshot_on_check_fail(browser,"Проверка кнопки сброса фильтров")


@allure.feature('Фильтрация в реестре отчетов')
@allure.story('2. Фильтрация на уровне район-города')
def test_filter_district_city_level(browser):
    logging.info('Запустили тест проверки фильтрации на уровне район-города')
    test_page = OperationsHelper(browser)
    with allure.step("Выбор уровня видимости 'Район-города'"):
        test_page.click_level()
        test_page.click_level_district_city()
        if not check.equal(test_page.get_check_district_city_lvl(),'Район города', 'Проверка, что находимся на уровне район-города'):
            save_screenshot_on_check_fail(browser, 'Проверка уровня "район-города"')
    with allure.step("Выбор региона и района"):
        test_page.click_region_field()
        test_page.click_msk_btn()
        time.sleep(2)
        test_page.click_district_field()
        test_page.click_vostok_btn()
    with allure.step("Выбор района-города"):
        test_page.click_district_city_field()
        test_page.click_veshnyaki_btn()
        if not check.equal(test_page.get_check_district_city_veshnyaki(), " муниципальный округ Вешняки ",
                           "Проверка успешной фильтрации района-города"):
            save_screenshot_on_check_fail(browser,'Проверка фильтрации по району-города')
    logging.info('Закончили тест проверки фильтрации на уровне район-города')
    with allure.step("Сбросить все фильтры в реестре"):
        test_page.click_reset_filters_btn()
        if not check.equal(test_page.get_check_all_reg(), "РФ", "Проверка сброса всех фильтров"):
            save_screenshot_on_check_fail(browser,"Проверка кнопки сброса фильтров")


@allure.feature('Фильтрация в реестре отчетов')
@allure.story('3. Фильтрация на районном уровне')
def test_filter_district_level(browser):
    logging.info('Запустили тест проверки фильтрации на районном уровне')
    test_page = OperationsHelper(browser)
    with allure.step("Выбор уровня видимости 'Районный'"):
        test_page.click_level()
        test_page.click_level_district()
        if not check.equal(test_page.get_check_district_lvl(),'Район', 'Проверка, что находимся на районном уровне'):
            save_screenshot_on_check_fail(browser, 'Проверка районного уровня')
    with allure.step("Выбор региона и района"):
        test_page.click_region_field()
        test_page.click_msk_btn()
        time.sleep(2)
        test_page.click_district_field()
        test_page.click_vostok_btn()
    with allure.step("Проверка успешной фильтрации на районном уровне"):
        if not check.equal(test_page.get_check_filter_district(), "Восточный", "Проверка успешной фильтрации района"):
            save_screenshot_on_check_fail(browser,'Проверка фильтрации по району')
    logging.info('Закончили тест проверки фильтрации районного уровня')
    with allure.step("Сбросить все фильтры в реестре"):
        test_page.click_reset_filters_btn()
        if not check.equal(test_page.get_check_all_reg(), "РФ", "Проверка сброса всех фильтров"):
            save_screenshot_on_check_fail(browser,"Проверка кнопки сброса фильтров")


@allure.feature('Фильтрация в реестре отчетов')
@allure.story('4. Фильтрация на региональном уровне')
def test_filter_region_level(browser):
    logging.info('Запустили тест проверки фильтрации на региональном уровне')
    test_page = OperationsHelper(browser)
    with allure.step("Выбор уровня видимости 'Региональный'"):
        test_page.click_level()
        test_page.click_level_region()
        if not check.equal(test_page.get_check_region_lvl(),'Регион', 'Проверка, что находимся на региональном уровне'):
            save_screenshot_on_check_fail(browser, 'Проверка регионального уровня')
    with allure.step("Выбор региона"):
        test_page.click_region_field()
        test_page.click_msk_btn()
        time.sleep(2)
    with allure.step("Проверка успешной фильтрации на региональном уровне"):
        if not check.equal(test_page.get_check_filter_region(), "г. Москва", "Проверка успешной фильтрации региона"):
            save_screenshot_on_check_fail(browser,'Проверка фильтрации по региону')
    logging.info('Закончили тест проверки фильтрации на региональном уровне')









