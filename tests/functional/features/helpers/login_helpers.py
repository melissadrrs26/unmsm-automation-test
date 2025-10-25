# features/helpers/bitwarden_ui_helper.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_helper(context):
    """
    Realiza el login en Bitwarden Web Vault usando Selenium y las credenciales del contexto.
    """
    driver = context.driver
    driver.get("https://vault.bitwarden.com/#/login")
    time.sleep(4)
    email_input = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    email_input.clear()
    email_input.send_keys(context.user)

    driver.find_element(By.CSS_SELECTOR, "button[buttontype='primary']").click()
    time.sleep(3)

    password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password_input.clear()
    password_input.send_keys(context.password)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)
    
    # Esperar que se cargue la bóveda (elemento característico)
    if "vault" in context.driver.current_url.lower():
        print("✅ Login exitoso en Bitwarden Web Vault")