from tree import Tree

T1 = Tree("V1", [Tree("V2",[]),Tree("V3",[]),Tree("V4",[Tree("V6",[Tree("V11",[Tree("V17",[Tree("V22",[Tree("V25",[Tree("V27",[])]),Tree("V26",[])]),Tree("V23",[]),Tree("V24",[])]),Tree("V18",[]),Tree("V19",[])]),Tree("V12",[]),Tree("V13",[]),Tree("V14",[Tree("V20",[])])]),Tree("V7",[Tree("V15",[])]),Tree("V8",[Tree("V16",[Tree("V21",[])])]),Tree("V9",[])]),Tree("V5",[Tree("V10",[])])])
T2 = Tree("H1", [Tree("H2",[]),Tree("H3",[]),Tree("H4",[Tree("H7",[Tree("H14",[Tree("H17",[Tree("H19",[]),Tree("H20",[Tree("H24",[]),Tree("H25",[])]),Tree("H21",[])]),Tree("H18",[Tree("H22",[]),Tree("H23",[])])])]),Tree("H8",[]),Tree("H9",[Tree("H15",[])])]),Tree("H5",[Tree("H10",[])]),Tree("H6",[Tree("H11",[Tree("H16",[])]),Tree("H12",[]),Tree("H13",[])])])
T3 = Tree("T1", [Tree("A",[]),Tree("B",[Tree("D",[Tree("H",[])]),Tree("E",[Tree("I",[]),Tree("J",[])])]),Tree("C",[Tree("F",[])]),Tree("G",[Tree("K",[])])])


tables = [T1,T2,T3]
idx = 0
collection = []
for i in range(1000):
    collection.append(tables[idx])
    idx = (idx + 1) % 3 