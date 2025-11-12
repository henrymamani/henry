from InquirerPy import inquirer
from agregar import Ceramica, Stock, Ventas
class incio:
    #--Menu--
    def principal():
        op=inquirer.select(message="MENU PRINCIPAL",choices=["1.Agregar","2.Ver Stock","3.Calculadora","4.Salir"],default="1.Agregar").execute()
        if op=="1.Agregar":
            Ceramica.Agregar()
        elif op=="2.Ver Stock":
            Stock.stock()
        elif op=="3.Calculadora":
            Ventas.calculadora()
        else:
            segui=inquirer.select(message="Seguro que quiere salir?",choices=["Si","No"]).execute()
            if segui=="No":
                Ceramica.principal()

          

          