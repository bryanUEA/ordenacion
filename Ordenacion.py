def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def ordenar_fila(matriz, indice_fila):
    # Se utiliza el algoritmo Bubble Sort para ordenar la fila
    n = len(matriz[indice_fila])
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if matriz[indice_fila][j] > matriz[indice_fila][j + 1]:
                matriz[indice_fila][j], matriz[indice_fila][j + 1] = matriz[indice_fila][j + 1], matriz[indice_fila][j]

# Definir una matriz
matriz = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]

# Imprimir la matriz original
print("Matriz Original:")
imprimir_matriz(matriz)

# Índice de la fila a ordenar (0-indexado)
fila_a_ordenar = 1

# Ordenar la fila específica
ordenar_fila(matriz, fila_a_ordenar)

# Imprimir la matriz con la fila ordenada
print("\nMatriz con la Fila Ordenada:")
imprimir_matriz(matriz)
