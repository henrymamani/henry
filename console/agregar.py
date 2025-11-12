from InquirerPy import inquirer
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
                uso=inquirer.select(message="Tipo de uso",choices=["pared","piso"]).execute()
                tam=input("ingrese el tamaño de la ceramica")
                m2_caja=float(input("ingrese el metro cuadrado de una caja"))
                can=int(input("Ingrese la cantidad que se recibio: "))
                print("\nSe agrego con exito\nCodigo: ",cod,". Modelo: ",mod,". Tipo de uso: ",uso,". Tamaño: ",tam,". M2_caja: ",m2_caja,". Color: ",color,". Cantidad: ",can)
                dat=(cod,mod,color,uso,tam,m2_caja,can)
                Ceramica.principal()
            except ValueError:
                print("En el codigo, cantidad debe colocar numeros")
class Stock:
    cod:int
    mod:str
    color:str
    clbre:str
    can:float

    def Stock():
        #aqui va la funcion de difuso o fuzz

        Ceramica.principal()

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
        Ceramica.principal()

Ceramica.principal()  
