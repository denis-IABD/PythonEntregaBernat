def CrearTablero():
    lista = []
    for i in range(3):
        lista2 = ["_"]*3
        lista.append(lista2)
    return lista
 
def PedirNum(x):
    resultado = -1
    while resultado == -1:
        try:      
            y = int(input(f"Introduce la {x} dondé quieras colocar tu ficha(1,3): \n")) -1
            if y >= 3 or y < 0:
                print("Tiene que ser un número del 1 al 3")
            else:
                resultado = y
        except ValueError:
            print("Tiene que ser un número")
    return resultado    
 
def Comprobar(tablero, ficha):
    fila = False
    diagonal, diagonal2 = 0,0
    comprobado = False
    for i in range(3):
        if len(set(tablero[i])) == 1 and tablero[i][0] == ficha:
            fila = True
        if tablero[i][i] == ficha:
            diagonal +=1
        if tablero[i][2-i] == ficha:
            diagonal2 += 1
        columnas = 0
        for y in range(3):
            if tablero[y][i] == ficha:
                columnas +=1
            if columnas == 3:
                fila = True    
    if diagonal == 3 or diagonal2 == 3 or fila == True:
        comprobado = True
    return comprobado
            
def TresEnRaya():
    tablero = CrearTablero()
    turno = 1
    while True:
        ficha = "X" if turno % 2 else "O"
        for lista in tablero:
            print(" | ".join(lista))
        fila = PedirNum("fila")
        columna = PedirNum("columna")
        if tablero[fila][columna] != "_":
            print("Ya hay una ficha aqui.")
        else:
            tablero[fila][columna] = ficha
            turno +=1
            if turno >= 5:
                comprobado = Comprobar(tablero, ficha)
                ganador = "Jugador 1" if ficha == "X" else "Jugador 2"
                if comprobado == True:
                    print(f"Final del juego, ganador {ganador}")
                    break
                elif turno == 10:
                    print("Se acabó el juego, empate.")
                    break
    for lista in tablero:
        print(" | ".join(lista))

# Contra usuario( 2 personas no hay randoms )