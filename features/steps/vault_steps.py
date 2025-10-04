# features/steps/vault_steps.py
from behave import given, when, then
from helpers.login_helpers import login_helper
from selenium.webdriver.common.by import By
import time

@given("El usuario inicia sesión en Bitwarden")
def step_impl(context):
    login_helper(context)


@when('Busca el ítem "{item_name}" en la bóveda')
def step_impl(context, item_name):
    driver = context.driver

    # Esperar que aparezca el campo de búsqueda
    time.sleep(5)
    search_box = driver.find_element(By.CSS_SELECTOR, "input[name='searchText']")
    search_box.clear()
    search_box.send_keys(item_name)

    # Esperar resultados
    time.sleep(5)
    results = driver.find_elements(By.CSS_SELECTOR, ".tw-table-fixed")
    rows = results.find_elements(By.TAG_NAME, "tr")
    context.item_found = rows > 0


@then('Debería encontrar el ítem "{item_name}"')
def step_impl(context, item_name):
    assert context.item_found, f"❌ Item '{item_name}' no fue encontrado."
    print(f"✅ Item '{item_name}' se encontró exitosamente.")