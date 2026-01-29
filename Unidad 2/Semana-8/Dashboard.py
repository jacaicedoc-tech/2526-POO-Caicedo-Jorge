# Dashboard.py adaptado
# Autor: Jorge Andrés Caicedo Chere
# Materia: Programación Orientada a Objetos
# Descripción:
# Dashboard orientado a objetos para navegar por las unidades,
# visualizar scripts y ejecutarlos desde consola.

import os
import subprocess


class Dashboard:
    """
    Clase Dashboard que administra el menú principal,
    submenús y ejecución de scripts Python.
    """

    def __init__(self):
        # Ruta base donde se encuentra el archivo Dashboard.py
        self.ruta_base = os.path.dirname(__file__)
        self.unidades = {
            '1': 'Unidad 1',
            '2': 'Unidad 2'
        }

    def mostrar_codigo(self, ruta_script):
        """
        Muestra el código fuente de un script Python
        """
        ruta_script_absoluta = os.path.abspath(ruta_script)
        try:
            with open(ruta_script_absoluta, 'r') as archivo:
                codigo = archivo.read()
                print(f"\n--- Código de {ruta_script} ---\n")
                print(codigo)
                return codigo
        except FileNotFoundError:
            print("El archivo no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")
        return None

    def ejecutar_codigo(self, ruta_script):
        """
        Ejecuta un script Python en una nueva terminal
        """
        try:
            if os.name == 'nt':  # Windows
                subprocess.Popen(['cmd', '/k', 'python', ruta_script])
            else:  # Linux / Mac
                subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
        except Exception as e:
            print(f"Ocurrió un error al ejecutar el código: {e}")

    def mostrar_menu(self):
        """
        Muestra el menú principal del dashboard
        """
        while True:
            print("\n=== MENU PRINCIPAL - DASHBOARD ===")
            for key, value in self.unidades.items():
                print(f"{key} - {value}")
            print("0 - Salir")

            eleccion = input("Elige una unidad o '0' para salir: ")

            if eleccion == '0':
                print("Saliendo del programa.")
                break
            elif eleccion in self.unidades:
                ruta_unidad = os.path.join(self.ruta_base, self.unidades[eleccion])
                self.mostrar_sub_menu(ruta_unidad)
            else:
                print("Opción no válida.")

    def mostrar_sub_menu(self, ruta_unidad):
        """
        Muestra las subcarpetas dentro de una unidad
        """
        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

        while True:
            print("\n--- SUBMENÚ ---")
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
                    self.mostrar_scripts(ruta_sub)
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

    def mostrar_scripts(self, ruta_sub_carpeta):
        """
        Muestra los scripts Python disponibles en una subcarpeta
        """
        scripts = [
            f.name for f in os.scandir(ruta_sub_carpeta)
            if f.is_file() and f.name.endswith('.py')
        ]

        while True:
            print("\n--- SCRIPTS DISPONIBLES ---")
            for i, script in enumerate(scripts, start=1):
                print(f"{i} - {script}")
            print("0 - Regresar")
            print("9 - Menú principal")

            eleccion = input("Selecciona una opción: ")

            if eleccion == '0':
                break
            elif eleccion == '9':
                return
            try:
                indice = int(eleccion) - 1
                if 0 <= indice < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
                    codigo = self.mostrar_codigo(ruta_script)

                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            self.ejecutar_codigo(ruta_script)

                        input("\nPresiona Enter para continuar...")
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")


# Programa principal
if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.mostrar_menu()
