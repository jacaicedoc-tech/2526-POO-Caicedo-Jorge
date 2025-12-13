# Función para ingresar las temperaturas diarias
# # Programación Tradicional

def ingresar_temperaturas():
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


def main():
    print("Cálculo del promedio semanal del clima")
    temperaturas_semana = ingresar_temperaturas()
    promedio_semanal = calcular_promedio(temperaturas_semana)
    print(f"El promedio semanal de temperatura es: {promedio_semanal:.2f} °C")


main()
