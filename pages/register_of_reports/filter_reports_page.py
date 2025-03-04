from base.BaseApp import BasePage
from selenium.webdriver.common.by import By
import allure


class ReportRegistersLocators:
    LOCATOR_LOGIN_FIELD = (By.ID, "login")
    LOCATOR_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_LOGIN_BTN = (By.ID, "submit-button")
    # Проверка входа
    LOCATOR_MENU_FIELD = (By.XPATH, """//div[@class="heading"]/child::h2""")
    # Кнопка входа в СТАТ
    LOCATOR_ICON_STAT = (By.XPATH, """//div[@class="card"]/child::*[1]""")
    # Мониторинг здоровья
    locator_health_monitoring = (By.XPATH, """//a[@data-testid="menu_stat_health_monitoring"]""")
    # Форма №1 //*[contains(text(), " Форма № 1 ")]
    LOCATOR_FORM_1 = (By.XPATH, """//a[label[contains(text(), " Форма № 1 ")]]""")
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
    # Проверка уровня район-города
    LOCATOR_CHECK_DISTRICT_CITY = (By.XPATH, """//span[@class = "ant-table-column-title" and contains(text(), " Район города ")]""")
    # Проверка районного уровня
    LOCATOR_CHECK_DISTRICT = (By.XPATH, """//span[@class = "ant-table-column-title" and contains(text(), "Район")]""")
    # Проверка регионального уровня
    LOCATOR_CHECK_REGION = (By.XPATH, """//span[@class = "ant-table-column-title" and contains(text(), "Регион")]""")
    # Поле "регион" в реестре отчетов
    LOCATOR_REGIONAL_FIELD = (By.XPATH, """//nz-select[@ng-reflect-compare-with="(o1, o2) => o1 && o2 ? o1['reg"]""")
    # Выпадающий список регионов
    LOCATOR_DROPDOWN_REGIONAL = (By.XPATH, """//*[@id="cdk-overlay-0"]/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]""")
    # Москва из выпадающего списка регионов
    LOCATOR_MSK_BTN = (By.XPATH, """//nz-option-item[@title="г. Москва"]""")
    # Поле "Район" в реестре отчетов
    LOCATOR_DISTRICT_FIELD = (By.XPATH, """//nz-select[@ng-reflect-compare-with="(o1, o2) => o1 && o2 ? o1['okt"]""")
    # Поле "Район-города" в реестре отчетов
    LOCATOR_DISTRICT_CITY_FIELD = (By.XPATH, """//nz-select[@ng-reflect-compare-with="(o1, o2) => o1 && o2 ? o1['oka"]""")
    # Поле "Организация" организационный уровень
    LOCATOR_ORGANIZATION_FIELD = (By.XPATH,
            """//nz-select[@ng-reflect-compare-with="(o1, o2) => o1 && o2 ? o1['gui"]""")
    # Поле для ввода организации
    LOCATOR_ORG_NAME = (By.XPATH, """(//nz-select//input[contains(@class, 'ant-select-selection-search-input')])[3]""")
    # Организация "Альбион"
    LOCATOR_ORG_ALBION = (By.XPATH,
            """//nz-option-item[contains(@title, 'ООО "АЛЬБИОН" (119021, МОСКВА')]""")
    # Выбор района города "муниципальный округ Вешняки"
    LOCATOR_DISTRICT_CITY_VESHNYAKI = (By.XPATH,
            """//nz-option-item[contains(@title, 'муниципальный округ Вешняки')]""")
    # Район "Восточный" - Москва
    LOCATOR_VOSTOK_BTN = (By. XPATH, "//nz-option-item[@ng-reflect-title='Восточный']")
    # Проверка сортировки по организации "Альбион"
    LOCATOR_ORG_ALBION_FIELD = (By.XPATH, """(//a[contains(text(), 'ООО "АЛЬБИОН"')])[1]""")
    # Проверка сортировки по району-города
    LOCATOR_CHECK_DISTRICT_CITY_FIELD = (By.XPATH, """(//a[@class = "invisible_link" and contains(text(), "Вешняки")])[1]""")
    # Проверка сортировки по району
    LOCATOR_CHECK_DISTRICT_FIELD = (By.XPATH, """(//a[@class = "invisible_link" and contains(text(), "Восточный")])[1]""")
    # Проверка сортировки по региону
    LOCATOR_CHECK_REGION_FIELD = (By.XPATH, """(//a[@class = "invisible_link" and contains(text(), "г. Москва")])[1]""")
    # Кнопка сброса всех фильтров в реестре отчетов
    LOCATOR_RESET_FILTERS_BTN = (By.XPATH, """//i[@ng-reflect-tooltip-content="Сбросить фильтры"]""")
    # Поле "Состояние" в реестре отчетов
    LOCATOR_STATUS_FIELD = (By.XPATH, """//nz-select-item[@title = 'Все']""")
    # Выбор статуса "Утверждён"
    LOCATOR_APPROVED_BTN = (By.XPATH, """//nz-option-item[@ng-reflect-value = 'es_signed']""")
    # Поле "Периодичность" в реестре отчетов
    LOCATOR_PERIODICITY_FIELD = (By.XPATH, """//nz-select[@ng-reflect-is-disabled = 'false']""")
    # Выбор периодичности "Ежемесячная"
    LOCATOR_MONTHLY_BTN = (By.XPATH, """//nz-option-item[@ng-reflect-value = 'monthly']""")
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


class OperationsHelper(BasePage):

    # Ввод текста
    @allure.step('Ввод логина: {word}')
    def enter_login(self, word):
        self.enter_text_into_field(ReportRegistersLocators.LOCATOR_LOGIN_FIELD, word, description="Поле 'Логин'")

    @allure.step('Ввод пароля: {word}')
    def enter_password(self, word):
        self.enter_text_into_field(ReportRegistersLocators.LOCATOR_PASSWORD_FIELD, word, description="Поле 'Пароль'")

    @allure.step('Ввод названия организации: {word}')
    def enter_org_name(self, word):
        self.enter_text_into_field(ReportRegistersLocators.LOCATOR_ORG_NAME, word,
                                   description="Название организации")

    @allure.step("Ввод начального года: {word}")
    def enter_starting_year_calendar(self, word):
        self.enter_text_into_field(ReportRegistersLocators.LOCATOR_START_YEAR_FIELD, word, description="Поле 'Начальный год'", press_enter=True)

    @allure.step("Ввод конечного года: {word}")
    def enter_end_year_calendar(self, word):
        self.enter_text_into_field(ReportRegistersLocators.LOCATOR_END_YEAR_FIELD, word, description="Поле 'Конечный год'", press_enter=True)

    # Клик на кнопку
    @allure.step("Клик на кнопку 'Войти'")
    def click_login_button(self):
        self.click_button(ReportRegistersLocators.LOCATOR_LOGIN_BTN, description="Кнопка 'Войти'")

    @allure.step("Клик на иконку 'СТАТ отчетность'")
    def click_icon_stat(self):
        self.click_button(ReportRegistersLocators.LOCATOR_ICON_STAT, description="Иконка 'СТАТ отчетность'")

    @allure.step("Клик на раздел 'Мониторинг здоровья'")
    def click_health_monitoring(self):
        self.click_button(ReportRegistersLocators.locator_health_monitoring, description="Раздел 'Мониторинг здоровья'")

    @allure.step("Клик на 'Форма №1'")
    def click_form_1(self):
        self.click_button(ReportRegistersLocators.LOCATOR_FORM_1, description="Кнопка 'Форма №1'")

    @allure.step("Клик на выпадающий список уровней видимости")
    def click_level(self):
        self.click_button(ReportRegistersLocators.LOCATOR_LEVEL, description="Выпадающий список уровней видимости")

    @allure.step("Выбор уровня видимости: 'Организация'")
    def click_level_organization(self):
        self.click_button(ReportRegistersLocators.LOCATOR_LEVEL_ORGANIZATION,
                          description="Выбор уровня 'Организация'")

    @allure.step("Выбор уровня видимости: 'Район-города'")
    def click_level_district_city(self):
        self.click_button(ReportRegistersLocators.LOCATOR_LEVEL_DISTRICT_CITY,
                          description="Выбор уровня 'Район-города'")

    @allure.step("Выбор уровня видимости: 'Районный'")
    def click_level_district(self):
        self.click_button(ReportRegistersLocators.LOCATOR_LEVEL_DISTRICT,
                          description="Выбор уровня 'Районный'")

    @allure.step("Выбор уровня видимости: 'Региональный'")
    def click_level_region(self):
        self.click_button(ReportRegistersLocators.LOCATOR_LEVEL_REGIONAL,
                          description="Выбор уровня 'Региональный'")

    @allure.step("Клик на поле 'Регион' в реестре отчетов")
    def click_region_field(self):
        self.click_button(ReportRegistersLocators.LOCATOR_REGIONAL_FIELD, description="Регион (выпадающий список)")

    @allure.step("Выбираем регион из выпадающего списка: 'Москва'")
    def click_msk_btn(self):
        self.click_button(ReportRegistersLocators.LOCATOR_MSK_BTN, description="Москва из выпадающего списка")

    @allure.step("Клик на поле 'Район' в реестре отчетов")
    def click_district_field(self):
        self.click_button(ReportRegistersLocators.LOCATOR_DISTRICT_FIELD, description="Район (выпадающий список)")

    @allure.step("Выбираем район из выпадающего списка: 'Восточный'")
    def click_vostok_btn(self):
        self.click_button(ReportRegistersLocators.LOCATOR_VOSTOK_BTN, description="Восточный район Москва")

    @allure.step("Клик на поле 'Организация' в реестре отчетов")
    def click_organization_field(self):
        self.click_button(ReportRegistersLocators.LOCATOR_ORGANIZATION_FIELD, description="Выпадающий список организаций")

    @allure.step("Клик на поле 'Район-города' в реестре отчетов")
    def click_district_city_field(self):
        self.click_button(ReportRegistersLocators.LOCATOR_DISTRICT_CITY_FIELD, description="Выпадающий список район-города")

    @allure.step("Выбираем организацию из выпадающего списка: 'Альбион'")
    def click_albion_btn(self):
        self.click_button(ReportRegistersLocators.LOCATOR_ORG_ALBION, description="Организация 'Альбион")

    @allure.step("Выбираем район-города из выпадающего списка: 'муниципальный округ Вешняки'")
    def click_veshnyaki_btn(self):
        self.click_button(ReportRegistersLocators.LOCATOR_DISTRICT_CITY_VESHNYAKI, description="Район-города 'муниципальный округ Вешняки'")

    @allure.step("Клик на поле 'Состояние' в реестре отчетов")
    def click_status_btn(self):
        self.click_button(ReportRegistersLocators.LOCATOR_STATUS_FIELD, description='Поле "Состояние" в реестре отчетов')

    @allure.step("Выбираем состояние из выпадающего списка: 'Утверждён'")
    def click_approved_btn(self):
        self.click_button(ReportRegistersLocators.LOCATOR_APPROVED_BTN, description="Статус 'Утверждён'")

    @allure.step("Клик на поле 'Периодичность' в реестре отчетов")
    def click_periodicity_btn(self):
        self.click_button(ReportRegistersLocators.LOCATOR_PERIODICITY_FIELD, description='Поле "Периодичность" в реестре отчетов')

    @allure.step("Выбираем периодичность из выпадающего списка: 'Ежемесячная'")
    def click_monthly_btn(self):
        self.click_button(ReportRegistersLocators.LOCATOR_MONTHLY_BTN, description="Периодичность 'Ежемесячная'")

    @allure.step("Клик на поле 'Период' в реестре отчетов - дата")
    def click_period_data_btn(self):
        self.click_button(ReportRegistersLocators.LOCATOR_START_DATE_FIELD, description='Поле "Период" в реестре отчетов')

    @allure.step("Клик на поле 'Период' в реестре отчетов - год")
    def click_period_year_btn(self):
        self.click_button(ReportRegistersLocators.LOCATOR_START_YEAR_FIELD, description='Поле "Период" в реестре отчетов-год')

    @allure.step("Выбираем фильтрацию в календаре: 'Год'")
    def click_year_calendar_btn(self):
        self.click_button(ReportRegistersLocators.LOCATOR_YEAR_BTN, description='Календарь фильтр "Год"')

    @allure.step("Клик на кнопку 'Сбросить фильтры'")
    def click_reset_filters_btn(self):
        self.click_button(ReportRegistersLocators.LOCATOR_RESET_FILTERS_BTN, description="Кнопка 'Сбросить фильтры'")

    # Получение текста
    @allure.step("Проверяем успешную авторизацию пользователя")
    def get_menu_text(self):
        return self.get_text_from_element(ReportRegistersLocators.LOCATOR_MENU_FIELD, description="Текст меню после авторизации")

    @allure.step("Проверяем успешный переход на уровень 'Организация'")
    def get_check_organization_lvl(self):
        return self.get_text_from_element(ReportRegistersLocators.LOCATOR_CHECK_ORGANIZATION,
                                          description="Подтверждение уровня 'Организация'")

    @allure.step("Проверяем успешный переход на уровень 'Район-города'")
    def get_check_district_city_lvl(self):
        return self.get_text_from_element(ReportRegistersLocators.LOCATOR_CHECK_DISTRICT_CITY,
                                          description="Подтверждение уровня 'Район-города'")

    @allure.step("Проверяем успешный переход на уровень 'Районный'")
    def get_check_district_lvl(self):
        return self.get_text_from_element(ReportRegistersLocators.LOCATOR_CHECK_DISTRICT,
                                          description="Подтверждение уровня 'Районный'")

    @allure.step("Проверяем успешный переход на уровень 'Региональный'")
    def get_check_region_lvl(self):
        return self.get_text_from_element(ReportRegistersLocators.LOCATOR_CHECK_REGION,
                                          description="Подтверждение уровня 'Региональный'")

    @allure.step("Проверяем успешную фильтрацию по организации: 'Альбион'")
    def get_check_organization_albion(self):
        return self.get_text_from_element(ReportRegistersLocators.LOCATOR_ORG_ALBION_FIELD,
                                          description="Успешная проверка фильтрации организаций")

    @allure.step("Проверяем успешную фильтрацию по району-города")
    def get_check_district_city_veshnyaki(self):
        return self.get_text_from_element(ReportRegistersLocators.LOCATOR_DISTRICT_CITY_VESHNYAKI,
                                          description="Успешная проверка фильтрации района-города")

    @allure.step("Проверяем успешную фильтрацию по району")
    def get_check_filter_district(self):
        return self.get_text_from_element(ReportRegistersLocators.LOCATOR_CHECK_DISTRICT_FIELD,
                                          description="Успешная проверка фильтрации по району")

    @allure.step("Проверяем успешную фильтрацию по региону")
    def get_check_filter_region(self):
        return self.get_text_from_element(ReportRegistersLocators.LOCATOR_CHECK_REGION_FIELD,
                                          description="Успешная проверка фильтрации по региону")

    @allure.step("Проверка, что выбраны все регионы")
    def get_check_all_reg(self):
        return self.get_text_from_element(ReportRegistersLocators.LOCATOR_REGIONAL_FIELD, description="Выбраны все регионы")

    @allure.step("Проверяем успешную фильтрацию по состоянию")
    def get_check_sort_status(self):
        return self.get_text_from_element(ReportRegistersLocators.LOCATOR_SORT_CHECK_FIELD,
                                          description="Успешная проверка фильтрации по состоянию")

    @allure.step("Проверяем успешную фильтрацию по периоду")
    def get_check_sort_period(self):
        return self.get_text_from_element(ReportRegistersLocators.LOCATOR_PERIOD_CHECK_FIELD,
                                          description="Успешная проверка фильтрации по периоду")

    # Выпадающие списки

    def select_dropdown_regional(self, text):
        return self.select_from_dropdown(ReportRegistersLocators.LOCATOR_DROPDOWN_REGIONAL, text,
                                         description="Region dropdown list")









