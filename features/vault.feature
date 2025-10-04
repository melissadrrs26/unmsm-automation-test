Feature: Boveda Bitwarden

  Scenario: Buscar ítem en Bitwarden Vault
    Given El usuario inicia sesión en Bitwarden
    When Busca el ítem "elemento1" en la bóveda
    Then Debería encontrar el ítem "elemento1"