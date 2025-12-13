# --------------------------------------------
# PROGRAMA: Promedio semanal del clima
# Paradigma: Programación Orientada a Objetos POO
# --------------------------------------------

# Clase base (ABSTRACCIÓN + ENCAPSULAMIENTO)
class ClimaDiario:
    def __init__(self, temperatura):
        # Atributo privado (encapsulamiento)
        self.__temperatura = temperatura

    # metodo para obtener temperatura

    def obtener_temperatura(self):
        return self.__temperatura


# Clase hija que hereda de ClimaDiario (HERENCIA)
class ClimaSemanal(ClimaDiario):
    def __init__(self):
        # Lista privada para almacenar las temperaturas
        self.__temperaturas = []

    # metodo para ingresar temperaturas a diario

    def ingresar_temperaturas(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves",
                "Viernes", "Sábado", "Domingo"]

        print("=== Registro del clima semanal ===")

        for dia in dias:
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            clima_dia = ClimaDiario(temp)   # Uso de la clase base
            self.__temperaturas.append(clima_dia)

    # metodo para calcular el promedio semanal

    # (POLIMORFISMO: redefine el comportamiento)
    def calcular_promedio(self):
        suma = 0
        for dia in self.__temperaturas:
            suma += dia.obtener_temperatura()

        promedio = suma / len(self.__temperaturas)
        return promedio


# Programa principal
def main():
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()

    print("\n--------------------------------")
    print("PROMEDIO SEMANAL DEL CLIMA")
    print("--------------------------------")
    print(f"Temperatura promedio: {promedio:.2f} °C")


# Ejecución del programa
main()
