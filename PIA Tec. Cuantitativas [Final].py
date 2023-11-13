# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 23:36:41 2023

@author: Rots
"""

def convertir_base(numero, base_origen, base_destino):
    decimal = int(str(numero), base_origen)
    resultado = ""
    while decimal > 0:
        digito = decimal % base_destino
        resultado = str(digito) + resultado
        decimal //= base_destino
    return resultado

def menu_conversion():
    while True:
        print("*************************************************************************************")
        print("************             Seleccione la opción de conversión:             ************")
        print("                                                                                   ")
        print("                         1. Convertir de base 7 a base 19                   ")
        print("                                                                                   ")
        print("                         2. Convertir de base 21 a base 9                   ")
        print("                                                                                ")
        print("                         3. Convertir de base 13 a base 5                   ")
        print("                                                                                   ")
        print("                         4. Salir                                                              ")
        print("                                                                                  ")
        print("*************************************************************************************")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            numero_base7 = input("Ingrese el número en base 7: ")
            resultado = convertir_base(numero_base7, 7, 19)
            print(f"Resultado de la conversión: {resultado}")
            
        elif opcion == "2":
            numero_base21_a_base9 = input("Ingrese el número en base 21: ") 
            resultado2 = convertir_base(numero_base21_a_base9, 21, 9)
            print(f"Base 21 a Base 9: {resultado2}")
            
        elif opcion == "3":
            numero_base13_a_base5 = input("Ingrese el número en base 13: ")
            resultado3 = convertir_base(numero_base13_a_base5, 13, 5)
            print(f"Base 13 a Base 5: {resultado3}")

        elif opcion == "4":
            print("Saliendo del programa.")
            break  # Salir del bucle principal al seleccionar la opción "4"
        
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")
            
        # Preguntar al usuario si desea realizar otra conversión
        otra_conversion = input("¿Desea realizar otra conversión? (Sí/No): ")
        if otra_conversion.lower() != "si":
            print("Saliendo del programa.")
            break  # Salir del bucle principal si el usuario no desea realizar otra conversión

# Ejecutar el menú
menu_conversion()