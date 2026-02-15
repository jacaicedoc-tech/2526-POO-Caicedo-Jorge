
# Dashboard.py
# Autor: Jorge Andrés Caicedo Chere
# Materia: Programación Orientada a Objetos
# Repositorio: jacaicedoc-tech/2526-POO-Caicedo-Jorge (estructura real)
# Descripción:
# Dashboard adaptado para navegar por las unidades y ejecutar scripts Python.

import os
import subprocess

def mostrar_codigo(ruta_script):
    """
    Muestra el código fuente del script seleccionado
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    """
    Ejecuta el script Python en Windows usando cmd
    """
    try:
        subprocess.Popen(['cmd', '/k', 'python', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    """
    Menú principal del Dashboard
    """

    # RUTA BASE REAL de tu proyecto en Windows
    ruta_base = r"C:\Users\Kiara\PycharmProjects\2526-POO-Caicedo-Jorge"

    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print("\n===== MENU PRINCIPAL - DASHBOARD =====")
        for key, value in unidades.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")

        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            ruta_unidad = os.path.join(ruta_base, unidades[eleccion_unidad])
            mostrar_sub_menu(ruta_unidad)
        else:
            print("Opción no válida. Intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    """
    Muestra las subcarpetas dentro de la unidad seleccionada
    """
    if not os.path.exists(ruta_unidad):
        print("La carpeta de la unidad no existe.")
        return

    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\n----- SUBMENÚ -----")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion = input("Elige una subcarpeta: ")

        if eleccion == '0':
            break
        try:
            indice = int(eleccion) - 1
            if 0 <= indice < len(sub_carpetas):
                ruta_sub = os.path.join(ruta_unidad, sub_carpetas[indice])
                mostrar_scripts(ruta_sub)
            else:
                print("Opción no válida.")
        except ValueError:
            print("Opción no válida.")

def mostrar_scripts(ruta_sub_carpeta):
    """
    Muestra los scripts .py disponibles en la subcarpeta
    y permite ver su código o ejecutarlos
    """
    scripts = [
        f.name for f in os.scandir(ruta_sub_carpeta)
        if f.is_file() and f.name.endswith('.py')
    ]

    while True:
        print("\n----- SCRIPTS DISPONIBLES -----")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar")
        print("9 - Menú principal")

        eleccion_script = input("Selecciona una opción: ")

        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return
        try:
            indice = int(eleccion_script) - 1
            if 0 <= indice < len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
                codigo = mostrar_codigo(ruta_script)
                if codigo:
                    ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)
                    input("\nPresiona Enter para continuar...")
            else:
                print("Opción no válida.")
        except ValueError:
            print("Opción no válida.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
