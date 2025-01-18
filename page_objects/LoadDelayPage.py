import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class LoadDelayPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.button_locator = (By.XPATH, '//button[contains(text(), "Button Appearing After Delay")]')

    @allure.step("Ожидание появления кнопки после задержки")
    def present_button_after_delay(self) -> None:
        """Проверка существования кнопки после задержки."""
        self.wait_for_element_to_be_visible(self.button_locator)

    @allure.step("Проверка, что кнопка отображается")
    def is_button_displayed(self) -> bool:
        """Проверка, что кнопка отображается на странице."""
        return self.is_element_visible(self.button_locator)
