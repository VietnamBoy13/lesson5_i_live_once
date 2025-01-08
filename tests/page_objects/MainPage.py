from selenium.webdriver.common.by import By
from tests.page_objects.BasePage import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.link_progress_bar = (
            By.XPATH,
            '//div[@class="col-sm"]//a[@href="/progressbar"]'
        )
        self.link_load_delay = (
            By.XPATH,
            '//div[@class="col-sm"]//a[@href="/loaddelay"]'
        )
        self.link_text_input = (
            By.XPATH,
            '//div[@class="col-sm"]//a[@href="/textinput"]'
        )
        self.link_dynamic_table = (
            By.XPATH,
            '//div[@class="col-sm"]//a[@href="/dynamictable"]'
        )
        self.link_unbroken_space = (
            By.XPATH,
            '//div[@class="col-sm"]//a[@href="/nbsp"]'
        )

    @allure.step('Найти ссылку(Progress Bar) и нажать на нее')
    def click_link_progress_bar(self) -> None:
        self.click_element(self.link_progress_bar)

    @allure.step('Найти ссылку(Load Delay) и нажать на нее ')
    def click_link_load_delay(self) -> None:
        self.click_element(self.link_load_delay)

    @allure.step('Найти ссылку(Text Input) и нажать на нее')
    def click_link_text_input(self) -> None:
        self.click_element(self.link_text_input)

    @allure.step('Найти ссылку(Dynamic Table) и нажать на нее')
    def click_link_dynamic_table(self) -> None:
        self.click_element(self.link_dynamic_table)

    @allure.step('Найти ссылку(Non-Breaking Space) и нажать на нее')
    def click_link_unbroken_space(self) -> None:
        self.click_element(self.link_unbroken_space)