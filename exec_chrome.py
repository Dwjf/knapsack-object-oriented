import random
from Chrome_values import value,cost,constraint
from Chromosome import Chromosome

def main(n,cost,value):
    "Iterate and save best result.Test.Retest"
    optimal = 0
    best_binary=[]
    best_weight = []
    for i in range(n):
        chrome1 = Chromosome()
        chrome1.generate_chrome()
        chrome1.score_weight(cost)
        chrome1.score_value(value)
        if chrome1.is_feasible(constraint):
            if chrome1.fitness>optimal:
                optimal=chrome1.fitness
                best_binary= chrome1.genes
                best_weight = chrome1.weight

    return best_binary,optimal,best_weight

print(main(15000,cost,value))