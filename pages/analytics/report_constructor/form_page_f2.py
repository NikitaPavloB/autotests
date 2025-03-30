from base.BaseApp import BasePage
from selenium.webdriver.common.by import By
import allure
from pages.analytics.report_constructor.form_page_f1 import TestForm1Locators

class TestForm2Locators:
    # Авторизация в TestForm1Locators
    # Переход в раздел в TestForm1Locators
    # Поле Форма в TestForm1Locators
    # ВЫБОР ФОРМЫ ИЗ СПИСКА
    LOCATOR_FORM2 = (By.XPATH, """(//nz-option-item[@ng-reflect-label='Форма 2 «Сведения об инфекцион'])[1]""")
    # Поле Периодичность в TestForm1Locators
    # ПОЛЕ ВКЛАДКА
    LOCATOR_TABS = (By.XPATH, "//nz-select-item[@ng-reflect-label='Инфекционные заболевания']")
# class UserTemplates:
class OperationsHelper2(BasePage):
    @allure.step('Поиск формы в выпадающем списке: {word}')
    def enter_form_name(self, word):
        self.enter_text_into_field(TestForm1Locators.LOCATOR_FORM, word)
        self.click_button(TestForm2Locators.LOCATOR_FORM2, description="Форма 2")

    @allure.step('Автозаполнение поле Вкладка')
    def select_tabs(self):
        self.click_button(TestForm2Locators.LOCATOR_TABS, description="Инфекционные заболевания")

