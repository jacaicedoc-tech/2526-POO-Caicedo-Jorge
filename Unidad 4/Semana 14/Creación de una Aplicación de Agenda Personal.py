# =========================
# AGENDA PERSONAL
# IMPORTACIÓN DE LIBRERÍAS
# AUTOR JORGE CAICEDO
# =========================
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import json
import os

# =========================
# CLASE PRINCIPAL
# =========================
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("650x400")

        # =========================
        # FRAME: LISTA DE EVENTOS
        # =========================
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10)

        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        self.tree.column("Fecha", width=100)
        self.tree.column("Hora", width=80)
        self.tree.column("Descripción", width=300)

        self.tree.pack()

        # =========================
        # FRAME: ENTRADA DE DATOS
        # =========================
        frame_entrada = tk.Frame(root)
        frame_entrada.pack(pady=10)

        # Fecha
        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.fecha = DateEntry(frame_entrada, date_pattern='yyyy-mm-dd')
        self.fecha.grid(row=0, column=1)

        # Hora
        tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
        self.hora = tk.Entry(frame_entrada)
        self.hora.grid(row=1, column=1)

        # Descripción
        tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.descripcion = tk.Entry(frame_entrada, width=40)
        self.descripcion.grid(row=2, column=1)

        # =========================
        # FRAME: BOTONES
        # =========================
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Mostrar Agenda", command=self.cargar_agenda).grid(row=0, column=2, padx=5)
        tk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=3, padx=5)

    # =========================
    # FUNCIÓN: AGREGAR EVENTO
    # =========================
    def agregar_evento(self):
        fecha = self.fecha.get()
        hora = self.hora.get()
        descripcion = self.descripcion.get()

        if fecha and hora and descripcion:
            # Insertar en la tabla
            self.tree.insert("", "end", values=(fecha, hora, descripcion))

            # Crear evento
            evento = {
                "fecha": fecha,
                "hora": hora,
                "descripcion": descripcion
            }

            # Leer archivo si existe
            if os.path.exists("agenda.json"):
                with open("agenda.json", "r") as f:
                    try:
                        datos = json.load(f)
                    except:
                        datos = []
            else:
                datos = []

            # Agregar evento
            datos.append(evento)

            # Guardar archivo
            with open("agenda.json", "w") as f:
                json.dump(datos, f, indent=4)

            # Limpiar campos
            self.hora.delete(0, tk.END)
            self.descripcion.delete(0, tk.END)

        else:
            messagebox.showwarning("Error", "Completa todos los campos")

    # =========================
    # FUNCIÓN: ELIMINAR EVENTO
    # =========================
    def eliminar_evento(self):
        seleccionado = self.tree.selection()

        if seleccionado:
            confirmar = messagebox.askyesno("Confirmar", "¿Deseas eliminar el evento?")
            if confirmar:
                self.tree.delete(seleccionado)
                # (Nota: opcionalmente también puedes eliminarlo del JSON)
        else:
            messagebox.showwarning("Error", "Selecciona un evento")

    # =========================
    # FUNCIÓN: CARGAR AGENDA
    # =========================
    def cargar_agenda(self):
        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Leer archivo
        if os.path.exists("agenda.json"):
            with open("agenda.json", "r") as f:
                try:
                    datos = json.load(f)

                    for evento in datos:
                        self.tree.insert("", "end", values=(
                            evento["fecha"],
                            evento["hora"],
                            evento["descripcion"]
                        ))
                except:
                    messagebox.showerror("Error", "Archivo dañado")
        else:
            messagebox.showinfo("Info", "No hay eventos guardados")

# =========================
# EJECUCIÓN DEL PROGRAMA
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()