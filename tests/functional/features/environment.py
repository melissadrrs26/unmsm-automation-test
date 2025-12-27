# features/environment.py
import json
import os
import subprocess
import time
import allure
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from requests import options
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
    
def after_step(context, step):
    if step.status == "failed" and hasattr(context, "driver"):
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=f"{step.name}",
            attachment_type=AttachmentType.PNG
        )

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()

    #copy profile default chrome
    options.add_argument(
        r"user-data-dir=C:\selenium-profile"
    )
    options.add_argument("--profile-directory=Default")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.quit()