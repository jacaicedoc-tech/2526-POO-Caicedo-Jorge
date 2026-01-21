# --------------------------------------------
# PROGRAMA: Gestión de Empleados
# Uso de Constructores (__init__)
# --------------------------------------------

class Empleado:
    def __init__(self, nombre, cargo, salario):
        """
        Constructor de la clase Empleado.
        Se ejecuta automáticamente al crear un objeto.
        Inicializa los atributos del empleado.
        """
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        print("Empleado registrado correctamente.")

    def mostrar_datos(self):
        """
        Muestra la información del empleado.
        """
        print("Nombre:", self.nombre)
        print("Cargo:", self.cargo)
        print("Salario:", self.salario)


# --------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------

empleado1 = Empleado("Jorge Caicedo", "Recaudador", 600)
empleado1.mostrar_datos()
