# Ejemplo de Polimorfismo

class Pato:
    def sonido(self):
        return "Cuac!"

class Gato:
    def sonido(self):
        return "Miau!"

def hacer_sonido(animal):
    print(animal.sonido())


hacer_sonido(Pato())
hacer_sonido(Gato())
