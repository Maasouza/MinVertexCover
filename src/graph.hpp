#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

class Graph{
    int V;
    int E;
    vector<int> *adj;
public:
    Graph(string infile);
    void addEdge(int i, int j);
    void removeEdge(int i,int j);

    int numV();
    int numE();

    vector<int> getNeighbors(int v);
    vector<int>* getEdges();

    vector<int> cover();
};

