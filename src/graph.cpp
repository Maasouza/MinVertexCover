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
        adj = new vector<int>[V];
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
    adj[i].erase(adj->begin()+(j));
    adj[j].erase(adj->begin()+(i));
}

void Graph::addEdge(int i,int j){
    E++;
    adj[i].push_back(j);
    adj[j].push_back(i);
}


//------------------------------------------------ vectorS

vector<int> Graph::getNeighbors(int v){
    return adj[v];
}

vector<int>* Graph::getEdges(){
    return adj;
}


vector<int> Graph::cover(){
    //arrumar codigo para que receba valores ja marcados
    vector<int> cobertura;
    bool visited[V];
    for (int i=0; i<V; i++){
        visited[i] = false;
    }

    vector<int>::iterator i;
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
            cobertura.push_back(u);
        }
    }

    return cobertura;
}

//------------------------------------------------ INTEGER RETRUNS

int Graph::numV(){
    return V;
}

int Graph::numE(){
    return E;
}