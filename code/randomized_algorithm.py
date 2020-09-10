import math
import random
import copy
from tree import create_subtree, is_subtree

def choose_nodes(nodes, size_of_set):
    return random.sample(nodes, k=size_of_set)

def max_common_subtree(collection,k):
    collection = copy.deepcopy(collection)
    minimal_tree = min(collection, key = lambda x: x.size)
    collection.remove(minimal_tree)

    n = minimal_tree.size
    m = math.floor(math.log(n)/math.log(k))
    nodes = list(minimal_tree.get_all_nodes())

    max_subtree = None
    repeat_range = n*n
    for i in range(repeat_range):
        choosen = choose_nodes(nodes, m)
        subtree_flag = True
        subtree = create_subtree(minimal_tree,choosen,0)[0]
        for tree in collection:
            if not is_subtree(subtree,tree):
                subtree_flag = False
                break
        if subtree_flag and (max_subtree == None or subtree.size > max_subtree.size):
            max_subtree = subtree
    return max_subtree