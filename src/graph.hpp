#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>

using namespace std;

class Graph{
    int V;
    int E;
    list<int> *adj;
public:
    Graph(string infile);
    void addEdge(int i, int j);
    void removeEdge(int i,int j);

    int getV();
    int getE();

    list<int> getNeighbors(int v);
    list<list<int>> getEdges();

    list<int> cover();
};

