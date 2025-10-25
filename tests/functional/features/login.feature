Feature: Login Bitwarden

  Scenario: Usuario inicia sesión en Bitwarden Vault
    Given El usuario abre la página de login de Bitwarden
    When Ingresa el correo "melissadrrs@gmail.com"
    And Hace clic en el botón de continuar
    And Ingresa la clave "unmsm123456."
    And Hace clic en el botón de login
    Then Debería ver la página principal de Vault

  Scenario: Usuario ERROR inicia sesión en Bitwarden Vault
    Given El usuario abre la página de login de Bitwarden
    When Ingresa el correo "melissadrrs@gmail.com"
    And Hace clic en el botón de continuar
    And Ingresa la clave "claverror"
    And Hace clic en el botón de login
    Then Debería ver la página principal de Vault
