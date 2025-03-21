import sqlite3

misql=sqlite3.connect("waos.db")
cursor=misql.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXIST Clientes(
    ID INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL,
    Edad INTEGER
)
''')
print("Hsta aquí se crea una tabla si no existe")
misql.commit()
misql.close()