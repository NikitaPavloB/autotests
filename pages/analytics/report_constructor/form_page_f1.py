from base.BaseApp import BasePage
from selenium.webdriver.common.by import By
import allure

from pages.analytics.mock import table_mock_form1
from pages.analytics.mock.table_mock_form1 import table_mock


class TestForm1Locators:
    LOCATOR_LOGIN_FIELD = (By.ID, "login")
    LOCATOR_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_LOGIN_BTN = (By.ID, "submit-button")
    # Проверка входа
    LOCATOR_MENU_FIELD = (By.XPATH, """//div[@class="heading"]/child::h2""")
    # Кнопка входа в СТАТ
    LOCATOR_ICON_STAT = (By.XPATH, """//div[@class="card"]/child::*[1]""")
    # Раздел Конструктор отчетов
    LOCATOR_ICON_ANALYTICS_CONSTRUCT = (By.XPATH, """(//a[@ng-reflect-tooltip-content="Конструктор отчётов"])""")
    # ОБЩИЕ СВЕДЕНИЯ
    # ПОЛЕ ШАБЛОН ЗАПРОСА
    LOCATOR_TEMPLATE_REQUEST = (By.XPATH, """(//label[contains(text(), "Шаблон запроса")]/following-sibling::*)""")
    # ТЕСТОВЫЙ ШАБЛОН
    LOCATOR_TEST_TEMPLATE = (By.XPATH, """(//nz-option-item[@ng-reflect-label='Форма1_Ежемесячная для тестиро'])""")
    # Поле Форма
    # LOCATOR_FORM = (By.XPATH, """(//nz-select-search//input[contains(@class,"ant-select-selection-search-input")])[1]""")
    # LOCATOR_FORM = (By.XPATH, "//[label[contains(text(), 'Форма')]]//following-sibling::input[contains(@class,'ant-select-selection-search-input')]")
    # LOCATOR_FORM = (By.XPATH, "//nz-form-item/nz-form-control/div/div/div/nz-select/nz-select-top-control/nz-select-search/input")
    LOCATOR_FORM = (By.XPATH, """(//nz-select[@ng-reflect-compare-with = "(o1, o2) => o1 && o2 ? o1['gui"]) [1]""")
    # ВЫБОР ФОРМЫ ИЗ СПИСКА
    LOCATOR_FORM1 = (By.XPATH, """(//nz-option-item[@ng-reflect-label='Форма 1 «Сведения об инфекцион'])[1]""")
    # Поле Периодичность
    LOCATOR_PERIODICITY = (By.XPATH, "//nz-select-item[@ng-reflect-label='Ежемесячная']")
    # Поле Вкладка
    LOCATOR_TAB = (By.XPATH, "//nz-select-item[@ng-reflect-label='Форма №1']")
    # НАБОР СТРОК
    # Кнопка добавления новой строки
    LOCATOR_BUTTON_NEW_ROW = (By.XPATH, "//i[@data-testid='icon_add']")
    # Новые строки
    LOCATOR_BUTTON_NEW_ROW1 = (
        By.XPATH, """(//label[contains(text(), "Атрибут который попадет в строки")]/following-sibling::*)[1]""")
    LOCATOR_BUTTON_NEW_ROW2 = (
        By.XPATH, """(//label[contains(text(), "Атрибут который попадет в строки")]/following-sibling::*)[2]""")
    # Добавление атрибута Территории
    LOCATOR_TERRITORY = (By.XPATH, "//nz-option-item[@ng-reflect-title='Все территории РФ']")
    # Добавление атрибута Зарегистрировано заболеваний...
    LOCATOR_REGISTERED_Diseases = (By.XPATH, "//nz-option-item[@ng-reflect-title='Зарегистрировано заболеваний в']")
    # НАБОР СТОЛБЦОВ
    # Кнопка добавления нового столбца
    LOCATOR_BUTTON_NEW_COLUMN = (By.XPATH, "(//i[@data-testid='icon_add'])[2]")
    # Новые столбцы
    LOCATOR_NEW_COLUMN = (
        By.XPATH, """(//label[contains(text(), "Атрибут который попадет в столбцы")]/following-sibling::*)[1]""")
    LOCATOR_NEW_COLUMN1 = (By.XPATH, """(//label[contains(text(), "Значение")]/following-sibling::*)[3]""")
    LOCATOR_NEW_COLUMN2 = (
        By.XPATH, """(//label[contains(text(), "Атрибут который попадет в столбцы")]/following-sibling::*)[2]""")
    LOCATOR_NEW_COLUMN3 = (By.XPATH, """(//label[contains(text(), "Значение")]/following-sibling::*)[4]""")

    # Добавление атрибута Год(а)
    LOCATOR_YEAR = (By.XPATH, "//nz-option-item[@ng-reflect-title='Год']")
    # Добавление значений для атрибута Год(а)
    LOCATOR_YEAR_2022 = (By.XPATH, "//nz-option-item[@ng-reflect-title='2022']")
    LOCATOR_YEAR_2023 = (By.XPATH, "//nz-option-item[@ng-reflect-title='2023']")
    LOCATOR_YEAR_2024 = (By.XPATH, "//nz-option-item[@ng-reflect-title='2024']")
    # Добавление атрибута Месяц
    LOCATOR_MONTH = (By.XPATH, "//nz-option-item[@ng-reflect-title='Месяц']")
    # Добавление значений для атрибута Месяц
    LOCATOR_MONTH_JANUARY = (By.XPATH, "//nz-option-item[@ng-reflect-title='Январь']")
    LOCATOR_MONTH_FEBRUARY = (By.XPATH, "//nz-option-item[@ng-reflect-title='Февраль']")
    LOCATOR_MONTH_MARCH = (By.XPATH, "//nz-option-item[@ng-reflect-title='Март']")
    # НАБОР УСЛОВИЙ ВЫБОРКИ
    # Новое условие
    LOCATOR_BUTTON_NEW_CONDITION = (By.XPATH, "(//i[@data-testid='icon_add'])[3]")
    LOCATOR_NEW_CONDITION = (
        By.XPATH,
        """(//label[contains(text(), "Атрибут который попадет в условия выборки")]/following-sibling::*)[1]""")
    LOCATOR_NEW_CONDITION1 = (By.XPATH, """(//label[contains(text(), "Значение")]/following-sibling::*)[5]""")
    LOCATOR_NEW_CONDITION2 = (
        By.XPATH,
        """(//label[contains(text(), "Атрибут который попадет в условия выборки")]/following-sibling::*)[2]""")
    LOCATOR_NEW_CONDITION3 = (By.XPATH, """(//label[contains(text(), "Значение")]/following-sibling::*)[6]""")
    # Добавление атрибута Группы заболеваний
    LOCATOR_GROUP_OF_DISEASES = (By.XPATH, "//nz-option-item[@ng-reflect-title='Группы заболеваний для Формы 1']")
    # Добавление значений Нозологии
    LOCATOR_DIAGNOSIS = (By.XPATH, "//nz-option-item[@ng-reflect-title='Острые инфекции верхних дыхате']")
    # Добавление атрибута Возрастные группы
    LOCATOR_AGE_GROUPS = (By.XPATH, "//nz-option-item[@ng-reflect-title='Возрастные группы']")
    # Добавление значения Все возраста
    LOCATOR_ALL_AGE = (By.XPATH, "//nz-option-item[@ng-reflect-title='Все возраста']")
    # Кнопка формирования отчета
    LOCATOR_GENERATE_A_REPORT = (By.XPATH, "(//button[@data-testid='button_create'])[2]")
    # Таблица отчета
    LOCATOR_REPORT_TABLE = (By.CLASS_NAME, "ant-table")
    # НАСТРОЙКИ ОТОБРАЖЕНИЯ
    LOCATOR_CHECKBOX_AVERAGE_10_YEARS = (By.XPATH, """//span[contains(text(), "Среднемноголетний показатель (СМП) за 10 лет ")]""")

class UserTemplates:
    # Кнопка создания пользовательского шаблона
    LOCATOR_BUTTON_NEW_TEMPLATE = (By.XPATH, "(//button[@data-testid='button_create'])[1]")
    # Поле Имя шаблона
    LOCATOR_TEMPLATE_NAME = (By.XPATH, "//input[@ng-reflect-model='Форма_Ежемесячная']")
    # Кнопка сохранения шаблона
    LOCATOR_SAVE_TEMPLATE = (By.XPATH, "(//button[@data-testid='button_create'])[3]")
    # Удаление пользовательского шаблона
    LOCATOR_DELETE_TEMPLATE = (By.XPATH, "(//button[@data-testid='button_delete'])[1]")
    # Подтверждение удаления Пользовательского шаблона
    LOCATOR_POPUP_DELETE_TEMPLATE = (By.XPATH, "(//button[@ng-reflect-nz-type='primary'])[10]")


class OperationsHelper(BasePage):
    @allure.step('Ввод логина: {word}')
    def enter_login(self, word):
        self.enter_text_into_field(TestForm1Locators.LOCATOR_LOGIN_FIELD, word, description="Логин")

    @allure.step('Ввод пароля: {word}')
    def enter_password(self, word):
        self.enter_text_into_field(TestForm1Locators.LOCATOR_PASSWORD_FIELD, word, description="Пароль")

    @allure.step("Клик на кнопку 'Войти'")
    def click_login_button(self):
        self.click_button(TestForm1Locators.LOCATOR_LOGIN_BTN, description="Кнопка войти")

    @allure.step("Проверяем успешную авторизацию пользователя")
    def get_menu_text(self):
        return self.get_text_from_element(TestForm1Locators.LOCATOR_MENU_FIELD, description="Check menu field")

    @allure.step("Клик на иконку 'СТАТ отчетность'")
    def click_icon_stat(self):
        self.click_button(TestForm1Locators.LOCATOR_ICON_STAT, description="Иконка стат отчетность")

    @allure.step("Клик на иконку 'Конструктор отчетов'")
    def click_icon_constructor(self):
        self.click_button(TestForm1Locators.LOCATOR_ICON_ANALYTICS_CONSTRUCT, description="Иконка конструктор отчетов")

    @allure.step("Клик на поле Форма")
    def click_form_field(self):
        self.click_button(TestForm1Locators.LOCATOR_FORM, description="Форма")

    @allure.step('Поиск формы в выпадающем списке: {word}')
    def enter_form_name(self, word):
        self.enter_text_into_field(TestForm1Locators.LOCATOR_FORM, word)
        self.click_button(TestForm1Locators.LOCATOR_FORM1, description="Форма 1")

    @allure.step('Автозаполнение поля Периодичность')
    def select_periodicity(self):
        return self.get_text_from_element(TestForm1Locators.LOCATOR_PERIODICITY, description='Ежемесячная')

    @allure.step('Автозаполнение поле Вкладка')
    def select_tab(self):
        return self.get_text_from_element(TestForm1Locators.LOCATOR_TAB, description='Форма №1')

    @allure.step('Клик на кнопку добавления новой строки')
    def click_add_new_row(self):
        self.click_button(TestForm1Locators.LOCATOR_BUTTON_NEW_ROW, description='Кнопка добавления новой строки')

    @allure.step('Добавление атрибута Территории')
    def select_territory(self):
        self.click_button(TestForm1Locators.LOCATOR_BUTTON_NEW_ROW1)
        self.click_button(TestForm1Locators.LOCATOR_TERRITORY, description='Все территории РФ')

    @allure.step('Добавление атрибута Зарегистрировано заболеваний...')
    def select_registered_diseases(self):
        self.click_button(TestForm1Locators.LOCATOR_BUTTON_NEW_ROW2)
        self.click_button(TestForm1Locators.LOCATOR_REGISTERED_Diseases, description='Зарегистрировано заболеваний в')

    @allure.step('Клик на кнопку добавления нового столбца')
    def click_add_new_column(self):
        self.click_button(TestForm1Locators.LOCATOR_BUTTON_NEW_COLUMN, description='Кнопка добавления нового столбца')

    @allure.step('Добавление атрибута Год(а)')
    def select_year(self):
        self.click_button(TestForm1Locators.LOCATOR_NEW_COLUMN)
        self.click_button(TestForm1Locators.LOCATOR_YEAR, description='Год')

    @allure.step('Добавление значений для атрибута Год(а)')
    def click_yars_2022(self):
        self.click_button(TestForm1Locators.LOCATOR_NEW_COLUMN1)
        self.click_button(TestForm1Locators.LOCATOR_YEAR_2022, description='2022')
        self.click_button(TestForm1Locators.LOCATOR_YEAR_2023, description='2023')
        self.click_button(TestForm1Locators.LOCATOR_YEAR_2024, description='2024')

    @allure.step('Клик на кнопку добавления нового столбца')
    def click_add_new_column(self):
        self.click_button(TestForm1Locators.LOCATOR_BUTTON_NEW_COLUMN, description='Кнопка добавления нового столбца')

    @allure.step('Добавление атрибута Месяц')
    def select_month(self):
        self.click_button(TestForm1Locators.LOCATOR_NEW_COLUMN2)
        self.click_button(TestForm1Locators.LOCATOR_MONTH, description='Месяц')

    @allure.step('Добавление значений для атрибута Месяц')
    def click_months(self):
        self.click_button(TestForm1Locators.LOCATOR_NEW_COLUMN3)
        self.click_button(TestForm1Locators.LOCATOR_MONTH_JANUARY, description='Январь')
        self.click_button(TestForm1Locators.LOCATOR_MONTH_FEBRUARY, description='Февраль')
        self.click_button(TestForm1Locators.LOCATOR_MONTH_MARCH, description='Март')

    @allure.step('Добавление нового условия')
    def click_new_condition(self):
        self.click_button(TestForm1Locators.LOCATOR_BUTTON_NEW_CONDITION,
                          description='Кнопка добавления нового условия')

    @allure.step('Добавление атрибута Группы заболеваний')
    def select_group_of_diseases(self):
        self.click_button(TestForm1Locators.LOCATOR_NEW_CONDITION)
        self.click_button(TestForm1Locators.LOCATOR_GROUP_OF_DISEASES, description='Группы заболеваний для Формы 1')

    @allure.step('Добавление значений Нозологии')
    def select_diagnosis(self):
        self.click_button(TestForm1Locators.LOCATOR_NEW_CONDITION1)
        self.click_button(TestForm1Locators.LOCATOR_DIAGNOSIS, description='Острые инфекции верхних дыхате')

    @allure.step('Добавление нового условия')
    def click_new_condition(self):
        self.click_button(TestForm1Locators.LOCATOR_BUTTON_NEW_CONDITION,
                          description='Кнопка добавления нового условия')

    @allure.step('Добавление атрибута Возрастные группы')
    def select_age_groups(self):
        self.click_button(TestForm1Locators.LOCATOR_NEW_CONDITION2)
        self.click_button(TestForm1Locators.LOCATOR_AGE_GROUPS, description='Возрастные группы')

    @allure.step('Добавление значения Все возраста')
    def select_all_age(self):
        self.click_button(TestForm1Locators.LOCATOR_NEW_CONDITION3)
        self.click_button(TestForm1Locators.LOCATOR_ALL_AGE, description='Все возраста')

    @allure.step('Кнопка формирования отчета')
    def click_generate_report(self):
        self.click_button(TestForm1Locators.LOCATOR_GENERATE_A_REPORT, description='Кнопка формирования отчета')

    @allure.step('Проверка таблицы')
    def get_table_data(self):
        self.get_table_data_and_compare(TestForm1Locators.LOCATOR_REPORT_TABLE, table_mock_form1)

    @allure.step('Кнопка создания пользовательского шаблона')
    def click_create_template(self):
        self.click_button(UserTemplates.LOCATOR_BUTTON_NEW_TEMPLATE)

    @allure.step('Поле Имя шаблона: {word}')
    def enter_template_name(self, word):
        self.enter_text_into_field(UserTemplates.LOCATOR_TEMPLATE_NAME, word)

    @allure.step('Кнопка сохранения шаблона')
    def click_save_template(self):
        self.click_button(UserTemplates.LOCATOR_SAVE_TEMPLATE)

    @allure.step('Удаление пользовательского шаблона')
    def delete_template(self):
        self.click_button(UserTemplates.LOCATOR_DELETE_TEMPLATE)
        self.click_button(UserTemplates.LOCATOR_POPUP_DELETE_TEMPLATE)

    @allure.step('Выбор шаблона запроса')
    def template_selection(self):
        self.click_button(TestForm1Locators.LOCATOR_TEMPLATE_REQUEST)
        self.click_button(TestForm1Locators.LOCATOR_TEST_TEMPLATE)

    @allure.step('Выбор чекбокса Средний многолетний за 10 лет')
    def select_average_10_years(self):
        self.click_checkbox(TestForm1Locators.LOCATOR_CHECKBOX_AVERAGE_10_YEARS)