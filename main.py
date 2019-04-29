# genetic algorithm implementation to generate randomly chosen phrase from
# random letter generation.

import numpy as np
import random

from utils import *

class GeneticAlgorithm():
    def __init__(self, target, n_population, n_selection, p_mutation):
        self.target = target
        self.n_population = n_population
        self.n_selection = n_selection
        self.p_mutation = p_mutation

    def run(self):
        pop = self.initialise_population()
        _, fittest = self.population_fittest(pop)
        n_generations = 0

        while (fittest < 0.9):
            parents = self.selection(pop)
            children = self.cross(parents)

            pop = self.update_population(parents, children)
            phrase, fittest = self.population_fittest(pop)

            print("Generation: %i" % n_generations)
            n_generations += 1

        print(phrase)

    def initialise_population(self):
        population = []
        for i in range(self.n_population):
            n = len(self.target)
            generated_phrase = phrase_generator(n)
            population.append(generated_phrase)
        return population

    def population_fittest(self, population):
        fitness_values = [fitness(x, self.target) for x in population]
        value = max(fitness_values)
        key = population[fitness_values.index(value)]
        return key, value

    def selection(self, population):
        pairs = []
        surviving_population = self.survival(population)
        while surviving_population:
            try:
                p1 = pop_random(surviving_population)
                p2 = pop_random(surviving_population)
                pair = [p1, p2]
                pairs.append(pair)
            except:
                pass
        return pairs

    def cross(self, pairs):
        children = []
        for pair in pairs:
            n_children = random.randint(3, 6)
            for _ in range(n_children):
                child = crossover(pair[0], pair[1])
                child = mutation(child, self.p_mutation)
                children.append(child)
        return children

    def update_population(self, parents, children):
        updated_pop = []
        for pair in parents:
            updated_pop.append(pair[0])
            updated_pop.append(pair[1])
        updated_pop += children
        if (len(updated_pop) < 2):
            print("Extinction - no population")
            sys.exit()
        return updated_pop

    def survival(self, population):
        fitness_values = np.array([fitness(x, self.target) for x in population])
        fitness_threshold = np.quantile(fitness_values, self.n_selection)
        remaining_population = []
        for item in population:
            if (fitness(item, self.target) > fitness_threshold):
                remaining_population.append(item)
        return remaining_population

def main():

    # user defined constants
    target_phrase = "this work is fun"
    N_POPULATION = int(1e3)
    N_SELECTION = 0.4
    P_MUTATION = 0.05

    genetic_algorithm = GeneticAlgorithm(target_phrase, N_POPULATION, N_SELECTION, P_MUTATION)
    genetic_algorithm.run()

if __name__ == "__main__":
    main()
