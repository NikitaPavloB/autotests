import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://entry.test.rpn/auth/master/oauth/auth?redirect_uri=http%3A%2F%2Fentry.test.rpn%2F&client_id=f92bc23c-74ac-4f88-a34f-090b6fd6e09d&response_type=gateway&flow_type=browser_flow"

    def find_element(self, locator, time=20, condition=EC.visibility_of_element_located):
        try:
            element = WebDriverWait(self.driver, time).until(
                condition(locator),
                message=f"Can't find element by locator {locator}"
            )
            return element
        except:
            logging.exception(f"Exception while finding element {locator}")
            return None

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f"Property {property} not found in element with locator {locator}")
            return None

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open site")
            start_browsing = None
        return start_browsing

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.txt
        except:
            logging.exception("Exception with alert")
            return None

    # Метод для работы с выпадающими списками
    def select_dropdown_option(self, locator, text, time=10):
        try:
            dropdown = Select(self.find_element(locator, time))
            dropdown.select_by_value(text)
            logging.debug(f"Selected '{text}' in dropdown {locator}")
            return True
        except:
            logging.exception(f"Failed to select '{text}' in dropdown {locator}")
            return False

    # Вспомогательный элемент для ввода текста
    def enter_text_into_field(self, locator, word, description=None, press_enter=False):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.info(f"Send {word} to element {element_name}")
        field = self.find_element(locator, time=10, condition=EC.visibility_of_element_located)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
            if press_enter:
                field.send_keys(Keys.ENTER)
                logging.info(f"Pressed ENTER after entering '{word}' into {element_name}")
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    # Вспомогательный элемент для клика
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator, time=10, condition=EC.element_to_be_clickable)
        if not button:
            logging.error(f"Button {element_name} not found or not clickable")
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.info(f"Clicked {element_name} button")
        return True

    # Вспомогательный элемент для получения текста
    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return None
        logging.info(f"We find text {text} in field {element_name}")
        return text

    # Наводим курсор на один элемент и кликаем по другому
    def hover_and_click(self, hover_locator, click_locator, description=None, time=10):
        try:
            hover_element = self.find_element(hover_locator, time)
            actions = ActionChains(self.driver)
            actions.move_to_element(hover_element).perform()
            logging.info(f"Навели курсор на элемент: {hover_locator}")

            target_element = WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable(click_locator)
            )
            target_element.click()
            logging.info(f"Клик по элементу: {click_locator}")
            return True
        except:
            logging.exception(f"Не удалось навести на {hover_locator} и кликнуть по {click_locator}")
            return False

    # Перезагрузка страницы
    def reload_page(self):
        try:
            self.driver.refresh()
            logging.info("Страница успешно перезагружена")
            return True
        except:
            logging.exception("Ошибка при перезагрузке страницы")
            return False

    # Вспомогательный метод для работы с выпадающими списками

    def select_from_dropdown(self, locator, text, description=None):
        if description:
            logging.info(f"Trying to select '{text}' from {description}")
        else:
            logging.info(f"Trying to select '{text}' from dropdown {locator}")

        result = self.select_dropdown_option(locator, text, time=3)

        if result:
            logging.info(f"Successfully selected '{text}'")
        else:
            logging.error(f"Failed to select '{text}'")
        return result

    # Метод проверки значений в формируемых таблицах аналитического конструктора
    def get_table_data_and_compare(self, locator, mock_data):
        try:
            # Ожидание загрузки таблицы
            table = self.find_element(locator, time=10, condition=EC.presence_of_element_located)

            # Получение всех строк таблицы
            rows = table.find_elements(By.TAG_NAME, "tr")

            # Список для хранения данных из таблицы
            table_data = []

            # Извлечение данных из таблицы
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                row_data = [cell.text for cell in cells]
                if row_data:  # Игнорируем пустые строки (например, заголовки th)
                    table_data.append(row_data)

            # Получение ожидаемых данных(страницы с ожидаемыми результатами отдельным файлом создаем в папке mock)
            mock_data = mock_data()

            # Проверка данных
            all_match = True
            for i, row in enumerate(table_data):
                for j, cell_value in enumerate(row):
                    if cell_value != mock_data[i][j]:
                        logging.error(f"Несоответствие в строке {i + 1}, столбце {j + 1}: "
                                      f"Ожидалось '{mock_data[i][j]}', но получено '{cell_value}'")
                        all_match = False

            if all_match:
                logging.info("Все данные таблицы соответствуют ожидаемым")
            else:
                logging.warning("Обнаружены расхождения в данных таблицы")

            return all_match
        except:
            logging.exception("Ошибка при работе с таблицей")
            return False

    # Метод для работы с чекбоксом
    def click_checkbox(self, locator, description=None, expected_state=True):
        if description:
            element_name = description
        else:
            element_name = locator

        try:
            checkbox = self.find_element(locator, time=10, condition=EC.element_to_be_clickable)
            if not checkbox:
                logging.error(f"Чекбокс {element_name} не найден или недоступен для клика")
                return False

            current_state = checkbox.is_selected()

            if current_state != expected_state:
                checkbox.click()
                logging.info(
                    f"Клик по чекбоксу {element_name}. Установлено состояние: {'выбран' if expected_state else 'не выбран'}")

            new_state = checkbox.is_selected()
            if new_state != expected_state:
                logging.error(
                    f"Состояние чекбокса {element_name} не изменилось как ожидалось. Текущее состояние: {'выбран' if new_state else 'не выбран'}")
                return False

            return True

        except Exception as e:
            logging.exception(f"Ошибка при работе с чекбоксом {element_name}")
            return False
