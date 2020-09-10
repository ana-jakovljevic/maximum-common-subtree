from tree import Tree, is_subtree
import random
import copy
import math

def create_solution():
    return Tree("",[])

def fitness_function(s,collection):
    for tree in collection:
        if not is_subtree(s,tree):
            return 0
    return s.size

def choose_new_solution(solution,p):
    solution = copy.deepcopy(solution)

    all_nodes = solution.get_all_nodes()
    node = random.choice(all_nodes)

    operation = random.randrange(3)    
    if operation == 0:
        if node.parent == None or random.random() > p:
            operation = 1
        else:
            node.parent.delete_child(node)
    if operation == 1:
        node.add_child(Tree("",[]))

    if operation == 2:
        solution = Tree("",[solution])
    
    return solution

def max_common_subtree(collection):
    max_iter = 500

    solution = create_solution()
    solution_fitness = fitness_function(solution,collection)
    best_fitness_ever = solution_fitness
    best_solution = solution

    for i in range(1,max_iter):       
        p = math.log(2)/math.log(1+i)
        candidat = choose_new_solution(solution,p)
        candidat_fitness = fitness_function(candidat,collection)
        if candidat_fitness > solution_fitness:
            solution = candidat
            solution_fitness = candidat_fitness
        else:
            q = random.random()
            if p > q and candidat_fitness != 0:
                solution = candidat
                solution_fitness = candidat_fitness
        if solution_fitness > best_fitness_ever:
            best_fitness_ever = solution_fitness
            best_solution = solution
    return best_solution