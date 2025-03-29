import allure
from base.BaseApp import BasePage
from selenium.webdriver.common.by import By


class RegistersCommonLocators:
    # Уровень видимости
    LOCATOR_LEVEL = (By.ID, "level")
    # Федеральный уровень
    LOCATOR_LEVEL_CONSOLIDATED = (By.ID, "formLevel_consolidated")
    # Региональный уровень
    LOCATOR_LEVEL_REGIONAL = (By.ID, "formLevel_regional")
    # Районный уровень
    LOCATOR_LEVEL_DISTRICT = (By.ID, "formLevel_district")
    # Район-города уровень
    LOCATOR_LEVEL_DISTRICT_CITY = (By.ID, "formLevel_district_city")
    # Организационный уровень
    LOCATOR_LEVEL_ORGANIZATION = (By.ID, "formLevel_organization")
    # Проверка организационного уровня
    LOCATOR_CHECK_ORGANIZATION = (By.XPATH, """//label[@class = "label__color_gray" and text () = "Организация"]""")
    # Москва из выпадающего списка регионов
    LOCATOR_MSK_BTN = (By.XPATH, """//nz-option-item[@title="г. Москва"]""")
    # Район "Восточный" - Москва
    LOCATOR_VOSTOK_BTN = (By. XPATH, "//nz-option-item[@ng-reflect-title='Восточный']")
    # Выбор статуса "Утверждён"
    LOCATOR_APPROVED_BTN = (By.XPATH, """//nz-option-item[@ng-reflect-value = 'es_signed']""")
    # Выпадающий календарь: "Года"
    LOCATOR_YEAR_BTN = (By.XPATH, """//label[@ng-reflect-nz-value = 'Года']""")
    # Выпадающий календарь: "Месяца"
    LOCATOR_MONTH_BTN = (By.XPATH, """//label[@ng-reflect-nz-value = 'Месяца']""")
    # Выпадающий календарь: "Дени"
    LOCATOR_DAY_BTN = (By.XPATH, """//label[@ng-reflect-nz-value = 'Дни']""")
    # Поле "Период" - начальная дата
    LOCATOR_START_DATE_FIELD = (By.XPATH, """//input[@placeholder = 'Начальная дата']""")
    # Поле "Период" - конечная дата
    LOCATOR_END_DATE_FIELD = (By.XPATH, """//input[@placeholder = 'Конечная дата']""")
    # Поле "Период" - начальный месяц
    LOCATOR_START_MONTH_FIELD = (By.XPATH, """//input[@placeholder = 'Начальный месяц']""")
    # Поле "Период" - конечный месяц
    LOCATOR_END_MONTH_FIELD = (By.XPATH, """//input[@placeholder = 'Конечный месяц']""")
    # Поле "Период" - начальный год
    LOCATOR_START_YEAR_FIELD = (By.XPATH, """//input[@placeholder = 'Начальный год']""")
    # Поле "Период" - конечный год
    LOCATOR_END_YEAR_FIELD = (By.XPATH, """//input[@placeholder = 'Год окончания']""")
    # Проверка сортировки по состоянию
    LOCATOR_SORT_CHECK_FIELD = (By.XPATH, """(//a[@class = "invisible_link" and contains(text(), "Утвержден")])[1]""")
    # Проверка сортировки по периоду
    LOCATOR_PERIOD_CHECK_FIELD = (By.XPATH, """(//a[@class = "invisible_link" and contains(text(), "2054")])[1]""")
