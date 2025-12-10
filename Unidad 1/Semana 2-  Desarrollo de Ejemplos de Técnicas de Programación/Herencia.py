# Ejemplo de Herencia

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        return "Vehículo encendido"

class Moto(Vehiculo):
    pass

m = Moto("Moto Yamaha")
print(m.marca)
print(m.encender())
