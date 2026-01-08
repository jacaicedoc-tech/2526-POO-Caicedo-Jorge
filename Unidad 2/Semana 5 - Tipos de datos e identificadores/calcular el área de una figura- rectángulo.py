"""
Programa: Calculadora del área de un rectángulo
Descripción: Este programa solicita al usuario el ancho y el alto de un rectángulo,
calcula su área y muestra el resultado en pantalla.
"""

# Solicitar datos al usuario (string y float)
ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
alto_rectangulo = float(input("Ingrese el alto del rectángulo: "))

# Cálculo del área (float)
area_rectangulo = ancho_rectangulo * alto_rectangulo

# Variable booleana para validar si el área es mayor que cero
area_valida = area_rectangulo > 0

# Mostrar resultados
print("\n--- Resultados ---")
print("El área del rectángulo es:", area_rectangulo)

# Uso de boolean
if area_valida:
    print("El área calculada es válida.")
else:
    print("El área calculada no es válida.")
