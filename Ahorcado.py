import random

def lista():
    return [
    "sol", "mar", "luz", "paz", 
    "flor", "gato", "mesa", "nube", "tren", 
    "arbol", "libro", "playa", "reloj", "fuego", 
    "bosque", "camino", "ciudad", "puente", "espejo", 
    "ventana"
]
def Ahorcado():
    palabra = random.choice(lista())
    adivinado = ""
    adivinados = []
    for i in range(len(palabra)): 
        adivinado +="_"
    intentos = len(palabra)*2
    print(list(palabra))
    print(intentos)
    print(adivinado)
    intento = input("Introduce una letra: \n").lower()
    if len(intento) != 1:
        print("Tiene que ser solo 1 letra") 
    else:
        for i in palabra:
            if intento == i:
                adivinados.append(intento)
                adivinado.replace("_",palabra)
    print(adivinado)
    print(adivinados)
                
    
    
    
Ahorcado()