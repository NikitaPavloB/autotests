import logging
import pytest
import allure
import pytest_check as check
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.login.login_page import LoginPage


browser_name = "chrome"


# Фикстура для запуска браузера.
@pytest.fixture(scope="session")
def browser():
    if browser_name == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
        print("\n🚀 Запущен браузер: Firefox")
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        print("\n🚀 Запущен браузер: Chrome")

    # driver.maximize_window()
    yield driver
    driver.quit()
    print("\n🛑 Браузер закрыт")

# Хук для обработки падений тестов (но без скриншотов)


_screenshot_made_per_test = {}


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        test_name = item.name

        # Просто фиксируем факт ошибки, но не делаем скриншот
        _screenshot_made_per_test[test_name] = True


# Сохраняет скриншот при каждой ошибке pytest-check, но не завершает тест
def save_screenshot_on_check_fail(driver, description):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"{description}_error_{timestamp}"

        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        print(f"📸 Скриншот '{screenshot_name}' сохранен из pytest-check!")

        # Добавляем лог в Allure, чтобы шаг выделялся красным
        with allure.step(f"❌ Провалено: {description}"):
            assert False, description  # Помечает текущий шаг красным, но тест продолжается

    except Exception as e:
        if isinstance(e, AssertionError):  # Игнорируем assert False, description
            pass
        else:
            print(f"❌ Ошибка при создании скриншота в pytest-check: {e}")


# Фикстура для авторизации, выполняется один раз в начале модуля

@pytest.fixture(scope="module")
def login(browser):
    logging.info('Запустили фикстуру авторизации')
    page = LoginPage(browser)
    page.go_to_site()
    page.enter_login("1test_np")
    page.enter_password("Test123$")
    page.click_login_button()
    with allure.step('Проверка успешной авторизации'):
        if not check.equal(page.get_menu_text(),'Доступные для работы модули:', 'Проверка текста меню'):
            save_screenshot_on_check_fail(browser, 'Проверка авторизации')
    logging.info('Пользователь ввел логин и пароль. Нажал кнопку входа')
    yield page  # Передаем страницу в тесты
