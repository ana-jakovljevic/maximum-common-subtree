from time import time
import numpy as np
import random
from tree import Tree,is_subtree
import example_trees
import copy

class Individual:
    def __init__(self,tree):
        self.code = tree
        self.fitness = fitnessFunction(self)
        
    def repair(self):
        while self.fitness == 0:
            children = []
            #children = copy.deepcopy(random.choice(population).code.children)
            self.code = Tree("",children)
            self.fitness = fitnessFunction(self)
            
    def __lt__(self, other):
         return self.fitness < other.fitness
        
def fitnessFunction(individual):
    #individual_depth, individual_degree = individual.code.get_depth_and_degree()
    #if individual.code.size > min_tree.size or individual_depth > min_tree_depth or individual_degree > min_tree_degree:
    #    return 0
    for tree in collection:
        if not is_subtree(individual.code, tree):
            return 0
    return individual.code.size


def tournament_selection(population,tournament_size):
    maximum = float('-inf')
    k = -1
    
    for i in range(tournament_size):
        j = random.randrange(len(population))
        if population[j].fitness > maximum:
            maximum = population[j].fitness
            k = j
    return k


def roulette_selection(population):
    rand = random.random() * sum([p.fitness for p in population])
    current_sum = 0
    for i in range(len(population)):
        current_sum += population[i].fitness
        if rand <= current_sum:
            return i


def crossover(parent1, parent2, child1, child2):
    nodes1 = parent1.code.get_all_nodes()
    nodes2 = parent2.code.get_all_nodes()
    
    sum1 = 0
    sum2 = 0
    for node in nodes1:
        sum1 += len(node.children)
    for node in nodes2:
        sum2 += len(node.children)
        

    if sum1 == 0:
        node1 = parent1.code
    else:
        node1 = np.random.choice(nodes1,p=[len(node.children)/sum1 for node in nodes1])
    
    if sum2 == 0:
        node2 = parent2.code
    else:
        node2 = np.random.choice(nodes2,p=[len(node.children)/sum2 for node in nodes2])

    '''
    node1 = np.random.choice(nodes1)
    node2 = np.random.choice(nodes2)
    '''
    node1 = copy.deepcopy(node1)
    node2 = copy.deepcopy(node2)
    
    child1.code = Tree(node1.data, node1.children + [node2])
    child2.code = Tree(node2.data, node2.children + [node1])

def mutation(individual):
    all_nodes = individual.code.get_all_nodes()
    node = random.choice(all_nodes)
    if random.random() > 0.01:
        return 
    if individual.code.parent != None:
        individual.code.parent.delete_child(individual.code)

def population_init(size):
    population = []
    degree = 0
    for i in range(size):
        population.append(Individual(Tree("", [Tree("",[]) for x in range(degree)])))
        #population.append(Individual(Tree("", [])))
        degree = (degree + 1) % (min_tree_degree+1)
    return population, population    
    
def set_parameters():
    population_size = 80
    elite_size = 6
    iteration_range = 500
    tournament_size = 4
    return population_size, elite_size, iteration_range,tournament_size

def max_common_subtree(coll):
    global collection
    collection = coll
    global min_tree 
    min_tree = min(collection, key = lambda x: x.size)
    global min_tree_depth, min_tree_degree
    min_tree_depth, min_tree_degree =  min_tree.get_depth_and_degree()
    global population

    population_size, elite_size, iteration_range, tournament_size  = set_parameters()
    population,newPopulation = population_init(population_size)

    best_individual = None
    best_individual_repeat = 0
    
    for iteration in range(iteration_range):
        population.sort(key = lambda x: x.fitness, reverse=True)
        
        if population[0] == best_individual:
            best_individual_repeat += 1 
        else:
            best_individual_repeat = 0
        if best_individual_repeat > 30:
            return best_individual.code
        
        for i in range(elite_size):
            newPopulation[i] = population[i]
        for i in range(elite_size, population_size, 2):
            k1 = roulette_selection(population)
            k2 = roulette_selection(population)
            #k1 = tournament_selection(population,tournament_size)
            #k2 = tournament_selection(population,tournament_size)
            crossover(population[k1], population[k2], newPopulation[i], newPopulation[i + 1])
            mutation(newPopulation[i])
            mutation(newPopulation[i+1])
            newPopulation[i].fitness = fitnessFunction(newPopulation[i])
            newPopulation[i].repair()
            newPopulation[i + 1].fitness = fitnessFunction(newPopulation[i + 1])
            newPopulation[i+1].repair()
        population = newPopulation
        best_individual = population[0]


    population.sort(key = lambda x: x.fitness, reverse=True)
    return population[0].code
