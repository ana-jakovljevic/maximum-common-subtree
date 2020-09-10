class Tree:
    def __init__(self, data, children):        
        self.data = data
        self.children = children
        
        self.depth = None
        self.parent = None
        self.size = 1
        for child in self.children:
            child.parent = self
            self.size += child.size
        
    def __str__(self):
        res = "0" 
        for ch in self.children:
            res += str(ch)
        res = res +  "1"
        return res

    def delete_child(self,ch):
        self.children.remove(ch)
        self.size -= ch.size       
        if self.parent != None:
            self.parent.change_size(-1 * ch.size)
        ch.parent = None
    
    def add_child(self,ch):
        self.children.append(ch)
        self.size += ch.size
        ch.parent = self
        if self.parent != None:
            self.parent.change_size(ch.size)
        
    def change_size(self,size):
        self.size += size
        if self.parent != None:
            self.parent.change_size(size)
    
    def get_all_nodes(self):
        all_nodes = [self]
        for ch in self.children:
            all_nodes += ch.get_all_nodes()
        return all_nodes
        
    def get_depth_and_degree(self):
        max_degree = len(self.children)
        max_depth = 1
        for ch in self.children:
            depth,degree = ch.get_depth_and_degree() 
            if max_degree < degree:
                max_degree = degree
            if max_depth < depth +1:
                max_depth = depth+1
        return max_depth , max_degree

    def set_depths(self,depth):
        self.depth = depth
        for ch in self.children:
            ch.set_depths(depth+1)


def check_matrix(matrix,lst):
    row = matrix[0]
    for idx in range(len(row)):
        if not row[idx] in lst:
            if len(matrix) == 1:
                return True
            
            lst.append(row[idx])
            value = check_matrix(matrix[1:],lst)
            if value == True:
                return True
            else:
                lst.pop()
    return False

    
def check(root1, root2): 
    if root1.children == [] and root2.children == []: 
        return True
    
    if root1 == [] or root2 == []: 
        return False

    if len(root1.children) != len(root2.children):
        return False
    
    if root1.size != root2.size:
        return False
    
    matrix = []
    for ch1 in root1.children:
        equal_one_child = []
        for idx in range(len(root2.children)):
            if check(ch1,root2.children[idx]):
                equal_one_child.append(idx)
        matrix.append(equal_one_child)
    
    return check_matrix(matrix,[])

def is_subtree(t1,t2):
    if t1.size > t2.size:
        return  False

    if t1.children == []:
        return True

    if t1.size == t2.size:
        return check(t1,t2)
    
    if len(t1.children) > len(t2.children):
        for ch in t2.children:
            if is_subtree(t1,ch):
                return True
        return False
    
    matrix = []
    for ch1 in t1.children:
        equal_one_child = []
        for idx in range(len(t2.children)):
            if is_subtree(ch1,t2.children[idx]):
                equal_one_child.append(idx)                
        matrix.append(equal_one_child)
    
    return check_matrix(matrix,[])
    

def create_subtree(node, nodes, num_nodes):
    if node.children == []:
        if node in nodes:
            return Tree(node.data, []), 1
        return None, 0
    
    children_results = []
    my_num_nodes = 0
    for ch in node.children:
        tree, current_num_nodes = create_subtree(ch, nodes, 0)
        
        if current_num_nodes == len(nodes):
            return tree, current_num_nodes
        
        if current_num_nodes > 0:
            my_num_nodes += current_num_nodes
            children_results.append(tree)
    
    if node in nodes:
        my_num_nodes += 1
    
    if my_num_nodes == 0:
        return None, 0
    
    tree = Tree(node.data, children_results)
    return tree, my_num_nodes

