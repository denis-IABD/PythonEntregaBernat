from PiedraPapelTijera import piedraPapelTijera

def main():
    while True:
        eleccion = input("""
            Menú: Escoja una opción númerica
            
1. Piedra papel tijera  
2. Ahorcado
3. Tres en raya  
4. BlackJack
5. Salir \n
""")
        match eleccion:
            case "1":
                piedraPapelTijera()
            case "5":
                print("Adiós...")
                break
            case _:
                print("Tiene que ser un número")

try :
    main()
except KeyboardInterrupt:
    print("Has parado el programa.")   