#CREACIÓN DE UNA BASE DE DATOS CON DOS TABLAS RELACIONADAS UNO A MUCHOS
import random as rd
import sys
import datetime
import sqlite3 
from sqlite3 import Error
from datetime import(date,
                                   datetime,
                                   timedelta)
import openpyxl
#Crea una tabla en SQLite3



def Crear_Tabla ():
     try:
        with sqlite3.connect("CoworkingLTI") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NO EXIST Usuarios (clave INTERGER PRIMARY KEY, nombre TEXT NOT NULL);")
            mi_cursor.execute("CREATE TABLE IF NO EXIST Salas (clave INTERGER PRIMARY KEY, nombre TEXT NOT NULL, capacidad INTERGER NOT NULL);")
            mi_cursor.execute("CREATE TABLE IF NO EXIST Reservaciones (folio INTERGER PRIMARY KEY, nombre TEXT NOT NULL, horario text NOT NULL, fecha timestamp)  ")
            print("Tablas creadadas exitosamente")
     except Error as e:
         print (e)
     except:
         print(f"se produjo el siguiente errror: {sys.exc_info()[0]}")
     finally:
         conn.close()

Crear_Tabla ()

# Opcion 1
def Registrar_Reservacion ():
    while True:
        valor_clave = int(input("Cual es tu clave de cliente:  "))
        try:
            with sqlite3.connect("CoworkingLTI") as conn:
                mi_cursor = conn.cursor()
                valores = {"clave": valor_clave}
                mi_cursor.execute("Select * FROM Usuarios WHERE clave = clave", valores)
                registro = mi_cursor.fetchall()

                if registro:
                    for clave, nombre in registro:
                        print(f"{clave}\{nombre}")
                else:
                        print(f"No se encontró un proyecto asociado con la clave {valor_clave}")
        except Error as e:
            print (e)
        except:
            print(f"se produjo el siguiente errror: {sys.exc_info()[0]}")  
        else:
            Nombre = input("Ingresa el nombre de la reservación (Escribre SALIR para regresar al menú): ")
            if Nombre == '':
                continue
            elif Nombre == 'SALIR':
                return
            else:
                Horario = input("¿Cual es el horario que quieres? [M, V, N]: ")
                print(Horario)
                Fecha_Ingresada= input("Ingresa la fecha de reservación: ")
                Fecha_dt = datetime.strptime(Fecha_Ingresada, '%d/%m/%Y')
                fecha_actual = datetime.today()
                fecha_permitida = datetime.now() + timedelta ( days = 2)
                if Fecha_dt < fecha_permitida:
                    print("Debes hacer la reservacion con 2 dias de anticipación.")
                else:
                    nivel = rd.randint(1,99)
                    try:
                        with sqlite3.connect("CoworkingLTI") as conn:
                            mi_cursor = conn.cursor()
                            Miami={"folio":nivel, "nombre":Nombre,"horario":Horario,"fecha":Fecha_dt}
                            mi_cursor.execute("INSERT INTO  Reservaciónes VALUES( :folio, :nombre, :horario, :fecha)",Miami)
                            #print("El folio es ")
                            #print(nivel)
                            #print("El nombre es ")
                            #print(Nombre)
                    except Error as e:
                        print (e)
                    except:
                        print(f"Surgio una falla siendo esta la causa: {sys.exc_info()[0]}")
                    finally:
                        if (conn):
                            conn.close()
                            fecha_consultar = input("Confirma la fecha (dd/mm/aaaa):  ")
                            fecha_consultar =datetime.strptime(fecha_consultar, "%d/%m/%Y").date()
                            print("¡Reservacion Realizada con Exito!")
                            try:
                                with sqlite3.connect("CoworkingLTI", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:
                                    mi_cursor = conn.cursor()
                                    criterios ={"fecha": fecha_consultar}
                                    mi_cursor.execute("SELECT folio, nombre, horario, fecha FROM Reservaciones WHERE DATE(fecha) = (:fecha);", criterios)
                                    #mi_cursors.execute("SELECT clave, nombre, fecha_registro FROM Amigo WHERE DATE(fecha_registro) >= :fecha;", criterios)
                                    registros = mi_cursor.fetchall()

                                    for clave, nombre, fecha_registro, fecha in registros:
                                        print(f"Clave ={clave}, tipo de dato {type(clave)}")
                                        print(f"Nombre = {nombre}, tipo de dato {type(nombre)}")
                                        print(f"Horario = {fecha_registro}, tipo de dato {type(fecha_registro)}")
                                        print(f"Fecha =  {fecha}, tipo de dato {type(fecha)}")
                                    for clave, nombre, fecha_registro, fecha in registros:
                                        print("Clave\t" + "Nombre \t"+ " Turno\t" + "              Fecha\t")
                                        print(f"{clave}\t {nombre}\t {fecha_registro}\t {fecha}\t")
                                        return   
                                        
                            except sqlite3.Error as e:
                                print (e)
                            except Exception:
                                print(f"se produjo el siguiente errror: {sys.exc_info()[0]}")
                            finally:
                                 if (conn):
                                     conn.close()
                                     print("Se ha cerrado la conexión")

#Opcion 2      
def modificar_descripciones ():
    while True:
        llave = input("Cual es el nombre de tu sala actual:  ")
        try:
            with sqlite3.connect("CoworkingLTI") *as conn:
                mi_cursor = conn.cursor()
                valores1 = {"nombre":llave}
                mi_cursor.execute("SELECT * FROM Reservaciones WHERE nombre = nombre", valores1)
                registro = mi_cursor.fetchall()

                if registro:
                    for folio, nombre, horario, fecha in registro:
                        print("Clave\t" + "Nombre\t" + "Turno\t" + "              Fecha\t")
                        print(f"{folio}\t{nombre}\t{horario}\t{fecha}")
                else:
                    print(f"No se encontró un proyecto asociado con la clave {llave}")
        except Error as e:
              print (e)
        except:
              print(f"se produjo el siguiente errror: {sys.exc_info()[0]}")
        else:
            nuevo_nombre = input("A que nombre lo quieres cambiar?: ")
            id_number = folio
            Turno = horario
            fecha_dt = fecha
            try:
                with sqlite3.connect("CoworkingLTI") as conn:
                    mi_cursor = conn.cursor()
                    Sydney = {"folio":id_number, "nombre":nuevo_nombre, "turno":Turno, "fecha":fecha_dt}
                    mi_cursor.execute("UPDATE Reservaciones SET nombre = ( :nombre) WHERE (folio) = (:folio);", Sydney)
                    print("Modificacion realizada con exito. ")
                    return
            except Error as e:
                print (e)
            except:
                print(f"Surgio una falla siendo esta la causa:  {sys.exc_info()[0]}")



    
                





 
