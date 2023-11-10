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
            with sqlite3.connect("CoworkingLTI") as conn:
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

#opcion 3
def consulta_fecha():
    fecha_consultar = input ("Dime una fecha (dd/mm/aaaa):  ")
    fecha_dt = datetime.strptime(fecha_consultar, '%d/%m/Y%')

    try:
        with sqlite3.connect("CoworkingLTI", detect_types= sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES ) as conn:
            mi_cursor = conn.cursor()
            criterios ={"fecha": fecha_consultar}
            mi_cursor.execute("SELECT folio, nombre, horario, fecha FROM Reservaciones WHERE DATE(fecha) = (:fecha);", criterios)
            registros = mi_cursor.fetchall()

            for folio, nombre, horario, fecha in registros:
                print (f'Estas son las fechas ocupadas {fecha.date}')
    except Exception as e:
        print (e)
    except Exception:
       print(f"Se produjo el siguiente errror:  {sys.exc_info()[0]}")
    finally:
        if (conn):
            conn.close()
            print("se ha cerrado la conexión")



#Opcion 4
def reporte_a_Excel ():
    while True:
        fecha_reporte = input("¿De que fecha quieres sacar el reporte?  ")
        fecha_reporte = datetime.strptime(fecha_reporte, "%d/%m%Y")
        print("*"* 75)
        print("**                     REPORTE DE RESERVACIONES PARA EL DIA", fecha_reporte, "             **")
        try:
            with sqlite3.connect("CoworkingLTI", detect_types= sqlite3.PARSE_DECLTYPES  | sqlite3.PARSE_COLNAMES) as conn:
                  mi_cursor = conn.cursor()
                  criterios ={"fecha": fecha_reporte}
                  mi_cursor.execute("SELECT folio, nombre, horario, fecha FROM Reservaciones WHERE fecha = :fecha", criterios)
                  registrados = mi_cursor.fetchall()

                  if registrados:
                      for folio, nombre, horario, fecha in registrados:
                           print("Clave\t" + "Nombre\t" + " Turno\t" +"                        Fecha\t")
                           print(f"{folio}\t{nombre}\t{horario}\t{fecha}")
                           lista = []
                           lista.append (folio, nombre, horario, fecha)
                           print(lista)
                           wb = openpyxl.Workbook()
                           hoja = wb.active
                           hoja = wb.active

                           for listas in lista:
                               hoja.append(listas)
                           print(f'Hoja activa: {hoja.title}')
                           hoja["A1"] = 10
                           a1 = hoja["A1"]
                           print(a1.value)
                           wb.save('productos.xlsx')
                  else:
                           print(f"No se encontró un proyecto asociado con la clave {fecha_reporte}")
                           return
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

#Opcion 5
def Registrar_sala ():
    while True:
        SALA = input("Como se va a llamar la sala? (Escribe SALIR para regresar al menú):  ")
        if SALA=='':
            break
        elif SALA=='SALIR':
            return
        else:
            capacity = int(input("Cual va a ser la capacidad?:  "))
            N = rd.randint(1,99)
            try:
                with sqlite3.connect("CoworkingLTI") as conn:
                    mi_cursor = conn.cursor()
                    Valores5={"clave": N, "nombre": SALA, "capacidad":capacity }
                    mi_cursor.execute("INSERT INTO Salas (clave, nombre, capacidad) VALUES (:clave, :nombre, :capacidad)", Valores5)
                    print("Sala Registrada!")
                    print("Tu clave de la Sala es la siguiente:  ")
                    print(N)
            except Error as e:
                print (e)
            except:
                print(f"Surgio una falla siendo esta la causa:   {sys.exc_info()[0]}")
            finally:
                if (conn):
                    conn.close()

#Opcion 6
def Registrar_Cliente ():
    while True:
        Usuario=input("Ingresa al usuario (Escribe SALIR para regresar al menú):  ")
        n = rd.randint(1,99)
        if Usuario=='':
            break
        elif Usuario=='SALIR':
            return
        else:
            try:
                with sqlite3.connect("CoworkingLTI") as conn:
                    mi_cursor = conn.cursor()
                    valores={"clave": n, "nombre": Usuario}
                    mi_cursor.execute("INSERT INTO Usuarios (clave, nombre,) VALUES (:clave, :nombre)", valores)
                    print("Usuario Registrado!")
                    print("Tu clave de cliente es la siguiente:  ")
                    print(n)
            except Error as e:
                print (e)
            except:
                print(f"Surgio una falla siendo esta la causa:   {sys.exc_info()[0]}")
            finally:
                if (conn):
                    conn.close()

#Opcion7
def salir_del_programa ():
     print ("*"*30)
     print ("Hasta pronto, que tenga un excelente día!")
     print ("*"*30)
     print ("Vuelve a visitarnos pronto")
     print ("*"*30)

#Opcion8
def eliminar_reservacion ():
    while True:
        key_code = int(input("Dime tu clave de cliente:  "))
        try:
             with sqlite3.connect("CoworkingLTI") as conn:
                    mi_cursor = conn.cursor()
                    valores = {"clave":key_code}
                    mi_cursor.execute("SELECT *  FROM Usuarios WHERE clave =:clave", valores)
                    registro = mi_cursor.fetchall()
                    
                    if registro:
                        for clave, nombre, in registro:
                            print(f"{clave}\t{nombre}")
                    else:
                     print(f"No se encontró un proyecto asociado con la clave {key_code}")
        except Error as e:
                print (e)
        except:
                print(f"Se produjo el siguiente error:   {sys.exc_info()[0]}")
        else:
            id_sala = input("¿Cual es le id de la sala que quieres eliminar?  (Escribe SALIR para regresar al programa):  ")
            if id_sala =='':
                continue
            elif id_sala == 'SALIR':
                return
            else:
                Name = input("¿Cual era tu nombre de evento?:  ")
                Turno = input("Escribe tu horario:  ")
                fecha_asignada = input("Por favor ingrese la fecha:  ")
                fecha_dt = datetime.strptime(fecha_asignada, '%d/%m%Y')
                fecha_permitida = datetime.now() + timedelta ( days = 3)
                if fecha_dt < fecha_permitida:
                    print("No se puede cancelar, debido a que las cancelaciónes deben ser con 3 días de anticipación")
                else:
                    try:
                        with sqlite3.connect("CoworkingLTI") as conn:
                            mi_cursor = conn.cursor()
                            delete = {"folio":id_sala, "nombre":Name, "horario":Turno, "fecha":fecha_dt}
                            mi_cursor.execute("DELETE FROM Reservaciones WHERE folio = :folio;", delete)
                            #delete={"folio":id_sala, "nombre":Name, "horario":Turno, "fecha":fecha_dt}
                            #mi_cursor.execute("DELETE FROM Reservaciones WHERE folio = :folio;", delete)
                            print("Reservacion eliminada. ¡Lamentamos que hayas decidido cancelar tu evento!")
                            return
                    except Error as e:
                     print (e)
                    except Exception:
                     print(f"Se produjo el siguiente error:   {sys.exc_info()[0]}")
        finally:
                if (conn):
                    conn.close()
                    print("Se ha cerrado la conexión")

def exportar_base_de_datos_a_excel ():
    while True:
        wb = openpyxl.Workbook()
        hoja = wb.active
        print(f'Hoja activa: {hoja.title}')
        hoja.append(('Clave', 'Nombre'))
        hoja["B1"] = 86
        hoja["B2"] = "Rodrigo S."
        print("Excel creado correctamente")
        break



    
                
def Mi_menú ():
      print("Conexión Establecida")
      #EstablecerConexión ()
      Crear_Tabla ()
      print("*" * 20)
      print("1. Registra la reservación\n"
          "2. Modificar las descripciones de la reservación\n" +
          "3. Consulta la fecha disponible\n" +
          "4. Reporte de las reservaciones de una fecha\n" + 
          "5. Registrar Sala\n" +
          "6. Registrar Cliente\n" +
          "7. Salir del programa\n"+
          "8. Eliminar Reservacion \n"+ 
          "9. Exportar base de datos a Excel \n")
while True:
                try:
                    Opcion = int(input("Seleccione el numero de la accion que quiere realizar \n:"))
                except Error as e:
                    print(e)
                except:
                    print(f"Ocurruió un problema {sys.exc_info()[0]}")
                else:
                    if Opcion == 1:
                        Registrar_Reservacion ()
                    elif Opcion == 2:
                        modificar_descripciones ()
                    elif Opcion == 3:
                        consulta_fecha ()
                    elif Opcion == 4:
                        reporte_a_Excel ()
                    elif Opcion == 5:
                        Registrar_sala ()
                    elif Opcion == 6:
                        Registrar_Cliente
                    elif Opcion == 7:
                        salir_del_programa ()
                    elif Opcion == 8:
                      eliminar_reservacion
                    elif Opcion == 9:
                     exportar_base_de_datos_a_excel ()
                    else:
                        print("Eso no esta disponible en el menú, le recomiendo revisarlo de nuevo")




Mi_menú ()


# Reservacion
# Disponibilidad
# Modificar
# Eliminar
# Reporte
# Reporte en Excel
#  Sala
# Cliente
# Salir
#
    
                        
        




 