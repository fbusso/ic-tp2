import numpy as np


# El objetivo del problema de asignación cuadrática es asignar n edificios a n localizaciones de tal forma de
# minimizar el costo
#
# El costo se calcula como la suma, sobre todos los pares, del flujo de personas entre cada par de
# edificios, multiplicado por la distancia entre ellos.

def obtener_fitness(poblacion, distancias, flujos):
    tamanio = distancias.shape[0]
    puntajes_fitness = []
    for cromosoma in poblacion:
        # Verifica que no haya repetidos.
        assert len(cromosoma) == len(set(cromosoma))
        suma_fitness_cromosoma = 0
        for x in range(tamanio):
            for y in range(tamanio):
                suma_fitness_cromosoma += distancias[x, y] * flujos[cromosoma[x] - 1, cromosoma[y] - 1]
        puntajes_fitness.append(suma_fitness_cromosoma)

    return puntajes_fitness


def obtener_puntajes_fitness_normalizados(puntajes_fitness):
    mapear_a_minimizacion = list(map(lambda value: 1. / value, puntajes_fitness))
    resultados_normalizados = np.array(mapear_a_minimizacion) / np.sum(mapear_a_minimizacion)
    return resultados_normalizados
