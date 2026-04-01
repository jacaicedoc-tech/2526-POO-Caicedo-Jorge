# ==============================
# Gestión de Tareas con Atajos de Teclado
# Autor: Jorge Caicedo
# ==============================

import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Tareas")
ventana.geometry("400x450")
ventana.resizable(False, False)

# ==============================
# FUNCIONES PRINCIPALES
# ==============================

def añadir_tarea(event=None):
    tarea = entrada_tarea.get()

    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debe escribir una tarea")


def marcar_completada(event=None):
    try:
        indice = lista_tareas.curselection()[0]

        texto = lista_tareas.get(indice)

        # Verificar si ya está completada
        if not texto.startswith("✔ "):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, "✔ " + texto)

            # Cambiar color (feedback visual)
            lista_tareas.itemconfig(indice, fg="gray")

    except:
        messagebox.showwarning(
            "Advertencia",
            "Seleccione una tarea"
        )


def eliminar_tarea(event=None):
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)

    except:
        messagebox.showwarning(
            "Advertencia",
            "Seleccione una tarea"
        )


def cerrar_aplicacion(event=None):
    ventana.destroy()


# ==============================
# INTERFAZ GRÁFICA
# ==============================

# Campo de entrada
entrada_tarea = tk.Entry(
    ventana,
    font=("Arial", 12)
)
entrada_tarea.pack(
    padx=10,
    pady=10,
    fill=tk.X
)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

btn_añadir = tk.Button(
    frame_botones,
    text="Añadir Tarea",
    width=15,
    command=añadir_tarea
)
btn_añadir.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(
    frame_botones,
    text="Marcar Completada",
    width=18,
    command=marcar_completada
)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(
    frame_botones,
    text="Eliminar Tarea",
    width=15,
    command=eliminar_tarea
)
btn_eliminar.grid(row=0, column=2, padx=5)

# Lista de tareas
lista_tareas = tk.Listbox(
    ventana,
    font=("Arial", 12),
    height=15,
    selectbackground="lightblue"
)
lista_tareas.pack(
    padx=10,
    pady=10,
    fill=tk.BOTH,
    expand=True
)

# ==============================
# ATAJOS DE TECLADO
# ==============================

ventana.bind("<Return>", añadir_tarea)
ventana.bind("<c>", marcar_completada)
ventana.bind("<C>", marcar_completada)

ventana.bind("<Delete>", eliminar_tarea)
ventana.bind("<d>", eliminar_tarea)
ventana.bind("<D>", eliminar_tarea)

ventana.bind("<Escape>", cerrar_aplicacion)

# ==============================
# EJECUTAR PROGRAMA
# ==============================

ventana.mainloop()