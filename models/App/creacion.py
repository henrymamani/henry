import sqlite3
from InquirerPy import inquirer
from tabulate import tabulate
def conexion():
    #con=sqlite3.connect('registro.db')
    con=sqlite3.connect('C:/Users/HP/OneDrive/Desktop/Mi primier proyecto/models/App/registro.db')
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
    

#--Ver la tabla--
def ver_ceramica(conexion):
    curs=conexion.cursor()
    sentencia="SELECT * FROM ceramica"
    curs.execute(sentencia)
    #-mostrar en una tabla
    filas=curs.fetchall()
    columnas=[desc[0] for desc in curs.description]
    print(tabulate(filas,headers=columnas,tablefmt="fancy_grid"))

#--verifica si un dato ya existe
def ver_existe(conexion,co):
        cursor=conexion.cursor()
        sentencia=f"SELECT EXISTS(SELECT 1 FROM ceramica WHERE cod={co})"
        cursor.execute(sentencia)
        existe=cursor.fetchone()[0]
        
        if existe:
            print("dato encontrado")
            return True
        else:
            return False
#--Actualizar datos (cantidad)--
def actualizar_datos(conexion,cursor,can,co):
    sentencia=f"UPDATE ceramica set cant='{can}' WHERE cod ={co}"
    cursor.execute(sentencia)
    conexion.commit()
    print("Dato actualizado")
    return True

#--Modificar datos--

#--Modelo--
def ver_modelo(conexion,cod):
    cursor=conexion.cursor()
    sentencia=f"SELECT mod FROM ceramica WHERE cod={cod}"
    cursor.execute(sentencia)
    fila=cursor.fetchone()
    if fila:
        return fila[0]
    else:
        return None

#--Actualizar Modelo
def actualizar_modelo(conexion,cursor,mod1,co):
    sentencia=f"UPDATE ceramica set mod='{mod1}' WHERE cod={co}"
    cursor.execute(sentencia)
    conexion.commit()
    print("Modelo actualizado")
    return True

#--Color--
def ver_color(conexion,co):
    cursor=conexion.cursor()
    sentencia=f"SELECT color FROM ceramica WHERE cod={co}"
    cursor.execute(sentencia)
    fila=cursor.fetchone()
    if fila:
        return fila[0]
    else:
        return None
    
#--Actualizar Color
def actualizar_color(conexion,cursor,col1,co):
    sentencia=f"UPDATE ceramica set color='{col1}' WHERE cod={co}"
    cursor.execute(sentencia)
    conexion.commit()
    print("Color actualizado")
    return True

#--Uso
def ver_uso(conexion,co):
    cursor=conexion.cursor()
    sentencia=f"SELECT uso FROM ceramica WHERE cod={co}"
    cursor.execute(sentencia)
    fila=cursor.fetchone()
    if fila:
        return fila[0]
    else:
        return None
    
#--Actualizar Uso
def actualizar_uso(conexion,cursor,uso1,co):
    sentencia=f"UPDATE ceramica set uso='{uso1}' WHERE cod={co}"
    cursor.execute(sentencia)
    conexion.commit()
    print("Tipo de Uso actualizado")
    return True

#--tamanio
def ver_tamanio(conexion,co):
    cursor=conexion.cursor()
    sentencia=f"SELECT tam FROM ceramica WHERE cod={co}"
    cursor.execute(sentencia)
    fila=cursor.fetchone()
    if fila:
        return fila[0]
    else: 
        return None
    
#--Actualizar tamanio
def actualizar_tamanio(conexion,cursor,tam1,co):
    sentencia=f"UPDATE ceramica set tam='{tam1}' WHERE cod={co}"
    cursor.execute(sentencia)
    conexion.commit()
    print("Tamanio actualizado")
    return True

#--m2_caja
def ver_m2_caja(conexion,cursor,co):
    sentencia=f"SELECT m2_caja FROM ceramica WHERe cod={co}"
    cursor.execute(sentencia)
    fila=cursor.fetchone()
    if fila:
        return fila[0]
    else:
        return None
#--Actualizar_m2_caja
def actualizar_m2_caja(conexion,cursor,m2_caja1,co):
    sentencia=f"UPDATE ceramica set m2_caja='{m2_caja1}' WHERE cod={co}"
    cursor.execute(sentencia)
    conexion.commit()
    print("m2 actualizado")
    return True

#--Cantidad
def ver_cantidad(conexion,co):
    cursor=conexion.cursor()
    sentencia=f"SELECT cant FROM ceramica WHERE cod={co}"
    cursor.execute(sentencia)
    fila=cursor.fetchone()
    if fila:
        return fila[0]
    else:
        return None
    
if __name__=="__main__":
    con,cur=conexion()
    ver_ceramica(con)
    creacion(con,cur)

