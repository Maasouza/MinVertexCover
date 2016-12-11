import networkx as nx
from util import *


g = nx.Graph()

load_graph(g,"../data/test.dat")

start = time.time()
end = time.time()
print("--- Exec time: "+str((end-start)*1000)+" sec ---")


c,m,v = pre_process(g)


draw_results(g,c)

