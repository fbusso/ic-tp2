import copy
import random

from src.config import CROSSOVER_PROBABILITY


class Cruza(object):
    def __init__(self, crossover_algorithm):
        self.algoritmo_cruza = crossover_algorithm

    def cruza(self, population):
        return self.algoritmo_cruza(population)


class CruzaBasica(object):

    def __init__(self):
        pass

    def __call__(self, population):
        return self.cruzar(population)

    @staticmethod
    def cruzar(population):
        espcies_no_cruzadas = []
        especies_a_cruzar = []

        CruzaBasica.elegir_cromosomas_a_cruzar(population, espcies_no_cruzadas, especies_a_cruzar)
        tuplas_de_cruza = CruzaBasica.crear_tuplas_de_cruza(espcies_no_cruzadas, especies_a_cruzar)
        especies_cruzadas = CruzaBasica.cruzar_poblacion(tuplas_de_cruza)

        return especies_cruzadas + espcies_no_cruzadas

    @staticmethod
    def cruzar_poblacion(crossover_tuples):
        especies_cruzadas = []

        for tupla_cruzada in crossover_tuples:
            punto_de_cruza = random.randint(0, len(tupla_cruzada) - 1)
            hijo_a, hijo_b = CruzaBasica.cruzar_cromosomas(tupla_cruzada, punto_de_cruza=punto_de_cruza)
            especies_cruzadas.append(hijo_a)
            especies_cruzadas.append(hijo_b)

        return especies_cruzadas

    @staticmethod
    def elegir_cromosomas_a_cruzar(poblacion, especies_no_cruzadas, especies_a_cruzar):
        for cromosoma in poblacion:
            if random.uniform(0, 1) < CROSSOVER_PROBABILITY:
                especies_a_cruzar.append(cromosoma)
            else:
                especies_no_cruzadas.append(cromosoma)

    @staticmethod
    def crear_tuplas_de_cruza(especies_no_cruzadas, especies_a_cruzar):
        tuplas_de_cruza = []
        especies_a_cruzar = list(enumerate(especies_a_cruzar))
        while especies_a_cruzar:
            indice_cromosoma_a_cruzar, cromosoma_a_cruzar = especies_a_cruzar.pop()

            if not especies_a_cruzar:
                especies_no_cruzadas.append(cromosoma_a_cruzar)
                break

            indice_cromosoma_companiero, cromosoma_companiero = random.choice(especies_a_cruzar)
            especies_a_cruzar = list(filter(lambda value: value[0] != indice_cromosoma_companiero, especies_a_cruzar))
            tuplas_de_cruza.append((cromosoma_a_cruzar, cromosoma_companiero))
        return tuplas_de_cruza

    @staticmethod
    def cruzar_cromosomas(padres, punto_de_cruza):
        padre, madre = padres
        hijo_a, hijo_b = copy.copy(padre), copy.copy(madre)

        for indice in range(punto_de_cruza):
            valor_a = hijo_a[indice]
            valor_b = hijo_b[indice]

            indice_valor_b_en_a = hijo_a.index(valor_b)
            indice_valor_a_en_b = hijo_b.index(valor_a)

            hijo_a[indice_valor_b_en_a] = valor_a
            hijo_b[indice_valor_a_en_b] = valor_b

            hijo_a[indice] = valor_b
            hijo_b[indice] = valor_a
        return hijo_a, hijo_b
