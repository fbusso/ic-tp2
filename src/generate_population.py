import random


def generar_poblacion_aleatoria(number_of_objects, number_of_random_chromosomes):
    poblacion = []
    for _ in range(number_of_random_chromosomes):
        cromosoma_aleatorio = list(range(number_of_objects))
        random.shuffle(cromosoma_aleatorio)
        poblacion.append(cromosoma_aleatorio)
    return poblacion
