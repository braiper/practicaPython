import sqlite3

conexion=sqlite3.connect('tabla.db')
consulta=conexion.cursor()
tabla="CREATE TABLE tabla(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"\
    "nombre VARCHAR(30) NOT NULL," \
    "autor VARCHAR (40) NOT NULL,"\
    "year INTEGER(9) NOT NULL);"

print (tabla)

if(consulta.execute(tabla)):
    print('La tabla fue creada')
else:
    print('La tabla no fue creada')

consulta.close()
conexion.commit()
conexion.close()