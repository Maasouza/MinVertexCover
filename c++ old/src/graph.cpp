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


vector<int> Graph::coverHeuristica(){

    vector<int> cobertura;
    int  grauV[V];
    bool visited[V];
    int marcados = 0;
    for (int i=0; i<V; i++){
        visited[i] = false;
        grauV[i]=adj[i].size();
    }

    do{

        int v = maiorGrau(grauV,visited);
        if(v==-1){
            cout<<"deu xabú"<<endl;
            break;
        }
        if(!visited[v]){
            visited[v] = true;
            grauV[v] = 0;
            cobertura.push_back(v);
            marcados++;
            for(int i = 0 ; i < adj[v].size() ; i++){
                if(!visited[adj[v][i]]){
                    marcados++;
                    visited[adj[v][i]] = true;
                    grauV[adj[v][i]] = 0;
                    for(int j = 0 ; j < adj[i].size() ; j++ ){
                        grauV[adj[i][j]]--;
                    }
                }
            }
        }
    }while(marcados!=V);

    return cobertura;
}


//------------------------------------------------ INTEGER RETRUNS

int Graph::maiorGrau(int* graus,bool* marcados){

    srand(time(0));

    int m_grau=0;
    int* g = graus;

    bool* m = marcados;

    vector<int> index_vector;

    for(int i = 0 ; i < V ; i++){
        if(m_grau<g[i] && !m[i]){
            index_vector.clear();
            m_grau = g[i];
            index_vector.push_back(i);
        }else{
            if(m_grau==g[i] && !m[i]){
                index_vector.push_back(i);
            }
        }
    }

    if(index_vector.size()<1) return -1;

    int index = rand()%index_vector.size();

    return index_vector[index];
}

int Graph::numV(){
    return V;
}

int Graph::numE(){
    return E;
}