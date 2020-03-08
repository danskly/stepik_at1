product_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_language(browser):
    browser.implicitly_wait(7)
    browser.get(product_page)
    add_to_basket_button = browser.find_element_by_css_selector('.btn-add-to-basket')

    assert add_to_basket_button.is_displayed(), 'Кнопка добавления товара в корзину не отображается'
