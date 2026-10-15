import random

def ppp(eleccion, eleccionIA):
    puntos = {
        ("piedra", "papel") : -1,
        ("piedra", "tijera") : 1,
        ("papel", "tijera") : -1,
        ("papel","piedra") : 1,
        ("tijera", "papel") : 1,
        ("tijera", "piedra"): -1
    }
    resultado = 0
    
    if (eleccion, eleccionIA) in puntos:
        resultado = puntos[eleccion,eleccionIA]
    # metodo get
    # eliminariamos resultado o en su defeco resultado seria igual al get.
    # return puntos.get((eleccion, eleccionIA), 0)
    return resultado  

def pppPuntos(puntosUser,puntosRandom) :
    if puntosRandom == 3 or puntosUser == 3:
        print("FIn del juego.")
    return f"""
Tus puntos: {puntosUser}
Puntos del rival: {puntosRandom}
"""

def piedraPapelTijera():
    puntosRandom = 0
    puntosUser = 0
    opciones = ["piedra", "papel", "tijera"]
    while puntosRandom < 3 and puntosUser < 3:
        eleccion = input("Escoge entre: piedra, papel, tijera \n").lower()
        match eleccion:
            case "piedra" | "papel" | "tijera":
                elecIA = random.choice(opciones)
                print(f"IA: {elecIA}")
                resultado = ppp(eleccion, elecIA)  
                if resultado == 1:
                    print("Ganaste")
                    puntosUser +=1 
                elif resultado == -1:
                    print("Perdiste")
                    puntosRandom +=1  
                else: 
                    print("Empate")
                print(pppPuntos(puntosUser,puntosRandom))  
            case _:
                print("Tiene que ser una de las opciones")               
 