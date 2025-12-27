Feature: Boveda Bitwarden

  Scenario: Nuevo ítem en Bitwarden Vault
    Given El usuario inicia sesión en Bitwarden
    When Hace clic en la opción para crear un nuevo ítem de tipo "Inicio de sesión"
    And Rellena los detalles del ítem con nombre "elementoX", usuario "usuarioX" y contraseña "user123456."
    And Guarda el ítem
    Then Debería existir el ítem "elementoX"

  