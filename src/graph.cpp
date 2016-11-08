#include <fstream>

#include "graph.hpp"


using namespace std;

//------------------------------------------------ Construtor

Graph::Graph(string infile){
    ifstream graph(infile.c_str());
    string nVertices;

    if(graph.is_open()){
        getline(graph,nVertices);
        V = atoi(nVertices.c_str());
        adj = new list<int>[V];
        int i,j;
        while(!graph.eof()){
            graph>>i;
            graph>>j;
            addEdge(i,j);
        }
    }else{
        cout<<"Falha ao abrir o arquivo"<<endl;
    }
    graph.close();
}


//--------------------------------------------------- VOID

void Graph::removeEdge(int i,int j){
    E--;
    adj[i].remove(j);
    adj[j].remove(i);
}

void Graph::addEdge(int i,int j){
    E++;
    adj[i].push_back(j);
    adj[j].push_back(i);
}


//------------------------------------------------ LISTS

list<int> Graph::getNeighbors(int v){
    return adj[v];
}

list<list<int>> Graph::getEdges(){
    return adj;
}


list<int> Graph::cover(){
    //arrumar codigo para que receba valores ja marcados
    list<int> cobertura;
    bool visited[V];
    for (int i=0; i<V; i++){
        visited[i] = false;
    }

    list<int>::iterator i;
    for (int u=0; u<V; u++){
        if (visited[u] == false){
            for (i= adj[u].begin(); i != adj[u].end(); ++i){
                int v = *i;
                if (visited[v] == false){
                     visited[v] = true;
                     visited[u]  = true;
                     break;
                }
            }
        }
    }

    return cobertura;
}

//------------------------------------------------ INTEGER RETRUNS

int Graph::getV(){
    return V;
}

int Graph::getE(){
    return E;
}