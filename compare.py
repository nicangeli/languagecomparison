#!/usr/bin/env python3
""" Python module for fitness calculations according to http://www.linguistics.ucla.edu/people/stabler/LeeEtAl2005Grammar.pdf """

#These modifications put stuff in functions for easier reuse.

import itertools
import numpy
import random

def similarity_measure(language1, language2):
    """Calculate the language similarity for two languages.

    Representing a language as a sequence, the similarity between
    languages i and j, denoted a_ij, is defined as the proportion of
    parameters on which the two individuals agree. For example, the
    language similarity between an individual i whose language is
    represented as AAA and an individual j whose language is represented
    as ABA is a_ij=2/3."""

    # The following line also accepts an array of languages for
    # language2. This is not obvious, but it works, and I'll explain
    # the details next time we meet, if you want me to.
    return (language1==language2).sum()/len(language1)
    
def fitness(language, population, f0=1e-3):
    """Calculate the fitness of a language in a given population.

    The overall fitness of an individual, f_i, is described as

    f_i = f_0 + sum_j a_ij

    with a_ij calculated using similarity_measure"""

    return f0 + similarity_measure(
        language,
        numpy.asarray(population)) / len(population)

def one_each_population(length, n_values):
    """Generate a population that contains every language precisely once.
    """
    population=[]

    all_languages = itertools.product(
        range(n_values),
        repeat=lengthofsequence)
    for pairing in all_languages: 
        population.append(list(pairing))

    return population

def mutation(population,lengthofsequence,numberofvalues,mutationrate):
    index1=random.randrange(0,len(population))
    index2=random.randrange(0,len(population))
    population[index1]=population[index2]
    randomnumber=random.random()
    if randomnumber<mutationrate:        
        parametertochange=random.randrange(0,lengthofsequence)
        valuetochange=random.randrange(0,numberofvalues)
        population[index2][parametertochange]=valuetochange

    return population


# Simulation parameters
lengthofsequence = 1
numberofvalues = 64



for y in numpy.arange(0.5, 1.02, 0.02): 
    population = one_each_population(lengthofsequence, numberofvalues)

    for x in range(0,1000):
        population=mutation(population,lengthofsequence,numberofvalues,y)
    for language in population:
        print (language)
    for language in population:
        f = fitness(language, population)
        print("{0} = {1}".format(language, f))


    print(y)