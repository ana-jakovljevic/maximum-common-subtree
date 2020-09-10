from time import time
import numpy as np
from itertools import chain,combinations
import math
from tree import is_subtree, create_subtree

def greedy_partition(tree,bottom,top):
    my_partitions = []
    sum_eliminated = 0
    indicator = True #cvor ispunjava uslove
    if tree.size >= bottom and tree.size <= top:
        for child in tree.children:
            if child.size >= bottom:
                indicator = False
                partitions, eliminated = greedy_partition(child, bottom, top)
                sum_eliminated += eliminated
                my_partitions += partitions
    elif tree.size > top:
        indicator = False
        for child in tree.children:
            partitions, eliminated = greedy_partition(child, bottom, top)
            sum_eliminated += eliminated
            my_partitions += partitions
    else:
        indicator = False

    if indicator:
        return [tree], tree.size
    
    if tree.size - sum_eliminated >= bottom and tree.size - sum_eliminated <=top:
        return [tree] + my_partitions, tree.size
    else:
        return my_partitions, sum_eliminated



def partition_nodes(partition, partitions, distance, current_distance):    
    if partition in partitions and current_distance != 0:
        return []
    
    result = []
    for ch in partition.children:
        result += partition_nodes(ch, partitions, distance, current_distance+1)
    
    if distance == current_distance:
        return result
    else:
        return result + [partition]
    

def create_groups(partitions,distance,group_num):
    groups = [[] for i in range(group_num)]
    current_group = 0
    for partition in partitions:
        nodes_of_partition = partition_nodes(partition, partitions, distance, 0)
        for i in range(len(nodes_of_partition)):
            groups[current_group%group_num].append(nodes_of_partition[i])
            current_group += 1            
    return groups


def powerset(group,size):
    group = list(group)
    return combinations(group, size)

def max_common_subtree(collection,k):
    minimal_tree = min(collection, key = lambda x: x.size)
    collection.remove(minimal_tree)

    nodes = list(minimal_tree.get_all_nodes())
    n = minimal_tree.size
    m = math.floor(math.log(n)/math.log(k))
    _,d = minimal_tree.get_depth_and_degree()
    distance = math.floor(1/2 * (math.log(n)/math.log(d)))
    top = math.floor(2*n/(k*m))
    bottom = math.ceil(n/(k*m))

    partitions, _ = greedy_partition(minimal_tree,bottom,top)
    groups = create_groups(partitions,distance,top)

    max_subtree = None
    for group in groups:
        combinations = powerset(group, math.ceil(m/3))
        for combination in combinations:
            is_sub_fleg = True
            comb_list = list(combination)
            subtree,_ = create_subtree(minimal_tree,comb_list , 0)
            for tree in collection:
                if not is_subtree(subtree,tree):
                    is_sub_fleg = False
                    
            if max_subtree==None or is_sub_fleg and max_subtree.size < subtree.size:
                max_subtree = subtree
            
    collection.append(minimal_tree)
    return max_subtree