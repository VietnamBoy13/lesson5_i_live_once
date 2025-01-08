import allure
from selenium.webdriver.common.by import By
from tests.page_objects.BasePage import BasePage

class NbspPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.button_locator = (By.XPATH, "//button[normalize-space()='My Button']")

    @allure.step("Проверка отображения кнопки My Button")
    def check_my_button_is_visible(self) -> None:
        self.wait_for_element_to_be_visible(self.button_locator)
