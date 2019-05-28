import random
from Chrome_values import value,cost,constraint

class Chromosome:
    """ Create a chromosome class with fitness, cost, and gene
        attributes

        attributes: fitness, cost, gene

    """
    def __init__(self,genes=[],fitness=0,weight=0):
        self.genes = genes
        self.fitness = fitness
        self.weight = weight
    

# Generate gene

    def generate_chrome(self, num_gene=15):
        """generate one random chromosome"""
        genes = []
        for i in range(num_gene):
            gene=random.randint(0,1)
            genes.append(gene)
        self.genes = genes

    def score_value(self,value):
        '''to score one chromosome

        chromosome: list
        '''
        valuelist=[]
        for i in range(len(self.genes)):
            score=value[i]*self.genes[i]
            valuelist.append(score)
        v=sum(valuelist)
        self.fitness = v

    def score_weight(self,cost):
        '''to score one chromosome.
        chromosome: list
        '''
        weightlist=[]
        for i in range(len(self.genes)):
            score=cost[i]*self.genes[i]
            weightlist.append(score)
        w=sum(weightlist)
        self.weight = w

    def is_feasible(self,constraint):
        '''predicate on feasibility, that is values less than constraint'''
        if self.weight < constraint:
            return True
        return False
