from itertools import chain, combinations
import math
import random
from tree import create_subtree, is_subtree
import copy

def choose_nodes(nodes, num_of_sets,size_of_set):
    choosen = []
    for i in range(num_of_sets):
        chs = random.sample(nodes, k=size_of_set)
        choosen.append(chs)
        for ch in chs:
            nodes.remove(ch)
    return choosen
    

def powerset(lst):
    lst = list(lst)
    broj_elemenata = list(range(1,len(lst)+1))
    broj_elemenata.reverse()
    return chain.from_iterable(combinations(lst, x) for x in broj_elemenata)

def max_common_subtree(collection):
    minimal_tree = min(collection, key = lambda x: x.size)
    collection.remove(minimal_tree)

    n = minimal_tree.size
    num_of_sets = math.floor(n/math.floor((math.log(n)/math.log(2))))
    size_of_set = math.floor((math.log(n)/math.log(2)))
    nodes = list(minimal_tree.get_all_nodes())
    groups = choose_nodes(nodes, num_of_sets, size_of_set)

    max_subtree = None
    for group in groups:
        group = powerset(group)
        for choosen in group:
            subtree_flag = True
            subtree = create_subtree(minimal_tree,choosen,0)[0]
            for tree in collection:
                if not is_subtree(subtree,tree):
                    subtree_flag = False
                    break
            if subtree_flag and (max_subtree == None or subtree.size > max_subtree.size):
                max_subtree = subtree
                
    collection.append(minimal_tree)
    return max_subtree

