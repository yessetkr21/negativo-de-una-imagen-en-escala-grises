import random
def crearMatriz():
    matriz = []
    for i in range(8):
        fila = []
        for j in range(8):
            fila.append(random.randint(0, 255))
        matriz.append(fila)
    return matriz

def RestarMatrizInverso(matriz):
    for i in range(8):
        for j in range(8):
            matriz[i][j] = 255 - matriz[i][j]
    return matriz

def mostrarMatriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("{:<5}".format(elemento), end="")
        print()

matriz = crearMatriz()
print("Matriz original:")
mostrarMatriz(matriz)
print("")
print("Matriz multiplicada por el inverso:")
MULTIPLICADA = RestarMatrizInverso(matriz)
mostrarMatriz(matriz)
