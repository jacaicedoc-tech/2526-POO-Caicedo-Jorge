# ============================================================
# APLICACIÓN GUI: LISTA DE TAREAS
# Autor: (Jorge Caicedo)
# Descripción:
# Aplicación gráfica en Tkinter que permite:
# - Añadir tareas
# - Marcar tareas como completadas
# - Eliminar tareas
# - Manejar eventos como Enter y doble clic
# ============================================================

# Importamos la librería Tkinter
import tkinter as tk
from tkinter import messagebox

# ============================================================
# Clase principal de la aplicación
# ============================================================

class ListaTareasApp:

    def __init__(self, root):
        """
        Constructor de la clase.
        Inicializa la ventana principal y los componentes GUI.
        """

        # Ventana principal
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x450")

        # Lista interna para almacenar tareas
        self.tareas = []

        # ====================================================
        # CAMPO DE ENTRADA
        # ====================================================

        # Etiqueta
        self.label = tk.Label(root, text="Escribe una nueva tarea:")
        self.label.pack(pady=5)

        # Campo Entry
        self.entry_tarea = tk.Entry(root, width=40)
        self.entry_tarea.pack(pady=5)

        # Evento ENTER para añadir tarea
        self.entry_tarea.bind("<Return>", self.agregar_tarea)

        # ====================================================
        # BOTONES
        # ====================================================

        # Botón Añadir
        self.btn_agregar = tk.Button(
            root,
            text="Añadir Tarea",
            command=self.agregar_tarea
        )
        self.btn_agregar.pack(pady=5)

        # Botón Marcar completada
        self.btn_completar = tk.Button(
            root,
            text="Marcar como Completada",
            command=self.marcar_completada
        )
        self.btn_completar.pack(pady=5)

        # Botón Eliminar
        self.btn_eliminar = tk.Button(
            root,
            text="Eliminar Tarea",
            command=self.eliminar_tarea
        )
        self.btn_eliminar.pack(pady=5)

        # ====================================================
        # LISTBOX PARA MOSTRAR TAREAS
        # ====================================================

        self.listbox = tk.Listbox(
            root,
            width=45,
            height=15,
            selectbackground="lightblue"
        )

        self.listbox.pack(pady=10)

        # Evento doble clic para completar tarea
        self.listbox.bind("<Double-Button-1>", self.marcar_completada)

    # ========================================================
    # FUNCIONES PRINCIPALES
    # ========================================================

    def agregar_tarea(self, event=None):
        """
        Agrega una nueva tarea a la lista.
        Puede activarse con botón o tecla ENTER.
        """

        tarea = self.entry_tarea.get()

        # Verificar que no esté vacía
        if tarea != "":

            # Agregar tarea a lista interna
            self.tareas.append({
                "texto": tarea,
                "completada": False
            })

            # Mostrar en Listbox
            self.listbox.insert(tk.END, tarea)

            # Limpiar campo
            self.entry_tarea.delete(0, tk.END)

        else:
            messagebox.showwarning(
                "Advertencia",
                "No puedes agregar una tarea vacía."
            )

    # ========================================================

    def marcar_completada(self, event=None):
        """
        Marca una tarea como completada.
        Cambia su apariencia visual.
        """

        try:
            # Obtener índice seleccionado
            indice = self.listbox.curselection()[0]

            # Cambiar estado interno
            self.tareas[indice]["completada"] = True

            texto = self.tareas[indice]["texto"]

            # Mostrar tarea como completada
            self.listbox.delete(indice)
            self.listbox.insert(indice, "✔ " + texto)

            # Cambiar color visual
            self.listbox.itemconfig(
                indice,
                fg="gray"
            )

        except IndexError:
            messagebox.showwarning(
                "Advertencia",
                "Selecciona una tarea primero."
            )

    # ========================================================

    def eliminar_tarea(self):
        """
        Elimina una tarea seleccionada.
        """

        try:
            indice = self.listbox.curselection()[0]

            # Eliminar visualmente
            self.listbox.delete(indice)

            # Eliminar internamente
            del self.tareas[indice]

        except IndexError:
            messagebox.showwarning(
                "Advertencia",
                "Selecciona una tarea para eliminar."
            )

# ============================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================

if __name__ == "__main__":

    # Crear ventana principal
    root = tk.Tk()

    # Crear aplicación
    app = ListaTareasApp(root)

    # Ejecutar interfaz
    root.mainloop()