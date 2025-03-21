import os
import sqlite3
import time

base=sqlite3.connect("Usuarios.db")

def Crear():
        pass
def Mostrar():
        pass
def Editar():
        pass
def Eliminar():
        pass

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
                Crear()
        elif opc=="2":
                Mostrar()
        elif opc=="3":
                Editar()
        elif opc=="4":
                Eliminar()
        else:
                print("""              
                                *************************
                                *Al parecer ha ingresado*
                                *una opción incorrecta  *
                                *************************
                        """)







#1. Actualizar datos
#2. Modificar correo electrónico
#3. Modificar datos de usuario