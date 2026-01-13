# --------------------------------------------
# PROGRAMA: Sistema de Vehículos
# Paradigma: Programación Orientada a Objetos (POO)
# --------------------------------------------

# CLASE BASE
class Vehiculo:
    def __init__(self, marca, modelo, velocidad_max):
        self.marca = marca
        self.modelo = modelo
        # Encapsulación: atributo privado
        self.__velocidad_max = velocidad_max

    # Getter
    def get_velocidad_max(self):
        return self.__velocidad_max

    # Setter
    def set_velocidad_max(self, nueva_velocidad):
        if nueva_velocidad > 0:
            self.__velocidad_max = nueva_velocidad
        else:
            print("La velocidad debe ser mayor a cero")

    # Método que será sobrescrito (Polimorfismo)
    def descripcion(self):
        return f"Vehículo {self.marca} {self.modelo}"

    def mostrar_info(self):
        print(self.descripcion())
        print(f"Velocidad máxima: {self.get_velocidad_max()} km/h")


# CLASE DERIVADA
class Auto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_max, puertas):
        # Herencia
        super().__init__(marca, modelo, velocidad_max)
        self.puertas = puertas

    # Polimorfismo: sobrescritura del método
    def descripcion(self):
        return f"Auto {self.marca} {self.modelo} con {self.puertas} puertas"


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    # Creación de objetos
    vehiculo1 = Vehiculo("Genérico", "Modelo X", 120)
    auto1 = Auto("Toyota", "Corolla", 180, 4)

    # Uso de métodos
    vehiculo1.mostrar_info()
    print("-------------------")
    auto1.mostrar_info()
