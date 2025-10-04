# Demo: Login con Behave + Selenium en Bitwarden Vault

Este proyecto es un ejemplo de automatización de login en **Bitwarden Vault** usando **Behave (Cucumber para Python)** y **Selenium**.

## ⚠️ Advertencia
No uses tus credenciales reales en este ejemplo. Usa cuentas de prueba o entornos de staging.

## 🚀 Requisitos
- Python 3.8+
- Google Chrome
- pip

## 📦 Instalación
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

## ▶️ Ejecución
```bash
behave
```

Esto abrirá Chrome, intentará loguearse en [Bitwarden Vault](https://vault.bitwarden.com/) y validará la redirección al **Vault**.
