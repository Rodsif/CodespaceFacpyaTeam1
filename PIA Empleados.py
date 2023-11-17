import random as rd
import sys
import datetime
import sqlite3
from sqlite3 import Error
import openpyxl

# Nombre ficticio de la empresa
nombre_empresa = "TechCorp"

# Funciones para la creación de tablas y menú

def Crear_Tabla():
    try:
        with sqlite3.connect("RegistroPersonal") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS Empleados (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS Registros (id INTEGER PRIMARY KEY, tipo TEXT NOT NULL, fecha TIMESTAMP, empleado_id INTEGER NOT NULL, FOREIGN KEY(empleado_id) REFERENCES Empleados(id));")
            print("Tablas creadas exitosamente")
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()

Crear_Tabla()

# Opción 1
def registrar_entrada_salida():
    while True:
        nombre_empleado = input(f"Ingresa el nombre del empleado en {nombre_empresa} (o escribe SALIR para regresar al menú):  ")

        if nombre_empleado.upper() == 'SALIR':
            return

        try:
            with sqlite3.connect("RegistroPersonal") as conn:
                mi_cursor = conn.cursor()
                valores = {"nombre": nombre_empleado}
                mi_cursor.execute("SELECT * FROM Empleados WHERE nombre = :nombre", valores)
                registro = mi_cursor.fetchall()

                if registro:
                    for id_empleado, nombre in registro:
                        print(f"ID Empleado: {id_empleado}, Nombre: {nombre} en {nombre_empresa}")
                else:
                    print(f"No se encontró un empleado asociado con el nombre {nombre_empleado} en {nombre_empresa}")

                    # Preguntar si se desea registrar al empleado
                    respuesta = input("¿Deseas registrar a este empleado? (Sí/No): ").upper()

                    if respuesta != 'SÍ':
                        continue

                    # Registrar al empleado
                    try:
                        nuevo_id = rd.randint(1, 999)  # Generar una clave aleatoria para el nuevo empleado
                        mi_cursor.execute("INSERT INTO Empleados (id, nombre) VALUES (?, ?)", (nuevo_id, nombre_empleado))
                        print(f"Empleado {nombre_empleado} registrado con éxito en {nombre_empresa}.")
                    except Error as e:
                        print(e)
                    except Exception:
                        print(f"Surgió una falla al registrar al empleado {nombre_empleado}.")
                    finally:
                        conn.commit()

        except Error as e:
            print(e)
        except Exception:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        else:
            tipo_registro = input("¿Quieres marcar una ENTRADA o SALIDA? ")

            if tipo_registro.upper() not in ['ENTRADA', 'SALIDA']:
                print("Tipo de registro no válido. Debe ser ENTRADA o SALIDA.")
                continue

            fecha_actual = datetime.datetime.now()

            try:
                with sqlite3.connect("RegistroPersonal") as conn:
                    mi_cursor = conn.cursor()
                    Sydney = {"tipo": tipo_registro, "fecha": fecha_actual, "empleado_id": id_empleado}
                    mi_cursor.execute("INSERT INTO Registros (tipo, fecha, empleado_id) VALUES (?, ?, ?)", (tipo_registro, fecha_actual, id_empleado))
                    print(f"Registro de {tipo_registro} realizado con éxito para el empleado {nombre_empleado} en {nombre_empresa}")
            except Error as e:
                print(e)
            except Exception:
                print(f"Surgió una falla siendo esta la causa: {sys.exc_info()[0]}")
            finally:
                if conn:
                    conn.close()


# Opción 2
def revisar_registro():
    while True:
        llave = input(f"Cual es el nombre del empleado en {nombre_empresa} (Escribe SALIR para regresar al menú):  ")
        if llave == 'SALIR':
            return
        try:
            with sqlite3.connect("RegistroPersonal") as conn:
                mi_cursor = conn.cursor()
                valores1 = {"nombre": llave}
                mi_cursor.execute("SELECT * FROM Registros WHERE empleado_id = (SELECT id FROM Empleados WHERE nombre = :nombre)", valores1)
                registro = mi_cursor.fetchall()

                if registro:
                    for id_registro, tipo, fecha, empleado_id in registro:
                        print(f"ID Registro: {id_registro}, Tipo: {tipo}, Fecha: {fecha}, Empleado ID: {empleado_id} en {nombre_empresa}")
                else:
                    print(f"No se encontró un registro asociado con el nombre del empleado {llave} en {nombre_empresa}")
        except Error as e:
            print(e)
        except Exception:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        # ...

# Opción 3
def reporte_a_Excel():
    while True:
        fecha_reporte = input(f"¿De qué fecha quieres sacar el reporte en {nombre_empresa}? (Formato dd-mm-yyyy): ")

        try:
            fecha_parsed = datetime.datetime.strptime(fecha_reporte, "%d-%m-%Y")
        except ValueError:
            print("Error: La fecha ingresada no sigue el formato esperado.")
            continue

        print("*" * 75)
        print(f"** REPORTE DE ENTRADAS Y SALIDAS DE PERSONAL PARA EL DÍA {fecha_parsed.strftime('%d-%m-%Y')} EN {nombre_empresa} **")

        try:
            with sqlite3.connect("RegistroPersonal", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:
                mi_cursor = conn.cursor()
                criterios = {"fecha": fecha_parsed}
                mi_cursor.execute("SELECT Empleados.nombre, Registros.tipo, Registros.fecha FROM Registros JOIN Empleados ON Registros.empleado_id = Empleados.id WHERE DATE(Registros.fecha) = :fecha;", criterios)
                registros = mi_cursor.fetchall()

                if registros:
                    lista = [("Nombre", "Tipo", "Fecha")]

                    for nombre, tipo, fecha in registros:
                        print(f"Nombre: {nombre}, Tipo: {tipo}, Fecha: {fecha}")

                        # Añadir a la lista
                        lista.append((nombre, tipo, fecha))

                    # Crear el archivo Excel
                    wb = openpyxl.Workbook()
                    hoja = wb.active

                    for registro in lista:
                        hoja.append(registro)

                    print("Hoja activa:", hoja.title)
                    nombre_archivo = f'reporte_entradas_salidas_{nombre_empresa.lower()}.xlsx'
                    wb.save(nombre_archivo)

                    print(f"Reporte creado exitosamente. Puedes encontrar el archivo en: {nombre_archivo}")
                    return
                else:
                    print(f"No hay registros de entradas y salidas para la fecha {fecha_parsed.strftime('%d-%m-%Y')} en {nombre_empresa}")
        except Error as e:
            print(e)
        except Exception as ex:
            print(f"Se produjo el siguiente error: {ex}")
        finally:
            if conn:
                conn.close()
                print("Se ha cerrado la conexión")

# Opción 4
def salir_del_programa():
    print("*" * 30)
    print(f"Hasta pronto, que tenga un excelente día en {nombre_empresa}!")
    print("*" * 30)
    print("Vuelve a visitarnos pronto")
    print("*" * 30)
    sys.exit()

# Función principal
def Mi_menú():
    print("Conexión Establecida con " + nombre_empresa)
    Crear_Tabla()
    print("*" * 20)
    print("1. Registrar Entrada o Salida\n"
          "2. Revisar Registro de Empleados\n"
          "3. Reporte de Entradas y Salidas\n"
          "4. Salir")
    print("*" * 20)

    elección = int(input("¿Qué opción deseas realizar?:  "))

    while elección not in [1, 2, 3, 4]:
        print("Opción no válida. Por favor, elige una opción válida.")
        elección = int(input("¿Qué opción deseas realizar?:  "))

    if elección == 1:
        registrar_entrada_salida()
    elif elección == 2:
        revisar_registro()
    elif elección == 3:
        reporte_a_Excel()
    elif elección == 4:
        salir_del_programa()

# Llamada a la función principal
Mi_menú()
