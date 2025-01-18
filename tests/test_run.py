import allure
from page_objects.MainPage import MainPage
from page_objects.ProgressBarPage import ProgressBarPage
from page_objects.LoadDelayPage import LoadDelayPage
from page_objects.TextInputPage import TextInputPage
from page_objects.DynamicTablePage import DynamicTablePage
from page_objects.NbspPage import NbspPage
from conftest import driver


@allure.title('Проверка работы Progress Bar')
@allure.description('''
Шаги:
1. Перейти на страницу Progress Bar;
2. Нажать на кнопку "Start";
3. Подождать до достижения нужного значения;
4. Нажать на кнопку "Stop";
5. Проверить, что значение "Result" < 5;
6. Проверить, что значение "Duration" < 17000.
''')
def test_progress_bar(driver):
    main_page = MainPage(driver)
    main_page.click_link_progress_bar()
    progress_bar_page = ProgressBarPage(driver)
    progress_bar_page.click_start_button()
    progress_bar_page.wait_until_desired_value()
    progress_bar_page.click_stop_button()
    with allure.step(r'Проверить, что значение "Result" < 5'):
        assert progress_bar_page.get_result_text() < 5, \
            'Значение Result больше 5'
    with allure.step(r'Проверить, что значение "Duration " < 17000'):
        assert progress_bar_page.get_duration_text() < 17000, \
            'Значение Duration больше 17000'


@allure.title('Проверка работы Load Delay')
@allure.description('''
Шаги:
1. Перейти на страницу Load Delay;
2. Ожидать появления кнопки "Button Appearing After Delay";
3. Проверить, что кнопка отображается.
''')
def test_load_delay_page(driver):
    main_page = MainPage(driver)
    main_page.click_link_load_delay()
    load_delay_page = LoadDelayPage(driver)
    load_delay_page.present_button_after_delay()
    assert load_delay_page.is_button_displayed(), "Кнопка 'Button Appearing After Delay' не отображается."


@allure.title('Проверка работы Text Input')
@allure.description('''
Шаги:
1. Перейти на страницу Text Input;
2. Ввести новое имя кнопки в поле ввода;
3. Нажать кнопку;
4. Проверить, что имя кнопки изменилось.
''')
def test_text_input_page1(driver):
    main_page = MainPage(driver)
    main_page.click_link_text_input()

    text_input_page = TextInputPage(driver)
    new_button_name = "Новое имя кнопки"  # Пример нового имени

    # Получение текста кнопки до изменения
    old_button_name = text_input_page.get_button_text()

    # Ввод нового имени кнопки
    text_input_page.enter_new_button_name(new_button_name)

    # Нажатие на кнопку
    text_input_page.click_update_button()

    # Получение текста кнопки после изменения
    updated_button_name = text_input_page.get_button_text()

    # Проверка, что имя кнопки изменилось
    assert updated_button_name == new_button_name, f"Имя кнопки не изменилось. Ожидалось: '{new_button_name}', получено: '{updated_button_name}'."


def test_text_input_page(driver):
    main_page = MainPage(driver)
    main_page.click_link_text_input()
    text_input_page = TextInputPage(driver)
    new_button_name = "Новое имя кнопки"
    with allure.step('Получение текста кнопки до изменения'):
        old_button_name = text_input_page.get_button_text()
        allure.attach(old_button_name, name="Старое имя кнопки", attachment_type=allure.attachment_type.TEXT)
    with allure.step('Ввод нового имени кнопки'):
        text_input_page.enter_new_button_name(new_button_name)
    with allure.step('Нажатие на кнопку'):
        text_input_page.click_update_button()
    with allure.step('Получение текста кнопки после изменения'):
        updated_button_name = text_input_page.get_button_text()
        allure.attach(updated_button_name, name="Новое имя кнопки", attachment_type=allure.attachment_type.TEXT)
    assert updated_button_name == new_button_name, f"Имя кнопки не изменилось. Ожидалось: '{new_button_name}', получено: '{updated_button_name}'."


@allure.title('Проверка работы Dynamic Table')
@allure.description('''
Шаги:
1. Перейти на страницу Dynamic Table;
2. Получить значение CPU для процесса Chrome;
3. Получить значение CPU из выделенной желтым строки;
4. Проверить, что оба значения совпадают.
''')
def test_dynamic_table_page(driver):
    main_page = MainPage(driver)
    main_page.click_link_dynamic_table()  # Предполагается, что этот метод существует в MainPage
    dynamic_table_page = DynamicTablePage(driver)

    with allure.step('Получение значения CPU для процесса Chrome'):
        chrome_cpu_value = dynamic_table_page.get_chrome_cpu_value()
        allure.attach(chrome_cpu_value, name="CPU Chrome", attachment_type=allure.attachment_type.TEXT)

    with allure.step('Получение значения CPU из выделенной строки'):
        highlighted_cpu_value = dynamic_table_page.get_highlighted_cpu_value()
        allure.attach(highlighted_cpu_value, name="Выделенный CPU", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Проверить, что CPU Chrome: '{chrome_cpu_value}' совпадает с выделенным CPU: '{highlighted_cpu_value}'"):
        assert chrome_cpu_value == highlighted_cpu_value, f"Значения не совпадают. CPU Chrome: '{chrome_cpu_value}', Выделенный CPU: '{highlighted_cpu_value}'."


@allure.title('Проверка работы Nbsp')
@allure.description('''
Шаги:
1. Перейти на страницу с кнопкой "My Button";
2. Проверить, что кнопка "My Button" с неразрывным пробелом отображается.
''')
def test_nbsp(driver):
    main_page = MainPage(driver)
    main_page.click_link_unbroken_space()
    nbsp_page = NbspPage(driver)
    nbsp_page.check_my_button_is_visible()
