import numpy as np


# El objetivo del problema de asignación cuadrática es asignar n edificios a n localizaciones de tal forma de
# minimizar el costo
#
# El costo se calcula como la suma, sobre todos los pares, del flujo de personas entre cada par de
# edificios, multiplicado por la distancia entre ellos.

def compute_fitness_scores_list(population, distance_matrix, flow_matrix):
    matrices_size = distance_matrix.shape[0]
    fitness_scores_list = []
    for chromosome in population:
        assert len(chromosome) == len(set(chromosome))
        chromosome_fitness_sum = 0
        for x in range(matrices_size):
            for y in range(matrices_size):
                chromosome_fitness_sum += distance_matrix[x, y] * flow_matrix[chromosome[x] - 1, chromosome[y] - 1]
        fitness_scores_list.append(chromosome_fitness_sum)

    return fitness_scores_list


def get_normalized_result_of_fitness_function_scores_list(fitness_scores_list):
    map_to_minimization_problem = list(map(lambda value: 1. / value, fitness_scores_list))
    normalized_results = np.array(map_to_minimization_problem) / np.sum(map_to_minimization_problem)
    return normalized_results
