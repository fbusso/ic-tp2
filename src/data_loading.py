import os

import numpy as np

from src.config import INPUT_FILE


def leer_matriz(matrix_file) -> np.ndarray:
    matriz = []
    contador_filas = 0
    while contador_filas < tamanio_matrices:
        linea = matrix_file.readline()
        assert isinstance(linea, str)
        if not linea.isspace():
            contador_filas += 1
            fila = [int(valor) for valor in linea.split(sep=' ') if valor != '']
            matriz.append(fila)
    return np.array(matriz)


with open(os.path.join('../res', 'data', INPUT_FILE), mode='r') as archivo:
    tamanio_matrices = int(archivo.readline())
    distancias = leer_matriz(archivo)
    flujos = leer_matriz(archivo)
