import tkinter as tk
from tkinter import simpledialog

import customtkinter 
root = customtkinter.CTk()


#customtkinter.set_appearance_mode("dark")
#customtkinter.set_default_color_theme("dark-blue")

def obtener_nombre():
    nombre = simpledialog.askstring("Ingresar Nombre", "Por favor, ingrese su nombre:")
    if nombre:
        saludo = f"Hola, {nombre}!"
        resultado_label.config(text=saludo)

# Crear una instancia de la clase Tk
root = tk.Tk()
root.title("Programa de Saludo")

# Crear un botón que al hacer clic, solicitará el nombre del usuario
boton_obtener_nombre = tk.Button(root, text="Obtener Nombre", command=obtener_nombre)
boton_obtener_nombre.pack(pady=20)

# Crear una etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=10)

# Iniciar el bucle principal de Tkinter
root.mainloop()
