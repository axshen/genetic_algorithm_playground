# genetic algorithm implementation to generate randomly chosen phrase from
# random letter generation.

import numpy as np
import random

from utils import *

def main():

    # user defined constants
    N_POPULATION = 100
    N_SELECTION = 0.4
    P_MUTATION = 0.05

    # initialisation
    population = []

    # target
    target_phrase = "this work is fun"
    n = len(target_phrase)
    generated_phrase = phrase_generator(n)
    fitness_score = fitness(genserated_phrase, target_phrase)
    print(fitness_score)


if __name__ == "__main__":
    main()
