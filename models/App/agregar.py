import sqlite3
from InquirerPy import inquirer
from creacion import conexion, insertar_datos,ver_ceramica, ver_existe, actualizar_datos
from creacion import ver_modelo, actualizar_modelo,ver_color,actualizar_color,ver_uso,actualizar_uso,ver_tamanio,actualizar_tamanio,ver_m2_caja,actualizar_m2_caja,ver_cantidad
con,cur=conexion()
class incio:
    #--Menu--
    def principal():
        op=inquirer.select(message="MENU PRINCIPAL",choices=["1.Agregar","2.Ver Stock","3.Calculadora","4.Modificar","5.Salir"],default="1.Agregar").execute()
        if op=="1.Agregar":
            Ceramica.Agregar()
        elif op=="2.Ver Stock":
            Stock.stock()
        elif op=="3.Calculadora":
            Ventas.calculadora()
        elif op=="4.Modificar":
            Modificar.modificar()
        else:
            seguir=inquirer.select(message="Seguro que quiere salir?",choices=["Si","No"]).execute()
            if seguir=="No":
                incio.principal()

class Ceramica:
    cod:int
    mod:str
    color:str
    uso:str
    tam:str
    m2_caja:float
    can:float
    #--Pide los datos
    def Agregar():
            try:
                cod=int(input("Ingrese el codigo: "))
                mod=input("Ingrese modelo: ")
                color=input("Ingrese color: ")
                uso=inquirer.select(message="Tipo de uso: ",choices=["pared","piso"]).execute()
                tam=input("ingrese el tamaño de la ceramica: ")
                m2_caja=float(input("ingrese el metro cuadrado de una caja: "))
                can=int(input("Ingrese la cantidad que se recibio: "))
                print("\nSe agrego con exito\nCodigo: ",cod,". Modelo: ",mod,". Tipo de uso: ",uso,". Tamaño: ",tam,". M2_caja: ",m2_caja,". Color: ",color,". Cantidad: ",can)
                dat=(cod,mod,color,uso,tam,m2_caja,can)
                if ver_existe(con,cod)==True:
                    actualizar_datos(con,cur,can,cod)
                else:
                    insertar_datos(con,cur,dat)
                incio.principal()
            except ValueError:
                print("En el codigo, cantidad debe colocar numeros")
class Stock:
    cod:int
    mod:str
    color:str
    clbre:str
    can:float

    #--muestra la tabla de ceramica
    def stock():
        #aqui va la funcion de difuso o fuzz
        ver_ceramica(con)
        incio.principal()

class Ventas:
    cod:int
    mod:str
    color:str
    clbre:str
    can:float

    #--Calculadora--
    def calculadora(): 
        m2_area=float(input("Ingrese los m^2 de area para cubrir: "))
        m2_caja=float(input("Ingrese los m^2 de la caja: "))
        cajas=m2_area/m2_caja
        print(f"Total de cajas para cubrir: {cajas:.2f}")
        incio.principal()

class Modificar:
    codigo:int
    mod:str
    mod1:str
    color:str
    color1:str
    uso:str
    uso1:str
    tam:str
    tam1:str
    m2_caja:float
    m2_caja1:float
    can:float
    def modificar_codigo():
        try:
            codigo=int(input("ingrese el codigo de la ceramica a modificar: "))
            return codigo
        except ValueError:
            print("Debe ingresar un numero")
    def modificar():
    #--Menu de modificar
        try:
            codigo=Modificar.modificar_codigo()
            if ver_existe(con,codigo)==True:
                op=inquirer.select(message="Elija el atributo a modificar del codigo"+f"{codigo} ",choices=["1.Modelo","2.Color","3.Uso","4.Tamanio","5.m2_caja","6.cantidad","7.Salir"],default="1.Modelo").execute()
                if(op=="1.Modelo"):
                    print("El modelo anterior es: ",ver_modelo(con,codigo))
                    mod1=input("Ingrese el nuevo Modelo: ")
                    actualizar_modelo(con,cur,mod1,codigo)
                    Modificar.modificar()
                elif op=="2.Color":
                    print("El Color anterior es: ",ver_color(con,codigo))
                    color1=input("Ingrese el color nuevo: ")
                    actualizar_color(con,cur,color1,codigo)
                    Modificar.modificar()
                elif op=="3.Uso":
                    print("El tipo de Uso anterior es: ",ver_uso(con,codigo))
                    uso1=inquirer.select(message="Ingrese el nuevo tipo de Uso ",choices=["pared","piso"],default="1.Pared").execute()
                    if uso1=="pared":
                        actualizar_uso(con,cur,uso1,codigo)
                    else:
                        actualizar_uso(con,cur,uso1,codigo)
                    Modificar.modificar()
                elif op=="4.Tamanio":
                    print("El tamanio anterior es: ",ver_tamanio(con,codigo))
                    tam1=input("Ingrese el nuevo tamanio: ")
                    actualizar_tamanio(con,cur,tam1,codigo)
                    Modificar.modificar()
                elif op=="5.m2_caja":
                    print("El metro ^2 de una caja es: ",ver_m2_caja(con,cur,codigo))
                    m2_caja1=input("Ingrese el nuevo metro cuadrado de una caja: ")
                    actualizar_m2_caja(con,cur,m2_caja1,codigo)
                    Modificar.modificar()
                elif op=="6.cantidad":
                    print("La cantidad anterior es: ",ver_cantidad(con,codigo))
                    can1=float(input("Ingrese la nueva cantidad: "))
                    actualizar_datos(con,cur,can1,codigo)
                    Modificar.modificar()
                elif op=="7.Salir":
                    re=inquirer.select(message="Seguro que quiere salir: ",choices=["1.Si","2.No"]).execute()
                    if re=="1.Si":
                        incio.principal()
                    else:
                        Modificar.modificar()
            else:
                print("El codigo de la ceramica no tiene registros")
                incio.principal()
        except ValueError:
            print("En el codigo debe ingresar solo numeros")
incio.principal()
