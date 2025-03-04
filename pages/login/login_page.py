from base.BaseApp import BasePage
from selenium.webdriver.common.by import By
import allure


# Локаторы для страницы авторизации


class LoginLocators:
    LOCATOR_LOGIN_FIELD = (By.ID, "login")
    LOCATOR_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_LOGIN_BTN = (By.ID, "submit-button")
    # Проверка входа
    LOCATOR_MENU_FIELD = (By.XPATH, """//div[@class="heading"]/child::h2""")


class LoginPage(BasePage):

    # Ввод текста
    @allure.step('Ввод логина: {word}')
    def enter_login(self, word):
        self.enter_text_into_field(LoginLocators.LOCATOR_LOGIN_FIELD, word, description="Поле 'Логин'")

    @allure.step('Ввод пароля: {word}')
    def enter_password(self, word):
        self.enter_text_into_field(LoginLocators.LOCATOR_PASSWORD_FIELD, word, description="Поле 'Пароль'")

    # Клик на кнопку
    @allure.step("Клик на кнопку 'Войти'")
    def click_login_button(self):
        self.click_button(LoginLocators.LOCATOR_LOGIN_BTN, description="Кнопка 'Войти'")

    # Получение текста
    @allure.step("Проверяем успешную авторизацию пользователя")
    def get_menu_text(self):
        return self.get_text_from_element(LoginLocators.LOCATOR_MENU_FIELD, description="Текст меню после авторизации")

