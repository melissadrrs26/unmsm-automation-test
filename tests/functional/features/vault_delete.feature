Feature: Boveda Bitwarden

  Scenario: Eliminar ítem en Bitwarden Vault
    Given El usuario inicia sesión en Bitwarden
    When Existe el ítem llamado "elementoZ"
    And Hace clic en la opción para eliminar el ítem
    And Confirma la eliminación
    Then Debería estar eliminado el ítem "elementoZ"

  