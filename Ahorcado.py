import random

def lista():
    """
        Función para guardar palabras.
        
        Returns:
        list : Lista con un conjunto de palabras.
    """
    
    return [
    "sol", "mar", "luz", "paz", 
    "flor", "gato", "mesa", "nube", "tren", 
    "arbol", "libro", "playa", "reloj", "fuego", 
    "bosque", "camino", "ciudad", "puente", "espejo", 
    "ventana"
]
    
# Falta comprobar que no sea número*
def comprobar(intento, palabra, adivinado, intentos, noEstan):
    """
    Comprobar si la letra está en la palabra.
    
    Args:
    intento (str): Valor a evaluar.
    palabra (str): Palabra en la que evaluar.
    adivinado (list): Lista de "_" que se va complentando con intentos acertados de la palabra.
    intentos (int): Número de intentos que tiene el usuario para adivinar.
    noEstan (list): Lista para guardas letras que no forman parte de la palabra.
    
    Returns:
    intentos (int) : número de intentos actualizado.
    
    """
    
    if len(intento) != 1:
        print("Tiene que ser solo 1 letra") 
    elif intento in adivinado or intento in noEstan: 
        print("Ya has usado esta palabra")
    elif intento not in palabra:
        intentos = intentos -1
        noEstan.append(intento)
    else:
        for i in range(len(palabra)):
            if palabra[i] == intento:
                adivinado[i] = intento
    
    return intentos

def Mensaje(adivinado,intentos, noEstan):
    """
    Mensaje casual para devolver al usuario como va en la ronda.
        
    Args:
    adivinado (list): Lista que guarda que letras de la palabra ha adivinado el usuario.
    intentos (int): Número de intentos que tiene el usuario para adivinar.
    noEstan (list): Lista para guardas letras que no forman parte de la palabra.
    
    Returns:
    str: Mensaje para el usuario con los intentos, y ambas listas.
    """
    
    return f"""
Te quedan: {intentos} intentos
Has usado las siguientes letras: {', '.join(noEstan)}
Palabra: {''.join(adivinado)}
"""
                  
def Ahorcado():
    """
    Función principal que crea una palabra y ejecuta el bucle principal con ayuda
    de las funciones auxiliares para que el usuario pueda adivinar en un número x de intentos
    la palabra secreta creada de manera aleatoria.
    """
    
    palabra = random.choice(lista())
    adivinado = ["_"] * len(palabra)
    noEstan = []
    intentos = len(palabra)*2
    while intentos > 0:
        print(palabra) # Para poder comprobar el correcto funcionamiento de la función.
        print(Mensaje(adivinado,intentos,noEstan))
        intento = input("Introduce una letra: \n").lower()
        intentos = comprobar(intento, palabra, adivinado, intentos, noEstan)
        if "_" not in adivinado:
            print("Has ganado")
            break
    if "_" in adivinado:
        print(f"Perdiste, la palabra secreta era {palabra}")