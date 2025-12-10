# Ejemplo de Encapsulación

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def obtener_nombre(self):
        return self.__nombre

    def cambiar_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre


p = Persona("Andrés")
print(p.obtener_nombre())

p.cambiar_nombre("Kiara")
print(p.obtener_nombre())
