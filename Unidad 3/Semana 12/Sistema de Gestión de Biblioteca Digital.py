# ==========================================
# SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL
# ==========================================
# AUTOR POR JORGE CAICEDO
# ==========================================
# ----------- CLASE LIBRO ------------------
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para (título, autor) ya que son datos inmutables del libro
        self.datos_inmutables = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.datos_inmutables[0]}' por {self.datos_inmutables[1]} (ISBN: {self.isbn}) - Cat: {self.categoria}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para gestionar los libros prestados actualmente
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) - Libros: {[l.datos_inmutables[0] for l in self.libros_prestados]}"


class Biblioteca:
    def __init__(self):
        # Diccionario para búsqueda rápida por ISBN {isbn: objeto_Libro}
        self.libros_disponibles = {}
        # Conjunto para asegurar que los IDs de usuario sean únicos
        self.usuarios_registrados = {}  # {id_usuario: objeto_Usuario}
        self.ids_usuarios = set()

    # --- Gestión de Libros ---
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro añadido: {libro.datos_inmutables[0]}")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            eliminado = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {eliminado.datos_inmutables[0]}")
        else:
            print("No se encontró el libro con ese ISBN.")

    # --- Gestión de Usuarios ---
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.ids_usuarios.add(usuario.id_usuario)
            self.usuarios_registrados[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario.nombre}")
        else:
            print(f"Error: El ID {usuario.id_usuario} ya está en uso.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.ids_usuarios:
            usuario = self.usuarios_registrados[id_usuario]
            if not usuario.libros_prestados:
                self.ids_usuarios.remove(id_usuario)
                del self.usuarios_registrados[id_usuario]
                print(f"Usuario {id_usuario} eliminado correctamente.")
            else:
                print("No se puede dar de baja: El usuario tiene libros pendientes de devolver.")
        else:
            print("Usuario no encontrado.")

    # --- Préstamos y Devoluciones ---
    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros_disponibles and id_usuario in self.ids_usuarios:
            libro = self.libros_disponibles.pop(isbn)
            usuario = self.usuarios_registrados[id_usuario]
            usuario.libros_prestados.append(libro)
            print(f"Préstamo realizado: '{libro.datos_inmutables[0]}' a {usuario.nombre}")
        else:
            print("Error: Libro no disponible o usuario no registrado.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.ids_usuarios:
            usuario = self.usuarios_registrados[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Devolución exitosa: '{libro.datos_inmutables[0]}'")
                    return
            print("El usuario no tiene ese libro prestado.")
        else:
            print("Usuario no encontrado.")

    # --- Búsquedas ---
    def buscar_libro(self, criterio):
        # Busca por título, autor o categoría
        resultados = [libro for libro in self.libros_disponibles.values()
                      if criterio.lower() in libro.datos_inmutables[0].lower()
                      or criterio.lower() in libro.datos_inmutables[1].lower()
                      or criterio.lower() in libro.categoria.lower()]

        if resultados:
            print(f"\nResultados para '{criterio}':")
            for r in resultados: print(f" - {r}")
        else:
            print(f"\nNo se encontraron libros para: {criterio}")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            print(f"\nLibros actuales de {usuario.nombre}:")
            if not usuario.libros_prestados:
                print(" Ninguno.")
            for libro in usuario.libros_prestados:
                print(f" - {libro}")
        else:
            print("Usuario no encontrado.")


# ==========================================
# PRUEBA DEL SISTEMA (EJECUCIÓN)
# ==========================================

# 1. Instanciar la biblioteca
mi_biblioteca = Biblioteca()

# 2. Crear libros
l1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "978-01")
l2 = Libro("Breve historia del tiempo", "Stephen Hawking", "Ciencia", "978-02")
l3 = Libro("Python Crash Course", "Eric Matthes", "Programación", "978-03")

# 3. Añadir libros a la biblioteca
mi_biblioteca.añadir_libro(l1)
mi_biblioteca.añadir_libro(l2)
mi_biblioteca.añadir_libro(l3)

# 4. Registrar usuarios
u1 = Usuario("Jorge Caicedo", "U001")
u2 = Usuario("Kiara Ortiz", "U002")
mi_biblioteca.registrar_usuario(u1)
mi_biblioteca.registrar_usuario(u2)

# 5. Realizar préstamos
mi_biblioteca.prestar_libro("978-01", "U001") # Prestar a Ana
mi_biblioteca.prestar_libro("978-03", "U001") # Prestar otro a Ana

# 6. Buscar libros
mi_biblioteca.buscar_libro("Ciencia")
mi_biblioteca.buscar_libro("García Márquez")

# 7. Listar prestados
mi_biblioteca.listar_libros_prestados("U001")

# 8. Devolución
mi_biblioteca.devolver_libro("978-01", "U001")

# 9. Verificar estado final
mi_biblioteca.listar_libros_prestados("U001")
mi_biblioteca.buscar_libro("Cien años") # Debe aparecer de nuevo en disponibles