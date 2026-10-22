from PiedraPapelTijera import piedraPapelTijera
from Ahorcado import Ahorcado
from TresEnRaya import TresEnRaya
from BlackJack import BlackJack
def menu():
    return f"""
         Menú: Escoja una opción númerica
            
1. Piedra papel tijera  
2. Ahorcado
3. Tres en raya  
4. BlackJack
5. Salir \n
"""

def main():
    while True:
        eleccion = input(menu())
        if eleccion == "1":
            piedraPapelTijera()
        elif eleccion == "2":
            Ahorcado()
        elif eleccion == "3":
            TresEnRaya()
        elif eleccion == "4":
            BlackJack()
        elif eleccion == "5":
            print("Adiós...")
            break
        else:
            print("Tiene que ser un número de 1 al 5")

try :
    main()
except KeyboardInterrupt:
    print("Has parado el programa.")   