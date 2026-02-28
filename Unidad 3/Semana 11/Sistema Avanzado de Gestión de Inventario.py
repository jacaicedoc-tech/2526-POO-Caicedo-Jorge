


import json
import os

# =========================
# Clase Producto
# =========================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Convertir a diccionario (para guardar en JSON)
    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    # Crear objeto desde diccionario

    def from_dict(data):
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )


# =========================
# Clase Inventario
# =========================
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario: {id: Producto}

    # Añadir producto
    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto añadido correctamente.")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    # Buscar por nombre
    def buscar_por_nombre(self, nombre):
        encontrados = [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

        if encontrados:
            for p in encontrados:
                print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio()}")
        else:
            print("No se encontraron productos.")

    # Mostrar todos
    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos.values():
                print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio()}")

    # Guardar en archivo
    def guardar_en_archivo(self, archivo="inventario.json"):
        with open(archivo, "w") as f:
            json.dump(
                [p.to_dict() for p in self.productos.values()],
                f,
                indent=4
            )
        print("Inventario guardado correctamente.")

    # Cargar desde archivo
    def cargar_desde_archivo(self, archivo="inventario.json"):
        if os.path.exists(archivo):
            with open(archivo, "r") as f:
                datos = json.load(f)
                for item in datos:
                    producto = Producto.from_dict(item)
                    self.productos[producto.get_id()] = producto
            print("Inventario cargado correctamente.")
        else:
            print("No existe archivo previo. Se iniciará vacío.")


# =========================
# Menú Interactivo
# =========================
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_p, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_p = input("Ingrese ID a eliminar: ")
            inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(id_p, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo()

        elif opcion == "7":
            inventario.guardar_en_archivo()
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


# Ejecutar programa
if __name__ == "__main__":
    menu()