import random

from src.config import MUTATION_PROBABILITY


class Mutacion(object):
    def __init__(self, estrategia):
        self.algoritmo_mutacion = estrategia

    def mutate(self, population):
        return self.algoritmo_mutacion(population)


class MutacionBasica(object):

    def __init__(self):
        pass

    def __call__(self, population):
        return self.mutar_poblacion(population)

    # Se eligen dos genes aleatorios y se los intercambian.
    @staticmethod
    def mutar_poblacion(population):
        resultado = []

        for chromosome in population:
            if 0 <= random.uniform(0, 1) <= MUTATION_PROBABILITY:
                cromosomas_mutados = MutacionBasica.mutate_chromosome(chromosome,
                                                                      MutacionBasica.generar_indices_aleatorios(
                                                                          chromosome))
                resultado.append(cromosomas_mutados)
            else:
                resultado.append(chromosome)

        return resultado

    @staticmethod
    def mutate_chromosome(chromosome, random_indexes):
        gen_a_index, gen_b_index = random_indexes
        chromosome[gen_a_index], chromosome[gen_b_index] = chromosome[gen_b_index], chromosome[gen_a_index]
        return chromosome

    @staticmethod
    def generar_indices_aleatorios(chromosome):
        return random.randint(0, len(chromosome) - 1), random.randint(0, len(chromosome) - 1)
