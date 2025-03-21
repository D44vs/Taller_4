import sqlite3
import os
import time


conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS Clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL, 
                telefono INTEGER,
                email TEXT ,
                ciudad TEXT ,
                direccion TEXT )""")

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


def create_user(name,telefono,email,ciudad,direccion):
    cursor.execute("INSERT INTO users (name, telefono, email, ciudad, direccion) VALUES (?, ?, ?, ?, ?)", (name,telefono,email,ciudad,direccion))
    conn.commit()

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


def update_user(id, name, email):
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, id))
    conn.commit()

def delete_user(id):
    cursor.execute("DELETE FROM Clientes WHERE id = ?", (id,))
    conn.commit()




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
        os.system("cls")
        if opc == "0":
                cs="."
                for i in range(3):
                        print(f"Cerrando sesión{cs}")
                        cs+="."
                        time.sleep(1)
                        os.system("cls")
                print("Sesión finalizada exitosamente.")
                time.sleep(5)
                break
        elif opc=="1":
                name=input("Ingrese su nombre: ").capitalize()
                telefono=int(input("Ingrese su número de teléfono: "))
                email=input("ingrese su correco electrónico: ")
                ciudad=input("ingrese su ciudad: ")
                direccion=input("ingrese su dirección: ")

                create_user(name,telefono,email,ciudad,direccion)
        elif opc=="2":
                read_users()
                time.sleep(5)
        elif opc=="3":
                id=input
                name=input
                email=input
                update_user(id, name, email)
        elif opc=="4":
                cursor.execute("SELECT * FROM Clientes")
                resultados= cursor.fetchall()
                for fila in resultados:
                    print(f"ID: {fila[0]}", end=" ")
                    print(f"Nombre: {fila[1]}")
                    print("-"*20)
                id=input("Ingrese el ID del usuario que desea eliminar: " )
                delete_user(id)
        else:
                print("""              
                                *************************
                                *Al parecer ha ingresado*
                                *una opción incorrecta  *
                                *************************
                        """)

conn.close()


