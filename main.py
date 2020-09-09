from tree import Tree , is_subtree
import example_trees
from time import time

import genetic_algorithm
import general_purpose_algorithm
import randomized_algorithm
import deterministic_algorithm
import brute_force
import simulated_annealing

collection = example_trees.collection
print(len(collection))

start = time()
max_subtree = genetic_algorithm.max_common_subtree(collection)
print(str(max_subtree.size) + ": " + str(max_subtree))     
end = time()
print("Time(genetic):", end-start)


start = time()
max_subtree = general_purpose_algorithm.max_common_subtree(collection)
print(str(max_subtree.size) + ": " + str(max_subtree))   
end = time() 
print("Time(general-purpose): ", end-start)

start = time()
k = 3
max_subtree = randomized_algorithm.max_common_subtree(collection,k)
print(str(max_subtree.size) + ": " + str(max_subtree))   
end = time() 
print("Time(randomized): ", end-start)

start = time()
k = 2
max_subtree = deterministic_algorithm.max_common_subtree(collection,k)
print(str(max_subtree.size) + ": " + str(max_subtree))  
end = time() 
print("Time(deterministic): ", end-start)


start = time()
max_subtree = simulated_annealing.max_common_subtree(collection)
print(str(max_subtree.size) + ": " + str(max_subtree))   
end = time() 
print("Time(simulated annealing): ", end-start)

'''
start = time()
max_subtree = brute_force.max_common_subtree(collection)
print(str(max_subtree.size) + ": " + str(max_subtree))   
end = time() 
print("Time(brute force): ", end-start)
'''