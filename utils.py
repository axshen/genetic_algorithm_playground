import numpy as np
import random
import sys

def letters():
    alphabet = {i:chr(i + 96) for i in range(1, 27)}
    alphabet[0] = " "
    return alphabet

def phrase_generator(length):
    """
    Generate a random phrase of length from 27 letters
    """
    alphabet = letters()
    phrase = ""
    for i in range(length):
        letter_index = random.randint(0, 26)
        letter = alphabet[letter_index]
        phrase += letter
    return phrase

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

def selection(population, target_phrase, n_selection):
    """
    Selection of population based on fitness score of each generated phrase
    with respect to target phrase
    """
    for item in population:


