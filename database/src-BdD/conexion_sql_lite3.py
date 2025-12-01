import sqlite3
from InquirerPy import inquirer
def conectar():
    con=sqlite3.connect("DATABASE/DataBase")
    #Agrega debe argegar nuevos matriales a la tabla de Stock 
    cur=con.cursor()
    return con, cur
    #crear(con,cur)
def crear(conexion,cursor):
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
    #Stock 
    #Vamos a usar la misma tabla 
    # de agregar pero para lectura
    ventas="""
    CREATE TABLE IF NOT EXISTS ventas
    (COD INTEGER PRIMARY KEY NOT NULL,
    M2_AREA FLOAT NOT NULL,
    M2_CAJA FLOAT NOT NULL,
    CANT_VENT INTEGER NOT NULL,
    TOTL FLOAT NOT NULL);
    """
    cursor.execute(agregar)
    cursor.execute(ventas)
    conexion.close()
    print("tabla creada")

def Agregar():
    try:
        cod=int(input("Ingrese el codigo: "))
        mod=input("Ingrese modelo: ")
        color=input("Ingrese color: ")
        uso=inquirer.select(message="Tipo de uso",choices=["pared","piso"]).execute()
        tam=input("ingrese el tamaño de la ceramica")
        m2_caja=float(input("ingrese el metro cuadrado de una caja"))
        can=int(input("Ingrese la cantidad que se recibio: "))
        print("\nSe agrego con exito\nCodigo: ",cod,". Modelo: ",mod,". Tipo de uso: ",uso,". Tamaño: ",tam,". M2_caja: ",m2_caja,". Color: ",color,". Cantidad: ",can)
        dat=(cod,mod,color,uso,tam,m2_caja,can)
        return dat
    except ValueError:
        print("En el codigo, cantidad debe colocar numeros")
        return None

def InsertarDatos(conexion,cursor,datos):
    if datos==None:
        print("No se ingresaron datos por un error al llenar los datos")
    #sentencia="INSERT INTO ceramica(COD,MOD,COLOR,USO,TAM,M2_CAJA,CANT) VALUES(123,'CELMI','Rojo','Pared','42*42',1.55,100)"
    sentencia="INSERT INTO ceramica VALUES(?,?,?,?,?,?,?)"
    cursor.execute(sentencia,datos)
    #cursor.execute(sentencia)
    conexion.commit()
    print("se agregaron los datos")
    conexion.close()
con,cur=conectar()
datos=Agregar()
InsertarDatos(con,cur,datos)
#conectar()