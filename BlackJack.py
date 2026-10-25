import random

def baraja():
    """
    Función para guardar las cartas de la baraja.
    
    Returns:
    lista (list) : Lista con las posibles cartas del juego.
    """
    lista = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return lista

def calcular_puntos(mano):
    """
    Calcula los puntos totales de una mano de cartas, teniendo en cuenta
    que el As puede valer 11 o 1 si se pasa de 21.
    
    Args:
    mano (list) : Lista de cartas que tiene el jugador o la IA.
    
    Returns:
    puntos (int) : Suma total de puntos de la mano.
    """
    
    valores = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
    }
    puntos = 0
    ases = 0
    for carta in mano:
        puntos += valores[carta]
        if carta == "A":
            ases += 1
            
    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1
        
    return puntos

def mostrar_mesa(manoUser, manoIA, oculta):
    """
    Función que devuelve las cartas y puntos de la partida.
    
    Args:
    manoUser (list) : Cartas del usuario.
    manoIA (list) : Cartas del oponente (banca).
    oculta (bool) : Indica si solo se muestra la primera carta de la IA o todas.
    
    Returns:
    mensaje (str) : Mensaje con las manos y puntos actuales.
    """
    
    puntosUser = calcular_puntos(manoUser)
    mensaje = ""
    if oculta == True:
        mensaje = f"""
Tus cartas: {', '.join(manoUser)} (Puntos: {puntosUser})
Carta visible del rival: {manoIA[0]}
"""
    else:
        puntosIA = calcular_puntos(manoIA)
        mensaje = f"""
Tus cartas: {', '.join(manoUser)} (Puntos: {puntosUser})
Cartas del rival: {', '.join(manoIA)} (Puntos: {puntosIA})
"""
    return mensaje

def comprobar_ganador(puntosUser, puntosIA):
    """
    Compara las puntuaciones finales para mostrar quién gana la partida.
    
    Args:
    puntosUser (int) : Puntos finales del usuario.
    puntosIA (int) : Puntos finales de la IA.
    """
    
    if puntosUser > 21:
        print("Te has pasado de 21. Perdiste")
    elif puntosIA > 21:
        print("El rival se ha pasado de 21. Ganaste")
    elif puntosUser > puntosIA:
        print("Ganaste")
    elif puntosIA > puntosUser:
        print("Perdiste")
    else:
        print("Empate")

def BlackJack():
    """
    Función principal que inicia el bucle del juego de BlackJack
    repartiendo las cartas y llamando a las funciones auxiliares.
    """
    
    manoUser = [random.choice(baraja()), random.choice(baraja())]
    manoIA = [random.choice(baraja()), random.choice(baraja())]
    opciones = ["pedir", "plantarse"]
    while calcular_puntos(manoUser) < 21:
        print(mostrar_mesa(manoUser, manoIA, True))
        eleccion = input("Escoge entre: pedir, plantarse \n").lower()
        if eleccion in opciones:
            if eleccion == "pedir":
                manoUser.append(random.choice(baraja()))
            else:
                break
        else:
            print("Tiene que ser una de las opciones")        
    puntosUser = calcular_puntos(manoUser)
    if puntosUser <= 21:
        while calcular_puntos(manoIA) < 17:
            manoIA.append(random.choice(baraja())) # Jugamos más seguros cuando es la banca.      
    puntosIA = calcular_puntos(manoIA)
    print(mostrar_mesa(manoUser, manoIA, False))
    comprobar_ganador(puntosUser, puntosIA)