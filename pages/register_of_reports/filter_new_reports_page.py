import allure
from base.BaseApp import BasePage
from selenium.webdriver.common.by import By
from pages.register_of_reports.common_locators_page import RegistersCommonLocators


class NewRegisterReportsLocators:
    # Раздел "Отчёты организаций Роспотребнадзора"
    LOCATOR_STAT_REPORTS_AGGREGATION = (By.XPATH, """//a[@data-testid = "menu_stat_reports_aggregation"]""")
    # Форма №12-23
    LOCATOR_FORM_12_23 = (By.XPATH, """//a[label[contains(text(), "Форма № 12-23")]]""")
    # Проверка уровня район-города
    LOCATOR_NEW_CHECK_DISTRICT_CITY = (By.XPATH, """//th[@ng-reflect-nz-column-key = "district_city"]""")
    # Проверка районного уровня
    LOCATOR_NEW_CHECK_DISTRICT = (By.XPATH, """//th[@ng-reflect-nz-column-key = "district"]""")
    # Проверка регионального уровня
    LOCATOR_NEW_CHECK_REGION = (By.XPATH, """//th[@ng-reflect-nz-column-key = "region"]""")
    # Поле "Территория" в реестре отчетов
    LOCATOR_NEW_TERRITORY_FIELD = (By.XPATH, """(//nz-select//input[contains(@class, "ant-select-selection-search-input")])[1]""")
    # Поле "Регион" в реестре отчетов
    LOCATOR_NEW_REGIONAL_FIELD = (By.XPATH, """(//nz-select//input[contains(@class, "ant-select-selection-search-input")])[2]""")
    # Поле "Район" в реестре отчетов
    LOCATOR_NEW_DISTRICT_FIELD = (By.XPATH, """(//nz-select//input[contains(@class, "ant-select-selection-search-input")])[3]""")
    # Поле "Район-города" в реестре отчетов
    LOCATOR_NEW_DISTRICT_CITY_FIELD = (By.XPATH, """(//nz-select//input[contains(@class, "ant-select-selection-search-input")])[4]""")
    # Поле "Организация" организационный уровень (одинаковый с районом)
    LOCATOR_NEW_ORGANIZATION_FIELD = (By.XPATH, """(//nz-select//input[contains(@class, "ant-select-selection-search-input")])[3]""")
    # Поле "Состояние" в реестре отчетов
    LOCATOR_NEW_STATUS_FIELD = (By.XPATH, """//label[contains(text(), "Состояние")]/following-sibling::*""")
    # Поле "Периодичность" в реестре отчетов
    LOCATOR_NEW_PERIODICITY_FIELD = (By.XPATH, """//label[contains(text(), "Периодичность")]/following-sibling::*""")
    # Выбор периодичности "Квартальная"
    LOCATOR_QUARTERLY_BTN = (By.XPATH, """//nz-option-item[@ng-reflect-value = "quarterly"]""")
    # "РФ" из выпадающего списка
    LOCATOR_RF_BTN = (By.XPATH, """//nz-option-item[@title="РФ"]""")
    # Очистка поля "Период" через крестик
    LOCATOR_NEW_CLEAR_PERIOD = (By.XPATH, """//*[local-name()="svg" and @data-icon="close-circle"]//*[local-name()="path"]""")


class RegisterNewOperationsHelper(BasePage):

    # Ввод текста
    @allure.step("Ввод начального года: {word}")
    def enter_starting_year_calendar(self, word):
        self.enter_text_into_field(RegistersCommonLocators.LOCATOR_START_YEAR_FIELD, word, description="Поле 'Начальный год'", press_enter=True)

    @allure.step("Ввод конечного года: {word}")
    def enter_end_year_calendar(self, word):
        self.enter_text_into_field(RegistersCommonLocators.LOCATOR_END_YEAR_FIELD, word, description="Поле 'Конечный год'", press_enter=True)

    # Клик на кнопку
    @allure.step("Клик на иконку 'СТАТ отчетность'")
    def click_icon_stat(self):
        self.click_button(RegistersCommonLocators.LOCATOR_ICON_STAT, description="Иконка 'СТАТ отчетность'")

    @allure.step("Клик на раздел 'Отчёты организаций Роспотребнадзора'")
    def click_reports_rospotrebnadzor_organizations(self):
        self.click_button(NewRegisterReportsLocators.LOCATOR_STAT_REPORTS_AGGREGATION, description="Раздел 'Отчёты организаций Роспотребнадзора'")

    @allure.step("Клик на 'Форма №12-23'")
    def click_form_12_23(self):
        self.click_button(NewRegisterReportsLocators.LOCATOR_FORM_12_23, description="Кнопка 'Форма №12-23'")

    @allure.step("Клик на выпадающий список уровней видимости")
    def click_level(self):
        self.click_button(RegistersCommonLocators.LOCATOR_LEVEL, description="Выпадающий список уровней видимости")

    @allure.step("Выбор уровня видимости: 'Районный'")
    def click_level_district(self):
        self.click_button(RegistersCommonLocators.LOCATOR_LEVEL_DISTRICT, description="Выбор уровня 'Районный'")

    @allure.step("Клик на поле 'Территория' в реестре отчетов")
    def click_territory_field(self):
        self.click_button(NewRegisterReportsLocators.LOCATOR_NEW_TERRITORY_FIELD, description="Территория (выпадающий список)")

    @allure.step("Выбираем территорию из выпадающего списка: 'РФ'")
    def click_rf_btn(self):
        self.click_button(NewRegisterReportsLocators.LOCATOR_RF_BTN, description="РФ из выпадающего списка")

    @allure.step("Клик на поле 'Регион' в реестре отчетов")
    def click_new_region_field(self):
        self.click_button(NewRegisterReportsLocators.LOCATOR_NEW_REGIONAL_FIELD, description="Регион (выпадающий список)")

    @allure.step("Выбираем регион из выпадающего списка: 'Москва'")
    def click_msk_btn(self):
        self.click_button(RegistersCommonLocators.LOCATOR_MSK_BTN, description="Москва из выпадающего списка")

    @allure.step("Клик на поле 'Район' в реестре отчетов")
    def click_new_district_field(self):
        self.click_button(NewRegisterReportsLocators.LOCATOR_NEW_DISTRICT_FIELD, description="Район (выпадающий список)")

    @allure.step("Выбираем район из выпадающего списка: 'Восточный'")
    def click_vostok_btn(self):
        self.click_button(RegistersCommonLocators.LOCATOR_VOSTOK_BTN, description="Восточный район Москва")

    @allure.step("Клик на поле 'Состояние' в реестре отчетов")
    def click_new_status_btn(self):
        self.click_button(NewRegisterReportsLocators.LOCATOR_NEW_STATUS_FIELD, description='Поле "Состояние" в реестре отчетов')

    @allure.step("Выбираем состояние из выпадающего списка: 'Утверждён'")
    def click_approved_btn(self):
        self.click_button(RegistersCommonLocators.LOCATOR_APPROVED_BTN, description="Статус 'Утверждён'")

    @allure.step("Клик на поле 'Периодичность' в реестре отчетов")
    def click_new_periodicity_btn(self):
        self.click_button(NewRegisterReportsLocators.LOCATOR_NEW_PERIODICITY_FIELD, description='Поле "Периодичность" в реестре отчетов')

    @allure.step("Выбираем периодичность из выпадающего списка: 'Квартальная'")
    def click_quarterly_btn(self):
        self.click_button(RegistersCommonLocators.LOCATOR_QUARTERLY_BTN, description="Периодичность 'Квартальная'")

    @allure.step("Клик на поле 'Период' в реестре отчетов - дата")
    def click_period_data_btn(self):
        self.click_button(RegistersCommonLocators.LOCATOR_START_DATE_FIELD, description='Поле "Период" в реестре отчетов')

    @allure.step("Клик на поле 'Период' в реестре отчетов - год")
    def click_period_year_btn(self):
        self.click_button(RegistersCommonLocators.LOCATOR_START_DATE_FIELD, description='Поле "Период" в реестре отчетов-год')

    @allure.step("Выбираем фильтрацию в календаре: 'Год'")
    def click_year_calendar_btn(self):
        self.click_button(RegistersCommonLocators.LOCATOR_YEAR_BTN, description='Календарь фильтр "Год"')

    @allure.step("Нажимаем крестик для очистки периода")
    def click_clear_period(self):
        self.click_button(NewRegisterReportsLocators.LOCATOR_NEW_CLEAR_PERIOD, description='Крестик для очистки периода')

    @allure.step("Выбор уровня видимости: 'Региональный'")
    def click_level_region(self):
        self.click_button(RegistersCommonLocators.LOCATOR_LEVEL_REGIONAL,
                          description="Выбор уровня 'Региональный'")

    @allure.step("Проверяем успешный переход на уровень 'Региональный'")
    def get_new_check_region_lvl(self):
        return self.get_text_from_element(NewRegisterReportsLocators.LOCATOR_NEW_CHECK_REGION,
                                          description="Подтверждение уровня 'Региональный'")

    @allure.step("Проверяем успешную фильтрацию по региону")
    def get_check_filter_region(self):
        return self.get_text_from_element(RegistersCommonLocators.LOCATOR_CHECK_REGION_FIELD,
                                          description="Успешная проверка фильтрации по региону")

    @allure.step("Выбор уровня видимости: 'Федеральный'")
    def click_level_federal(self):
        self.click_button(RegistersCommonLocators.LOCATOR_LEVEL_CONSOLIDATED,
                          description="Выбор уровня 'Федеральный'")

    # Получение текста
    @allure.step("Проверяем успешную авторизацию пользователя")
    def get_menu_text(self):
        return self.get_text_from_element(RegistersCommonLocators.LOCATOR_MENU_FIELD, description="Текст меню после авторизации")
    
    @allure.step("Проверяем успешный переход на уровень 'Районный'")
    def get_check_district_lvl(self):
        return self.get_text_from_element(NewRegisterReportsLocators.LOCATOR_NEW_CHECK_DISTRICT, description="Подтверждение уровня 'Районный'")

    @allure.step("Проверяем успешную фильтрацию по району")
    def get_check_filter_district(self):
        return self.get_text_from_element(RegistersCommonLocators.LOCATOR_CHECK_DISTRICT_FIELD, description="Успешная проверка фильтрации по району")

    @allure.step("Проверяем успешную фильтрацию по состоянию")
    def get_check_sort_status(self):
        return self.get_text_from_element(RegistersCommonLocators.LOCATOR_SORT_CHECK_FIELD,
                                          description="Успешная проверка фильтрации по состоянию")

    @allure.step("Проверяем успешную фильтрацию по периоду")
    def get_check_sort_period(self):
        return self.get_text_from_element(RegistersCommonLocators.LOCATOR_PERIOD_CHECK_FIELD,
                                          description="Успешная проверка фильтрации по периоду")

    # Навести курсор на элемент и нажать
    @allure.step("Наводим на поле 'Год окончания' и нажимаем на крестик очистки")
    def hover_end_year_and_click_clear(self):
        return self.hover_and_click(
            RegistersCommonLocators.LOCATOR_END_YEAR_FIELD,
            NewRegisterReportsLocators.LOCATOR_NEW_CLEAR_PERIOD,
            description="Наведение на поле 'Год окончания' и клик на крестик"
        )


