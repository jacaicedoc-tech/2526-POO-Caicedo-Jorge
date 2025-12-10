# Ejemplo de Abstracción

class Animal:
    def hacer_sonido(self):
        pass   # Metodo abstracto (solo declaración)

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Uso
perro = Perro()
gato = Gato()

print(perro.hacer_sonido())
print(gato.hacer_sonido())
