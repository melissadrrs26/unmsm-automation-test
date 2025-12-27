Feature: Boveda Bitwarden

  Scenario: Editar ítem en Bitwarden Vault
    Given El usuario inicia sesión en Bitwarden
    When Ubique el ítem llamado "elemento1"
    And Hace clic en la opción para editar el ítem
    And Actualiza los detalles del ítem con usuario "usuario1"
    And Edita el ítem
    Then Debería estar actualizado el ítem "elemento1" con usuario "usuario1"

  