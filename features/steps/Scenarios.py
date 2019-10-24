from behave import *
from features.lib.pages import *


@then("Убедились, что появилось поисковое поле")
def step_impl(context):
    context.page = GoogleMainPage(context)
    assert context.page.search_line


@given('Зашли на сайт "{text}"')
def step_impl(context, text):
    context.page = BasePage(context)
    context.page.visit(text)


@then('Ввели в поисковое поле "{req}"')
def step_impl(context, req):
    context.page.input_search_req(req)


@step('Нажали на кнопку "{text}"')
def step_impl(context, text):
    context.page.search(text)


@then('Нажали на ссылку "{text}"')
def step_impl(context, text):
    context.page = GoogleSearchPage(context)
    context.page.go_link()


@then('Нажали на пункт "{text}"')
def step_impl(context, text):
    context.page = PWMainPage(context)
    context.page.go_menu(text)


@step('Убедились, что перешли в раздел "{text}"')
def step_impl(context, text):
    context.page.assert_page(context, text)


@then('Нажали кнопку "{text}"')
def step_impl(context, text):
    context.page = PWMainPage(context)
    context.page.press_button(context, text)


@then('Нашли поле "{text}" и ввели "{text1}"')
def step_impl(context, text, text1):
    context.page.input_data(context, text, text1)


@then('Выбрали в "{text}" пункт со значением "{text1}"')
def step_impl(context, text, text1):
    context.page.select_value(text, text1)


@step("Убедились, что перешли")
def step_impl(context):
    context.page = PwPayment(context)
    context.page.switch_frames(context)
    assert "bill.php" in context.browser.current_url


@step('Убедились, что значение в поле "{text}" равно "{text1}"')
def step_impl(context, text, text1):
    context.page.sum_assert(context, text, text1)
