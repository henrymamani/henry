import sqlite3
from InquirerPy import inquirer
from tabulate import tabulate
def conexion():
    con=sqlite3.connect("DATABASE/DataBase")
    cur=con.cursor()
    return con, cur
#---Creacion de las tablas---
def creacion(conexion,cursor):
    #--Tabla ceramica--
    agregar="""
    CREATE TABLE IF NOT EXISTS ceramica
    (COD INTEGER PRIMARY KEY NOT NULL,
    MOD TEXT NOT NULL,
    COLOR TEXT NOT NULL,
    USO TEXT NOT NULL,
    TAM TEXT NOT NULL,
    M2_CAJA FLOAT NOT NULL,
    CANT INTEGER NOT NULL);
    """
    cursor.execute(agregar)
    conexion.close()
    print("Tabla creada")

#--Agregrar datos--
def insertar_datos(conexion,cursor,datos):
    if datos==None:
        print("Nose registraron datos")
    sentencia=("INSERT INTO ceramica VALUES (?,?,?,?,?,?,?)")
    cursor.execute(sentencia,datos)
    conexion.commit()
    print("Se agregaron los datos")
    conexion.commit()
    conexion.close()

#--Ver la tabla--
def ver_ceramica(conexion,cursor):
    sentencia="SELECT * FROM ceramica"
    cursor.execute(sentencia)
    #-mostrar en una tabla
    filas=cursor.fetcall()
    columnas=[desc[0] for desc in cursor.description]
    print(tabulate(filas,headers=columnas,tablefmt="fancy_grid"))




