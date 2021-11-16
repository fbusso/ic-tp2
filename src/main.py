import os.path
import sys
import time

import numpy as np

from src.config import POPULATION_SIZE, NUMBER_OF_GENERATIONS, DRAW_VISUALIZATION, INPUT_FILE, DRAW_CHART
from src.cruza import CruzaBasica, Cruza
from src.data_loading import tamanio_matrices, flujos, distancias
from src.fitness_function import obtener_puntajes_fitness_normalizados, obtener_fitness
from src.generate_population import generar_poblacion_aleatoria
from src.mutacion import Mutacion, MutacionBasica
from src.plot_drawer import PlotDrawer
from src.seleccion import Seleccion, SeleccionTorneo
from src.visualization_drawer import CustomDrawer

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

estrategia_seleccion = Seleccion(selection_algorithm=SeleccionTorneo())
estrategia_mutacion = Mutacion(estrategia=MutacionBasica())
estrategia_cruza = Cruza(crossover_algorithm=CruzaBasica())


def main():
    poblacion = generar_poblacion_aleatoria(tamanio_matrices, POPULATION_SIZE)

    graficador_custom = CustomDrawer()
    graficador = PlotDrawer()

    indices_generacion = []
    resultados_promedio = []
    resultados_minimos = []
    resultados_maximos = []
    ultimo_mejor_cromosoma = []

    def draw_visual_frame():
        graficador_custom.draw_generation_frame(mejor_cromosoma, epoch, mejor_fitness, mejor_cromosoma, flujos,
                                                distancias)
        time.sleep(1)
        return

    def imprimir_epoch():
        print("Epoch: \t\t\t\t\t{}\nFitness Medio: \t\t\t{}\nMejor Fitness: \t\t\t{}\nMejor Cromosoma: \t\t{}\n\n"
              .format(epoch, fitness_medio, mejor_fitness, mejor_cromosoma))

    for epoch in range(NUMBER_OF_GENERATIONS):

        puntajes_fitness = obtener_fitness(poblacion, distancias, flujos)
        puntajes_fitness_normalizados = obtener_puntajes_fitness_normalizados(puntajes_fitness)

        mejor_fitness = np.min(puntajes_fitness)
        min_fitness = np.max(puntajes_fitness)
        fitness_medio = np.mean(puntajes_fitness)

        resultados_maximos.append(mejor_fitness)
        resultados_minimos.append(min_fitness)
        resultados_promedio.append(fitness_medio)
        indices_generacion.append(epoch)

        mejor_cromosoma = poblacion[np.argmin(puntajes_fitness)]
        mejor_cromosoma = list(map(lambda value: value + 1, mejor_cromosoma))

        cromosomas_seleccionados = estrategia_seleccion.select(poblacion, puntajes_fitness_normalizados)
        cromosomas_cruzados = estrategia_cruza.cruza(cromosomas_seleccionados)
        cromosomas_mutados = estrategia_mutacion.mutate(cromosomas_cruzados)

        imprimir_epoch()
        if DRAW_VISUALIZATION and ultimo_mejor_cromosoma != mejor_cromosoma:
            draw_visual_frame()

        ultimo_mejor_cromosoma = mejor_cromosoma

        poblacion = cromosomas_mutados

    if DRAW_CHART:
        graficador.drawPlot(INPUT_FILE, indices_generacion, resultados_promedio, resultados_maximos, resultados_minimos)

    graficador_custom.screen.mainloop()


if __name__ == "__main__":
    main()
