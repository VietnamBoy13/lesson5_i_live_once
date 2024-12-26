import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(driver, timeout)
        self.page_url = 'https://www.saucedemo.com/inventory.html'

    def find_element(self, by: By or int, value: str) -> WebElement:
        return self.wait.until(expected_conditions.visibility_of_element_located((by, value)),
                               message=f'Элемент {by, value} не найден')

    def find_elements(self, by: By or int, value: str) -> [WebElement]:
        return self.wait.until(expected_conditions.visibility_of_all_elements_located((by, value)),
                               message=f'Элементы {by, value} не найдены')

    def get_current_url(self) -> str:
        return self.driver.current_url


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.login = (By.ID, 'user-name')  # Локатор по ID для элемента строки ввода login
        self.password = (By.ID, 'password')  # Локатор по ID для элемента строки ввода password
        self.login_btn = (By.NAME, 'login-button')  # Локатор по Name для элемента кнопка Login

    @allure.step(r'Ввод логина и пароля, нажатие кнопки вход')
    def auth(self, login: str, password: str) -> None:
        self.find_element(*self.login).send_keys(login)
        self.find_element(*self.password).send_keys(password)
        self.find_element(*self.login_btn).click()


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.item = (By.ID, 'item_4_title_link')  # Заголовок любого товара: Здесь будет локатор по ID
        self.add_jacket_to_cat_btn = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")  # Кнопка Add to Cart для Sauce Labs Fleece Jacket: Здесь будет локатор XPATH
        self.cart_btn = (By.XPATH, "//*[@id='shopping_cart_container']")  # Кнопка корзины: Здесь будет локатор XPATH
        self.open_to_menu_btn = (By.ID, 'react-burger-menu-btn')
        self.back_to_logout = (By.XPATH, "//*[@id='logout_sidebar_link']")

    @allure.step(r'Нажатие на заголовок товара "Sauce labs fleece jacket"')
    def choose_item(self) -> None:
        self.find_element(*self.item).click()

    @allure.step(r'Нажатие кнопки "Add to cart" для карточки с товаром под названием "Sauce labs fleece jacket" ')
    def add_jacket_to_cart_btn_click(self) -> None:
        self.find_element(*self.add_jacket_to_cat_btn).click()

    @allure.step(r'Нажатие на кнопку "Корзина" выглядит как тележка из магазина')
    def cart_btn_click(self) -> None:
        self.find_element(*self.cart_btn).click()

    @allure.step(r'Нажатие на кнопку "Menu" выглядит как 3 вертикальные черточки')
    def open_to_menu_btn_click(self) -> None:
        self.find_element(*self.open_to_menu_btn).click()

    @allure.step(r'Нажатие на кнопку "LogOut" для повторного входа на сайт ')
    def back_to_logout_click(self):
        self.find_element(*self.back_to_logout).click()

    @allure.step(r'Проверка, что переход на страницу "https://www.saucedemo.com/inventory.html" не произошёл')
    def assert_not_on_inventory_page(self) -> bool:
        return self.get_current_url() != self.page_url

class ItemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.add_to_cart_btn = (By.XPATH, "//*[@name='add-to-cart']")  # Кнопка Add to Cart: Здесь будет локатор XPATH
        self.back_to_products = (By.XPATH, "//*[@name='back-to-products']")  # Кнопка Back to products: Здесь будет локатор XPATH

    @allure.step(r'Нажатие кнопки добавить в корзину')
    def add_to_cart_btn_click(self) -> None:
        self.find_element(*self.add_to_cart_btn).click()

    @allure.step(r'Нажатие кнопки выход')
    def back_to_products_click(self) -> None:
        self.find_element(*self.back_to_products).click()


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.item_list = (By.XPATH, "//*[@class='inventory_item_price']")  # Локатор XPATH элемента продукта. Локатор должен находить
        # ровно 2 элемента на странице: первый и второй товар,
        # то есть в DevTools вы должны видеть "1 of 2" при поиске данного локатора
        self.back_to_products_btn = (By.XPATH, "//*[@name='continue-shopping']")

    @allure.step(r'Вывод первого и второго товара')
    def number_of_products(self) -> int:
        return len(self.find_elements(*self.item_list))


    @allure.step(r'Нажатие кнопки выход')
    def back_to_products_btn_click (self) -> None:
        self.find_element(*self.back_to_products_btn).click()

