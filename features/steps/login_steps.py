from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@given("El usuario abre la página de login de Bitwarden")
def step_open_login(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://vault.bitwarden.com/")
    context.driver.maximize_window()
    time.sleep(5)  # esperar a que cargue la página

@when('Ingresa el correo "{correo}"')
def step_enter_credentials(context, correo):
    context.driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys(correo)
    #context.driver.find_element(By.ID, "email").send_keys(correo)
    #context.driver.find_element(By.ID, "masterPassword").send_keys(password)

@when('Hace clic en el botón de continuar')
def step_enter_credentials(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[buttontype='primary']").click()
    time.sleep(3)  # esperar a que cargue la página

@when('Ingresa la clave "{password}"')
def step_enter_credentials(context, password):
    context.driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)

@when("Hace clic en el botón de login")
def step_click_login(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)  # esperar a que cargue la página

@then("Debería ver la página principal de Vault")
def step_verify_vault(context):
    assert "vault" in context.driver.current_url.lower()
    context.driver.quit()
