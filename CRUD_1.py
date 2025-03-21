# Se importa las librearias correspondentes
import sqlite3
import os
import time

# Se crea conexion con la base de datos, si no existe la crea con ese nombre y extension 
conn = sqlite3.connect("database.db")
cursor = conn.cursor() # se crea objeto para interactuar con la base de datos

#Se crea tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS Clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL, 
                telefono INTEGER,
                email TEXT ,
                ciudad TEXT ,
                direccion TEXT )""")
conn.commit()

# En caso que mi tabla este vacia, se agregan los datos. En caso que no simplemente continua con normalidad
clientes = [
        (1, "Juan", 3000000000, "email@test.com", "Bucaramanga", "Cra 33 # 24 - 12"),
        (2, "Ana", 3100000000, "ana@test.com", "Bogotá", "Calle 45 # 20 - 30"),
        (3, "Luis", 3200000000, "luis@test.com", "Medellín", "Av. Poblado # 10 - 50"),
        (4, "María", 3300000000, "maria@test.com", "Cali", "Calle 5 # 15 - 60"),
        (5, "Carlos", 3400000000, "carlos@test.com", "Barranquilla", "Carrera 50 # 70 - 25")
]
try:
        cursor.executemany("INSERT INTO Clientes (ID, name, telefono, email, ciudad, direccion) VALUES (?, ?, ?, ?, ?, ?)", clientes)
except:
        pass

conn.commit()

#funcion para crear usuario
def create_user(name,telefono,email,ciudad,direccion):
        cursor.execute("INSERT INTO Clientes (name, telefono, email, ciudad, direccion) VALUES (?, ?, ?, ?, ?)", (name,telefono,email,ciudad,direccion))

#funcion para mostrar los usuarios
def read_users():
        cursor.execute("SELECT * FROM Clientes")
        resultados=cursor.fetchall()
        if resultados:
                print("Datos en la tabla 'Clientes':")
                for fila in resultados:
                        print(f"ID: {fila[0]}")
                        print(f"Nombre: {fila[1]}")
                        print(f"Teléfono: {fila[2]}")
                        print(f"Email: {fila[3]}")
                        print(f"Ciudad: {fila[4]}")
                        print(f"Dirección: {fila[5]}")
                        print("-" * 30)
        else:
                print("No hay clientes par mostrar.")

#funciones para actualizar los datos de los usuarios-------
def update_user(i_d):
        telefono=int(input("Ingrese el numero de telefono: "))
        email=input("Ingrese el nuevo correo: ")
        ciudad=input("Ingrese la nueva ciudad: ")
        direccion=input("Ingrese la nueva direccion: ")
        cursor.execute("UPDATE Clientes SET telefono = ?, email = ?, ciudad = ?, direccion= ? WHERE id = ?", (telefono,email,ciudad,direccion,i_d))
        conn.commit()

def mod_telefono(i_d):
        telefono=int(input("Ingrese el numero de telefono: "))
        cursor.execute("UPDATE Clientes SET telefono=? WHERE id = ?", (telefono,i_d))
        conn.commit()

def mod_email(i_d):
        email=input("Ingrese el nuevo correo: ")
        cursor.execute("UPDATE Clientes SET email=? WHERE id = ?", (email,i_d))
        conn.commit()
#----------------------------------------------------------

# Eliminacion de usuarios
def delete_user(id):
        cursor.execute("DELETE FROM Clientes WHERE id = ?", (id,))




while True:
        opc = input("""
                Hola y bienvenido, a continuación usted podrá realizar las 
                siguientes acciones:
                
                        1. Crear usuario
                        2. Mostrar usuarios
                        3. Actualizar Usuarios
                        4. Eliminar usuarios
                        0. Salir
                
                Su opción: """)
        os.system("cls") # Cada "os.system("cls")" es para limpiar la consola y tener respuestas mas limpias
        if opc == "0":
                # Simplemente quise que finalizar el proceso se viera mas estetico
                cs="."
                for i in range(3):
                        print(f"""                                        ******************{'*'*i}
                                        *Cerrando sesión{cs}*
                                        ******************{'*'*i}""")
                        cs+="."
                        time.sleep(2)
                        os.system("cls")
                print("""                                        *********************************                                      
                                        *Sesión finalizada exitosamente.*
                                        *********************************""")
                time.sleep(5)
                break
        elif opc=="1":
                #Solicito los datos del nuevo usuario para crearlo en la funcion
                name=input("Ingrese su nombre: ").capitalize()
                telefono=int(input("Ingrese su número de teléfono: "))
                email=input("ingrese su correco electrónico: ")
                ciudad=input("ingrese su ciudad: ")
                direccion=input("ingrese su dirección: ")
                create_user(name,telefono,email,ciudad,direccion)
        elif opc=="2":
                #Mustra los usuarios
                read_users()
                input("Presione 'Enter' para continuar.")
        elif opc=="3":
                #Primero pregunto lo que desea editar antes de pasar a editarlo por separado
                # Tambien pregunto el id 
                i_d=int(input("Ingrese el ID del usuario: "))
                opc2=input("""
                        
                        1. Modificar Telefono de un usuario.
                        2. Modificar Email de un usuario.
                        3. Modificar datos personales de un usuario.
                        
                Su opcion: """)
                print()
                if opc2=="1":
                        mod_telefono(i_d)
                elif opc2=="2":
                        mod_email(i_d)
                elif opc2=="3":
                        update_user(i_d)
                else:
                        print("Opcion erronea")
                # update_user(id, name, email)
        elif opc=="4":
                #Elimina el usuario, tambien muestra los usuarios disponibles de manera resumida
                cursor.execute("SELECT * FROM Clientes")
                resultados= cursor.fetchall()
                for fila in resultados:
                        print(f"ID: {fila[0]}", end=" ")
                        print(f"Nombre: {fila[1]}")
                        print("-"*20)
                id=input("\nIngrese el ID del usuario que desea eliminar: " )
                delete_user(id)
        else:# En caso de ingresar una opcion no valida muestra el mensaje a continuacion
                print("""              
                                *************************
                                *Al parecer ha ingresado*
                                *una opción incorrecta  *
                                *************************
                        """)
        os.system("cls")
        conn.commit()
conn.close()#Cierra la base de datos


