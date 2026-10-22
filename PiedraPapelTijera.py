import random



def elegir_ronda(eleccion, eleccionIA):
    """
    Función que compara 2 elecciones para devolver puntos.
    
    Args:
    eleccion (str) : Elección del usuario1.
    eleccionIA (str) : Elección del usuario2.
    
    Returns:
    resultado (int) : 1 punto al usuario1, -1 punto al usuario2, 0 no puntos para ninguno.
    """
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
    # Fuente: https://thedataschools.com/python/diccionarios/get-metodo-diccionario.html
    return resultado  

def mostrar_puntos(puntosUser,puntosRandom) :
    """
        Función que devuelve los puntos de la partida. Además imprime fin del juego si acaba.
        
        Args:
        puntosUser (int) : Puntos del usuario.
        puntosRandom (int) : Puntos del oponente.
        
        Returns:
        str : El número de puntos por usuario.
    """
    
    if puntosRandom == 3 or puntosUser == 3:
        print("Fin del juego.")
    return f"""
Tus puntos: {puntosUser}
Puntos del rival: {puntosRandom}
"""

def piedraPapelTijera():
    """
    Inicia el bucle principal del juego de Piedra, Papel o Tijera 
    llamando a las funciones auxiliares.
    El juego termina cuando un jugador alcanza los 3 puntos.
    """
    puntosRandom = 0
    puntosUser = 0
    opciones = ["piedra", "papel", "tijera"]
    while puntosRandom < 3 and puntosUser < 3:
        eleccion = input("Escoge entre: piedra, papel, tijera \n").lower()
        if eleccion in opciones:
            elecIA = random.choice(opciones)
            print(f"IA: {elecIA}")
            resultado = elegir_ronda(eleccion, elecIA)  
            if resultado == 1:
                print("Ganaste")
                puntosUser +=1 
            elif resultado == -1:
                print("Perdiste")
                puntosRandom +=1  
            else: 
                print("Empate")
            print(mostrar_puntos(puntosUser,puntosRandom))  
        else:
            print("Tiene que ser una de las opciones")