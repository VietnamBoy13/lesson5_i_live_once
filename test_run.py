from pages import LoginPage, InventoryPage, ItemPage, CartPage


def test_est_1_login(driver):
    auth_page = LoginPage(driver)
    auth_page.auth('standard_user', 'secret_sauce')

    inventory_page = InventoryPage(driver)
    inventory_page.choose_item()

    item_page = ItemPage(driver)
    item_page.add_to_cart_btn_click()
    item_page.back_to_products_click()
    inventory_page.add_jacket_to_cart_btn_click()
    inventory_page.cart_btn_click()

    cart_page = CartPage(driver)
    assert cart_page.number_of_products() == 2
    cart_page.back_to_products_btn_click()

# ниже делаешь выход на станицу с входом
    inventory_page.open_to_menu_btn_click()
    inventory_page.back_to_logout_click()

    auth_page.auth('standard_user', '12345')

# проверку входа на страницу