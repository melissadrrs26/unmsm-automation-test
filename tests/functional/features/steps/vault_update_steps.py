# features/steps/vault_create_steps.py
from multiprocessing import context
from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@when('Ubique el ítem llamado "{item_name}"')
def step_impl(context, item_name):

    # Dar clic en "Nuevo"
    time.sleep(5)
    context.driver.find_element(By.XPATH, f"//button[normalize-space(text())='{item_name}']").click()
    time.sleep(2)

@when("Hace clic en la opción para editar el ítem")
def step_impl(context): 
    driver = context.driver

    # Dar clic en guardar
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[.//span[normalize-space()='Editar']]").click()
    time.sleep(3)


@when('Actualiza los detalles del ítem con usuario "{username}"')
def step_impl(context, username):
    driver = context.driver

    # Esperar que aparezca el popup de nuevo ítem
    time.sleep(5)
    search_box = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='username']")
    search_box.clear()
    search_box.send_keys(username)


@when("Edita el ítem")
def step_impl(context): 
    driver = context.driver

    # Dar clic en guardar
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[.//span[normalize-space()='Guardar']]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//button[@biticonbutton='bwi-close']").click()
    time.sleep(3)

@then('Debería estar actualizado el ítem "{item_name}" con usuario "{username}"')
def step_impl(context, item_name, username): 
    driver = context.driver

    # Esperar resultados
    time.sleep(2)
    results_username = driver.find_elements(By.XPATH, f"//tr[.//span[text()='{username}']]")
    results_item = driver.find_elements(By.XPATH, f"//tr[.//button[normalize-space()='{item_name}']]")
    context.item_found = len(results_item) > 0 and len(results_username) > 0

    assert context.item_found, f"❌ Item '{item_name}' no se actualizó correctamente."
    print(f"✅ Item '{item_name}' se actualizó exitosamente.")