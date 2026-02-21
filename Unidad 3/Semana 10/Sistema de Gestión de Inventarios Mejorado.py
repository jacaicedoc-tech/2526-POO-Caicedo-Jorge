
#Sistema de Gestión de Inventarios Mejorado

import os

# ==========================
# Clase Producto
# ==========================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_line(self):
        """Convierte el producto en una línea para guardarlo en el archivo"""
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"

    def from_line(linea):
        """Reconstruye un producto desde una línea del archivo"""
        try:
            id_producto, nombre, cantidad, precio = linea.strip().split(",")
            return Producto(id_producto, nombre, int(cantidad), float(precio))
        except ValueError:
            print("Línea corrupta encontrada en el archivo y fue ignorada.")
            return None


# ==========================
# Clase Inventario
# ==========================
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga productos desde el archivo"""
        try:
            if not os.path.exists(self.archivo):
                # Crear archivo si no existe
                open(self.archivo, "w").close()
                print("Archivo de inventario creado automáticamente.")
                return

            with open(self.archivo, "r") as f:
                for linea in f:
                    producto = Producto.from_line(linea)
                    if producto:
                        self.productos[producto.id_producto] = producto

            print("Inventario cargado correctamente.")

        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar inventario: {e}")

    def guardar_inventario(self):
        """Guarda todos los productos en el archivo"""
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(producto.to_line())
            print("Cambios guardados correctamente en el archivo.")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar inventario: {e}")

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("El producto ya existe.")
            return
        self.productos[producto.id_producto] = producto
        self.guardar_inventario()
        print("Producto agregado correctamente.")

    def actualizar_producto(self, id_producto, cantidad, precio):
        if id_producto not in self.productos:
            print("Producto no encontrado.")
            return
        self.productos[id_producto].cantidad = cantidad
        self.productos[id_producto].precio = precio
        self.guardar_inventario()
        print("Producto actualizado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto not in self.productos:
            print("Producto no encontrado.")
            return
        del self.productos[id_producto]
        self.guardar_inventario()
        print("Producto eliminado correctamente.")

    def buscar_producto(self, id_producto):
        return self.productos.get(id_producto, None)

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        for producto in self.productos.values():
            print(f"ID: {producto.id_producto} | "
                  f"Nombre: {producto.nombre} | "
                  f"Cantidad: {producto.cantidad} | "
                  f"Precio: ${producto.precio:.2f}")


# ==========================
# Interfaz de Usuario
# ==========================
def menu():
    inventario = Inventario()

    while True:
        print("\n=== SISTEMA DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)

            elif opcion == "2":
                id_producto = input("ID del producto: ")
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(id_producto, cantidad, precio)

            elif opcion == "3":
                id_producto = input("ID del producto: ")
                inventario.eliminar_producto(id_producto)

            elif opcion == "4":
                id_producto = input("ID del producto: ")
                producto = inventario.buscar_producto(id_producto)
                if producto:
                    print(f"ID: {producto.id_producto} | "
                          f"Nombre: {producto.nombre} | "
                          f"Cantidad: {producto.cantidad} | "
                          f"Precio: ${producto.precio:.2f}")
                else:
                    print("Producto no encontrado.")

            elif opcion == "5":
                inventario.mostrar_inventario()

            elif opcion == "6":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")
        except Exception as e:
            print(f"Error inesperado: {e}")


# Ejecutar programa
if __name__ == "__main__":
    menu()