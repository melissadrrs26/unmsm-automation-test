# features/steps/vault_create_steps.py
from multiprocessing import context
from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@when('Existe el ítem llamado "{item_name}"')
def step_impl(context, item_name):

    time.sleep(5)
    context.driver.find_element(By.XPATH, f"//button[normalize-space(text())='{item_name}']").click()
    time.sleep(2)

@when("Hace clic en la opción para eliminar el ítem")
def step_impl(context): 

    time.sleep(5)
    context.driver.find_element(By.XPATH, "//button[@biticonbutton='bwi-trash']").click()
    time.sleep(3)

@when('Confirma la eliminación')
def step_impl(context):

    time.sleep(5)
    context.driver.find_element(By.XPATH, "//button[.//span[normalize-space(text())='Sí']]").click()
    time.sleep(3)

@then('Debería estar eliminado el ítem "{item_name}"')
def step_impl(context, item_name): 

    # Esperar resultados
    time.sleep(2)
    results = context.driver.find_elements(By.XPATH, f"//tr[.//button[normalize-space()='{item_name}']]")
    context.item_found = len(results) == 0 

    assert context.item_found, f"❌ Item '{item_name}' no se eliminó correctamente."
    print(f"✅ Item '{item_name}' se eliminó exitosamente.")