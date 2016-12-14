import itertools as it
from util import *


def brute_force(g):
    vertices = list(range(len(g.nodes())))

    for r in range(1,len(vertices)):
        print(r)
        for i in it.combinations(vertices,r):
            cover = list(i)
            if(isCover(g,cover)):
                return [ 1 if i in cover else 0 for i in range(len(g.nodes()))]