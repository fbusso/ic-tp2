import numpy as np
import random


class Seleccion(object):
    def __init__(self, selection_algorithm):
        self.algorimo_de_seleccion = selection_algorithm

    def select(self, population, fitness_scores):
        return self.algorimo_de_seleccion(population, fitness_scores)


class SeleccionRuleta(object):

    def __init__(self):
        pass

    def __call__(self, poblacion, puntajes_fitness):
        return self.seleccion(poblacion, puntajes_fitness)

    # Los cromosomas con mayor fitness van a ser seleccionados mas tiempo.
    @staticmethod
    def seleccion(population, lista_puntajes):
        poblacion_nueva = []

        # Elimina el máximo de cada elemento, así la selección ruleta dependerá de una diferencia mayor.
        peor_resultado = np.min(lista_puntajes)
        lista_puntajes = list(map(lambda value: value - peor_resultado, lista_puntajes))

        acumulado = np.cumsum(lista_puntajes)

        for _ in range(len(population)):
            probabilidad_seleccion = random.uniform(0, 1) * sum(lista_puntajes)
            miembro_aleatorio = SeleccionRuleta.elegir_cromosoma(population, acumulado, probabilidad_seleccion)
            poblacion_nueva.append(miembro_aleatorio)

        return poblacion_nueva

    @staticmethod
    def elegir_cromosoma(poblacion, acumulado, probabilidad_aleatoria):
        for indice, _ in enumerate(acumulado):
            if probabilidad_aleatoria <= acumulado[indice]:
                return poblacion[indice]


class SeleccionTorneo(object):

    def __init__(self):
        pass

    def __call__(self, poblacion, puntajes_fitness):
        return self.seleccion_torneo(poblacion, puntajes_fitness)

    @staticmethod
    def seleccion_torneo(poblacion, puntajes_fitness, elitismo=False):
        nueva_especie = []
        tamanio_poblacion = len(puntajes_fitness)
        tamanio_poblacion = tamanio_poblacion - 1 if elitismo else tamanio_poblacion
        for _ in range(0, tamanio_poblacion):

            un_indice = random.randint(0, len(puntajes_fitness) - 1)
            otro_indice = random.randint(0, len(puntajes_fitness) - 1)
            if puntajes_fitness[un_indice] > puntajes_fitness[otro_indice]:
                ganador = poblacion[un_indice]
            else:
                ganador = poblacion[otro_indice]
            nueva_especie.append(ganador)
        return nueva_especie
