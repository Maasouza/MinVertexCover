import networkx as nx
from util import *
from heuristic import *
from bruteforce import *
from bnb import *

g = nx.Graph()

load_graph(g,"../data/50v50d.dat")

#c =  brute_force(g)

#c = heuristic_cover(g,1)
c = branch_and_bound(g)
draw_results(g,c)