# Demo: Login con Behave + Selenium en Bitwarden Vault

 **Bitwarden Vault** usando **Behave (Cucumber para Python)** y **Selenium**.

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

For local test, create .env
```Dockers
    BITWARDEN_USER=user
    BITWARDEN_PASSWORD=password
```

## ▶️ Start API debug mode

1. Create .vscode directory 
2. create file launch.json
3. Copy this content
```Dockers
    {
    "version": "0.2.0",
    "configurations": [
        {
        "name": "Debug Behave Scenario",
        "type": "debugpy",
        "request": "launch",
        "module": "behave",
        "args": [
            "-f", "allure_behave.formatter:AllureFormatter",
            "-o", "reports/allure_results",
            "--no-capture",
            "--no-capture-stderr",
            "features/login.feature"
        ],
        "console": "integratedTerminal",
        "justMyCode": true
        }
    ]
    }
```
4. Go to "Run and Debug" and selected "Debug Behave Scenario"
5. If want report test:
```Dockers
   allure generate reports/allure_results -o reports/allure_report --clean
   allure open reports/allure_report
```