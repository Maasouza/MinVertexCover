import networkx as nx
from util import *
from heuristic import *
from bruteforce import *
from branch_and_bound import *

g = nx.Graph()

load_graph(g,"../data/20v30d.dat")

#c = [0 for x in range(g.number_of_nodes())]
#A = [0 for x in range(g.number_of_nodes())]
#c = heuristic_cover(g)
#c = brute_force(g)

size,c = branch_and_bound(g)

draw_results(g,c,1) #0 para cover = [1,0....,1,...0,....1] 1 para cover = [1,3,6]