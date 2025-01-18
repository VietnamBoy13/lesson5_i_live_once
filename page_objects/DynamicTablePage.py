import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class DynamicTablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.table_locator = (By.ID, "tableId")
        self.chrome_cpu_locator = (
            By.XPATH,
            '//*[@role="cell"][text()="Chrome"]/../*[@role="cell"][contains(text(), "%")]')  # Локатор для значения CPU Chrome
        self.highlighted_cpu_locator = (By.XPATH, '//p[@class="bg-warning"]')  # Локатор для выделенного CPU

    @allure.step("Получение значения CPU для процесса Chrome")
    def get_chrome_cpu_value(self) -> str:
        """Получение значения CPU для процесса Chrome."""
        chrome_cpu_element = self.wait_for_element_to_be_visible(self.chrome_cpu_locator)
        return chrome_cpu_element.text.strip()  # Удаляем лишние пробелы

    @allure.step("Получение значения CPU из выделенной строки")
    def get_highlighted_cpu_value(self) -> str:
        """Получение значения CPU из выделенной строки."""
        return self.wait_for_element_to_be_visible(self.highlighted_cpu_locator).text.split()[-1]
