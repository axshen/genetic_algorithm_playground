import numpy as np
import random
import sys

def letters():
    alphabet = {i:chr(i + 96) for i in range(1, 27)}
    alphabet[0] = " "
    return alphabet

def letter_generator():
    """
    Random letter generation (alphabet + space).
    """
    alphabet = letters()
    letter_index = random.randint(0, 26)
    letter = alphabet[letter_index]
    return letter

def phrase_generator(length):
    """
    Generate a random phrase of length from 27 letters
    """
    alphabet = letters()
    phrase = ""
    for i in range(length):
        letter = letter_generator()
        phrase += letter
    return phrase

def crossover(p1, p2):
    """
    For the time being we'll use the simplest version of crossover for text
    which is to take some fraction of the genes from the first and the remainder
    from the second phrase.
    """
    n = len(p1)
    crossover_point = random.randint(0, n)
    child = ""
    for i in range(n):
        if (i < crossover_point - 1):
            child += p1[i]
        else:
            child += p2[i]
    return child

def mutation(phrase, probability):
    n = len(phrase)
    out_phrase = ""
    for i in range(n):
        p_activation = random.random()
        if (p_activation < probability):
            new_letter = letter_generator()
            out_phrase += new_letter
        else:
            out_phrase += phrase[i]
    return out_phrase

def fitness(phrase, truth):
    """
    Fitness of generated phrase based on known truth phrase (score
    based on letter similarity)
    """
    phrase_letters = list(phrase)
    truth_letters = list(truth)
    n_phrase_letters = len(phrase_letters)
    n_truth_letters = len(truth_letters)
    score = 0

    if (n_phrase_letters != n_truth_letters):
        print("Error: phrases not the same length")
        sys.exit()
    else:
        for i in range(n_phrase_letters):
            if (phrase_letters[i] == truth_letters[i]):
                score += 1
        score = float(score / n_phrase_letters)
    return score

def pop_random(lst):
    """
    Randomly select and remove item from population
    """
    idx = random.randrange(0, len(lst))
    return lst.pop(idx)
