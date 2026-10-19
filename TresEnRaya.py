def CrearTablero():
    lista = []
    numero = 1
    for i in range(3):
        lista2 = []
        for x in range(3):
            lista2.append(numero)
            numero +=1
        lista.append(lista2)
    return lista
            
def TresEnRaya():
    for lista in CrearTablero():
        print(i for i in lista)
    
TresEnRaya()

# Contra usuario( 2 personas no hay randoms )