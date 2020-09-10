from tree import Tree

T1 = Tree("T1", [Tree("V2",[]),Tree("V3",[]),Tree("V4",[Tree("V6",[Tree("V11",[Tree("V17",[Tree("V22",[Tree("V25",[Tree("V27",[])]),Tree("V26",[])]),Tree("V23",[]),Tree("V24",[])]),Tree("V18",[]),Tree("V19",[])]),Tree("V12",[]),Tree("V13",[]),Tree("V14",[Tree("V20",[])])]),Tree("V7",[Tree("V15",[])]),Tree("V8",[Tree("V16",[Tree("V21",[])])]),Tree("V9",[])]),Tree("V5",[Tree("V10",[])])])
T2 = Tree("T1", [Tree("H2",[]),Tree("H3",[]),Tree("H4",[Tree("H7",[Tree("H14",[Tree("H17",[Tree("H19",[]),Tree("H20",[Tree("H24",[]),Tree("H25",[])]),Tree("H21",[])]),Tree("H18",[Tree("H22",[]),Tree("H23",[])])])]),Tree("H8",[]),Tree("H9",[Tree("H15",[])])]),Tree("H5",[Tree("H10",[])]),Tree("H6",[Tree("H11",[Tree("H16",[])]),Tree("H12",[]),Tree("H13",[])])])
T3 = Tree("T3", [Tree("A",[]),Tree("B",[Tree("D",[Tree("H",[])]),Tree("E",[Tree("I",[]),Tree("J",[])])]),Tree("C",[Tree("F",[])]),Tree("G",[Tree("K",[])])])

H1 = Tree("",[T1,T2,T3])
H2 = Tree("",[Tree("",[T1,T2])])
H3 = Tree("",[Tree("",[]),Tree("",[]),Tree("",[T1,T2,T3])])

G1 = Tree("",[Tree("",[]),Tree("",[T1,T2]),Tree("",[H3])])
G2 = Tree("",[Tree("",[H1]),Tree("",[H2])])
G3 = Tree("",[Tree("",[]),Tree("",[H1,H2,H3]),Tree("",[])])

E1 = Tree("",[Tree("",[H1,H2,H3]),Tree("",[G1,G2,G3])])
E2 = Tree("",[G1,G2,H1,H2,H3])
E3 = Tree("",[G3,T1,T2,T3])

V1 = Tree("",[Tree("",[Tree("",[])]),Tree("",[]),Tree("",[E1,E2])])
V2 = Tree("",[Tree("",[Tree("",[]),Tree("",[])]),Tree("",[G1,G2,G3])])
V3 = Tree("",[E1,G2,H3])

tables = [T1,T2,T3,H1,H2,H3,G1,G2,G3,E1,E2,E3,V1,V2,V3]
tables.sort(key=lambda x: x.size, reverse=True)

'''
idx = 0
collection = []
for i in range(100):
    collection.append(tables[idx])
    idx = (idx + 1) % len(tables)
'''