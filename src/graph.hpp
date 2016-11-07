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
    void addEdge(int j, int i);
    list<int> cover();
};

