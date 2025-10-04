# features/environment.py
import os
import allure
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    """Configura entorno global antes de todas las pruebas."""
    load_dotenv()  # 🔹 Cargar claves desde .env

    # Guardar credenciales en el contexto Behave
    context.user = os.getenv("BITWARDEN_USER")
    context.password = os.getenv("BITWARDEN_PASSWORD")
    # Configurar navegador
    options = Options()
    # options.add_argument("--headless")  # Descomentar si no quieres interfaz
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.driver.maximize_window()

def after_all(context):
    """Cierra el navegador al finalizar todas las pruebas."""
    context.driver.quit()

def after_step(context, step):
    if step.status == "failed" and hasattr(context, "driver"):
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=f"{step.name}",
            attachment_type=AttachmentType.PNG
        )