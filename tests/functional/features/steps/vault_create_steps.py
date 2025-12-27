# features/steps/vault_create_steps.py
from multiprocessing import context
from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@when('Hace clic en la opción para crear un nuevo ítem de tipo "{option_name}"')
def step_impl(context, option_name):

    # Dar clic en "Nuevo"
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//button[@title='Nuevo']").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, f"//button[.//span[normalize-space()='{option_name}']]").click()


@when('Rellena los detalles del ítem con nombre "{item_name}", usuario "{username}" y contraseña "{password}"')
def step_impl(context, item_name, username, password):
    driver = context.driver

    # Esperar que aparezca el popup de nuevo ítem
    time.sleep(5)
    search_box = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='name']")
    search_box.clear()
    search_box.send_keys(item_name)

    search_box = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='username']")
    search_box.clear()
    search_box.send_keys(username)

    search_box = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='password']")
    search_box.clear()
    search_box.send_keys(password)

@when("Guarda el ítem")
def step_impl(context): 
    driver = context.driver

    # Dar clic en guardar
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[.//span[normalize-space()='Guardar']]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//button[@biticonbutton='bwi-close']").click()
    time.sleep(3)

@then('Debería existir el ítem "{item_name}"')
def step_impl(context, item_name): 

    # Esperar resultados
    time.sleep(2)
    results = context.driver.find_elements(By.XPATH, f"//tr[.//button[normalize-space()='{item_name}']]")
    context.item_found = len(results) > 0

    assert context.item_found, f"❌ Item '{item_name}' no se creó correctamente."
    print(f"✅ Item '{item_name}' se creó exitosamente.")
