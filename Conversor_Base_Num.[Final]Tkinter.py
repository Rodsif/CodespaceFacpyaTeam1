import tkinter as tk
from tkinter import simpledialog

def convertir_base(numero, base_origen, base_destino):
    decimal = int(str(numero), base_origen)
    resultado = ""
    while decimal > 0:
        digito = decimal % base_destino
        resultado = str(digito) + resultado
        decimal //= base_destino
    return resultado

def realizar_conversion():
    opcion = variable_opcion.get()
    
    if opcion == 1:
        numero_base7 = entry_numero.get()
        resultado = convertir_base(numero_base7, 7, 19)
        label_resultado.config(text=f"Resultado de la conversión: {resultado}")
        
    elif opcion == 2:
        numero_base21_a_base9 = entry_numero.get() 
        resultado2 = convertir_base(numero_base21_a_base9, 21, 9)
        label_resultado.config(text=f"Base 21 a Base 9: {resultado2}")
        
    elif opcion == 3:
        numero_base13_a_base5 = entry_numero.get()
        resultado3 = convertir_base(numero_base13_a_base5, 13, 5)
        label_resultado.config(text=f"Base 13 a Base 5: {resultado3}")

def mostrar_ventana_entrada():
    numero = simpledialog.askstring("Ingresar Número", "Por favor, ingrese el número:")
    if numero:
        entry_numero.delete(0, tk.END)  # Limpiar la entrada actual
        entry_numero.insert(0, numero)  # Mostrar el número ingresado

# Crear una instancia de la clase Tk
root = tk.Tk()
root.title("Programa de Conversión de Bases")

# Crear una variable de control para la opción seleccionada
variable_opcion = tk.IntVar()

# Crear widgets
label_numero = tk.Label(root, text="Número:")
entry_numero = tk.Entry(root)
label_opcion = tk.Label(root, text="Seleccione la opción de conversión:")
radio_opcion1 = tk.Radiobutton(root, text="Convertir de base 7 a base 19", variable=variable_opcion, value=1)
radio_opcion2 = tk.Radiobutton(root, text="Convertir de base 21 a base 9", variable=variable_opcion, value=2)
radio_opcion3 = tk.Radiobutton(root, text="Convertir de base 13 a base 5", variable=variable_opcion, value=3)
button_ingresar_numero = tk.Button(root, text="Ingresar Número", command=mostrar_ventana_entrada)
button_convertir = tk.Button(root, text="Realizar Conversión", command=realizar_conversion)
label_resultado = tk.Label(root, text="Resultado de la conversión:")

# Organizar widgets en la ventana
label_numero.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
entry_numero.grid(row=0, column=1, padx=5, pady=5)
button_ingresar_numero.grid(row=0, column=2, padx=5, pady=5)
label_opcion.grid(row=1, column=0, columnspan=3, pady=10)
radio_opcion1.grid(row=2, column=0, columnspan=3, pady=5)
radio_opcion2.grid(row=3, column=0, columnspan=3, pady=5)
radio_opcion3.grid(row=4, column=0, columnspan=3, pady=5)
button_convertir.grid(row=5, column=0, columnspan=3, pady=10)
label_resultado.grid(row=6, column=0, columnspan=3, pady=5)

# Iniciar el bucle principal de Tkinter
root.mainloop()
