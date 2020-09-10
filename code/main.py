from tree import Tree, is_subtree
import example_trees
from time import time
from matplotlib import pyplot as plt

import genetic_algorithm
import general_purpose_algorithm
import randomized_algorithm
import deterministic_algorithm
import brute_force
import simulated_annealing

creator = example_trees.tables

time_genetic = []
time_general = []
time_randomized = []
time_deterministic =[]
time_annealing = []
collection_size = []

print(example_trees.T1.size)
collection = [example_trees.T1 for i in range(5)]
#collection = example_trees.collection

start = time()
max_subtree = general_purpose_algorithm.max_common_subtree(collection)
end = time() 
print("Time(general-purpose): ", end-start)
print(str(max_subtree.size) + ": " + str(max_subtree))   

start = time()
k = 3
max_subtree = randomized_algorithm.max_common_subtree(collection,k)
end = time() 
print("Time(randomized): ", end-start)
print(str(max_subtree.size) + ": " + str(max_subtree))   

start = time()
k = 2
max_subtree = deterministic_algorithm.max_common_subtree(collection,k)
end = time() 
print("Time(deterministic): ", end-start)
print(str(max_subtree.size) + ": " + str(max_subtree))  



start = time()
max_subtree = genetic_algorithm.max_common_subtree(collection)
end = time()
print("Time(genetic):", end-start)
print(str(max_subtree.size) + ": " + str(max_subtree))   


start = time()
max_subtree = simulated_annealing.max_common_subtree(collection)
end = time()  
print("Time(simulated annealing): ", end-start)
print(str(max_subtree.size) + ": " + str(max_subtree))   

'''
start = time()
max_subtree = brute_force.max_common_subtree(collection)
end = time() 
print("Time(brute force): ", end-start)
print(str(max_subtree.size) + ": " + str(max_subtree))   
'''