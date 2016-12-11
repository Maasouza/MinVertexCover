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
    bool *cobertura;

    Graph(string infile);
    void addEdge(int i, int j);
    void removeEdge(int i,int j);
    void coverHeuristica();

    int numV();
    int numE();
    int maiorGrau(int* graus,bool * cobertos);
    int atualizarGrau(int vertice,bool* cobertos);

    vector<int> getNeighbors(int v);
    vector<int>* getEdges();

};

