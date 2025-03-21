import sqlite3


"""
# Ejemplo de uso
#create_user("Alice", "alice@mail.com")  # Crear un usuario
#create_user("Wanda", "wanda@mail.com")
#create_user("lola", "lola@mail.com")
print(read_users())  # Ver todos los usuarios
update_user(2, "Alice Updated", "alice_updated@mail.com")  # Actualizar usuario
delete_user(4)  # Eliminar usuario
print(read_users())

"""























conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT, email TEXT)""")
conn.commit()

def crear_usuario(nombre, email):
    cursor.execute("INSERT INTO users (nombre, email,direccion) VALUES (?, ?,?)", (nombre, email))
    conn.commit()

def mostrar_usuarios():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def update_user_email(id, email):
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (email, id))
    conn.commit()

def update_user_direccion(id, direccion):
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (direccion, id))
    conn.commit()

def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
crear_usuario("Alice", "alice@mail.com")
print(mostrar_usuarios())  # Ver todos los usuarios
update_user_email(1, "alice_updated@mail.com")
update_user_direccion(1,"Calle 200")
delete_user(1)

# Cerrar conexión
conn.close()