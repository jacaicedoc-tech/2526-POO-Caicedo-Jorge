# --------------------------------------------
# PROGRAMA: Promedio semanal del clima
# Programación Tradicional con funciones
# --------------------------------------------

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("=== Registro de temperatura semanal ===")

    for dia in dias_semana:
        temp = float(input(f"Ingresa la temperatura del día {dia}: "))
        temperaturas.append(temp)

    return temperaturas


# Función para calcular promedio
def calcular_promedio(lista_temperaturas):
    promedio = sum(lista_temperaturas) / len(lista_temperaturas)
    return promedio


# Función principal
def main():
    datos = ingresar_temperaturas()
    promedio = calcular_promedio(datos)

    print("\n--------------------------------")
    print("PROMEDIO SEMANAL DEL CLIMA")
    print("--------------------------------")
    print(f"La temperatura promedio es: {promedio:.2f} °C")



main()

