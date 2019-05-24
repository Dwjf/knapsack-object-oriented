import random

class Chromosome:
    """Class for chromosome
    
    attributes: gene,value,weight
    """
def is_feasible(c,constraint):
    '''predicate on feasibility, that is values less than constraint'''
    if c.weight < constraint:
        return True
    return False

constraint = 200000
value = [
    44090,49643,248559,23209,307481,
    3936,87956,106463,143994,312835,
    149083,182022,328930,144721,64607
     ]

cost = [
    27992,10992,48600,16691,24688,
    11400,25164,27992,35220,39920,
    31424,21560,66420,33800,26500
    ]
    
def create_chrome(value,cost):
  
    def _generate_chrome(num_gene=15):
        """generate one random chromosome"""
        genes = []
        for i in range(num_gene):
            gene=random.randint(0,1)
            genes.append(gene)
        #print(genes)
        return genes


    genes = _generate_chrome()
    def score_value(genes,value):

        valuelist=[]
        for i in range(len(genes)):
            score=value[i]*genes[i]
            valuelist.append(score)
        v=sum(valuelist)
        return v

    def score_weight(genes,cost):
        '''to score one chromosome.

        chromosome: list
        '''
        weightlist=[]
        for i in range(len(genes)):
            score=cost[i]*genes[i]
            weightlist.append(score)
        w=sum(weightlist)
        return w
    #print(_generate_chrome()) 
    #return _generate_chrome(),_second()
    
    genes,value,weight =_generate_chrome(),score_value(genes, value),score_weight(genes,cost)
    c = Chromosome() # creation of instance of chromosome object
    c.genes=genes
    c.value=value
    c.weight = weight
    return c

def main(n):
    "Iterate and save best result"
    optimal=0
    best_binary=[]
    for i in range(n):
        c=create_chrome(value,cost)
        if is_feasible(c,constraint):
            if c.value>optimal:
                optimal=c.value
                best_binary=c.genes
                best_weight = c.weight
                print("Feasible Value",optimal,"at iteration",i,
                "Optimal binary",best_binary,"Weight:",best_weight)
    return optimal,"Best binary is",best_binary,"at weight of:",best_weight

print("Optimal value of:",main(30000))
#c=create_chrome()
#print(c.genes,c.value,c.weight)
