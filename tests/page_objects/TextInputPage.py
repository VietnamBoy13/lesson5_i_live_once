import allure
from selenium.webdriver.common.by import By
from tests.page_objects.BasePage import BasePage

class TextInputPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.input_locator = (By.ID, "newButtonName")
        self.button_locator = (By.ID, "updatingButton")

    @allure.step("Ввод нового имени кнопки")
    def enter_new_button_name(self, name: str) -> None:
        """Ввод нового имени кнопки в поле ввода."""
        input_field = self.wait_for_element_to_be_visible(self.input_locator)
        input_field.clear()  # Очистка поля ввода
        input_field.send_keys(name)  # Ввод нового имени

    @allure.step("Нажатие на кнопку")
    def click_update_button(self) -> None:
        """Нажатие на кнопку для обновления имени."""
        button = self.wait_for_element_to_be_visible(self.button_locator)
        button.click()

    @allure.step("Получение текста кнопки")
    def get_button_text(self) -> str:
        """Получение текста кнопки."""
        button = self.wait_for_element_to_be_visible(self.button_locator)
        return button.text
