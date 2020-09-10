from tree import is_subtree,check,Tree
from time import time
import itertools
import numpy as np  
import copy

def find_subtrees(t):
    if t.children == []:
        return [t], [t]
    
    result_lst = []
    current_lst = []
    
    all_curr = []
    help_list = []
    for ch in t.children:
        res, curr = find_subtrees(ch)
        all_curr.append(curr)
        help_list.append(list(range(len(curr)+1)))
        result_lst += res
    
    for order in list(itertools.product(*help_list)):
        children = []
        for i in range(len(order)):
            if order[i] == len(all_curr[i]):
                continue
            children.append(all_curr[i][order[i]])
        current_lst.append(Tree(t.data, children))
           
    for t1 in current_lst:
        for t2 in current_lst:
            if t1!=t2 and check(t1,t2):
                current_lst.remove(t2)
            
    result_lst += current_lst
    for t1 in result_lst:
        for t2 in result_lst:
            if t1 != t2 and check(t1,t2):
                result_lst.remove(t2)
    
    return result_lst, current_lst

def max_common_subtree(collection):
    minimal_tree = min(collection, key = lambda x: x.size)
    collection.remove(minimal_tree)

    subtrees,_ = find_subtrees(minimal_tree)
    subtrees.sort(key = lambda x: x.size, reverse = True)
    for subtree in subtrees:
        res = True
        for tree in collection:
            if not is_subtree(subtree,tree):
                res = False
                break
        if res == True:
            return subtree

    collection.append(minimal_tree)
    return None