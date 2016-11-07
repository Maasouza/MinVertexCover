#include "graph.hpp"

using namespace std;

Graph::Graph()
{

}

void Graph::addEdge(int v, int w)
{
    E++;
    adj[v].push_back(w); // Add w to v’s list.
    adj[w].push_back(v); // Since the graph is undirected
}


list<int> Graph::cover(){

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
}