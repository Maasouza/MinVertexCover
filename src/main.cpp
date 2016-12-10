#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include "graph.hpp"

using namespace std;

void print_info(char* name){

        cout<<"Argumentos invalidos\nExecute usando: "<<name<<"  --path ../path/to/graph.dat"<<endl;
        cout<<"O arquivo de entrada deve seguir o formato \n\nNº de vertices\nVa Vb\n.\n.\n.\nVi Vj"<<endl;

}

int main(int argc, char *argv[]) {

    if (argc != 3) {
        print_info(argv[0]);
        return 1;
    }

    string opt = argv[1];
    string infile = argv[2];

    if(opt != "--path"){
        print_info(argv[0]);
        return 1;
    }

    Graph g(infile);

    g.coverHeuristica();

    for(int i = 0 ; i < g.numV() ; i++){
        if(g.cobertura[i])
            cout<<g.cobertura[i]<<" ";
    }

    return 1;
}