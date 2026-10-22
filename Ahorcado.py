import random

def lista():
    return [
    "sol", "mar", "luz", "paz", 
    "flor", "gato", "mesa", "nube", "tren", 
    "arbol", "libro", "playa", "reloj", "fuego", 
    "bosque", "camino", "ciudad", "puente", "espejo", 
    "ventana"
]
    
# Falta comprobar que no sea número*
def comprobar(intento, palabra, adivinado, intentos, noEstan):
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
    return f"""
Te quedan: {intentos} intentos
Has usado las siguientes letras: {', '.join(noEstan)}
Palabra: {''.join(adivinado)}
"""
                  
def Ahorcado():
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