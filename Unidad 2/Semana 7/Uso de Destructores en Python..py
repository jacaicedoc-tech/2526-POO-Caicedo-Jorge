# --------------------------------------------
# PROGRAMA: Sistema Bancario
# Uso de Destructores (__del__)
# --------------------------------------------

class CuentaBancaria:
    def __init__(self, titular, saldo):
        """
        Constructor de la clase CuentaBancaria.
        Inicializa los datos de la cuenta.
        """
        self.titular = titular
        self.saldo = saldo
        print(f"Cuenta creada para {self.titular}.")

    def mostrar_saldo(self):
        """
        Muestra el saldo actual de la cuenta.
        """
        print(f"Saldo actual: ${self.saldo}")

    def __del__(self):
        """
        Destructor de la clase CuentaBancaria.
        Se ejecuta cuando el objeto se elimina.
        Simula el cierre de la cuenta bancaria.
        """
        print(f"La cuenta de {self.titular} ha sido cerrada.")


# --------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------

cuenta1 = CuentaBancaria("Jorge Caicedo", 3500)
cuenta1.mostrar_saldo()

# Al finalizar el programa o eliminar el objeto,
# el destructor se ejecuta automáticamente
