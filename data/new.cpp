#include <iostream>
#include <cstdio>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <stdlib.h>

using namespace std;

void print_info(char* name){

        cout<<"Argumentos invalidos\nExecute usando: "<<name<<"  --v nVertices --d Densidade --path ../path/to/new_graph.dat "<<endl;
        cout<<"O arquivo de saida seguirá o formato \n\nNº de vertices\nVa Vb\n.\n.\n.\nVi Vj"<<endl;

}

int main(int argc, char *argv[]) {

    if (argc != 7) {
        print_info(argv[0]);
        return 1;
    }


    string opt [3] = {(string)argv[1],(string)argv[3],(string)argv[5]};
    string params[3] = {(string)argv[2],(string)argv[4],(string)argv[6]};

    if(opt[0] != "--v" or opt[1] != "--d" or opt[2] != "--path"){
        print_info(argv[0]);
        return 1;
    }


    int nVertices = atoi(params[0].c_str());
    int density = atoi(params[1].c_str());
    string outfile = params[2].c_str();
    int nMaxArestas = (int) ((nVertices*(nVertices-1)/2)*density/100);
    int nArestas = 0;
    vector<int> *adj;

    adj = new vector<int>[nVertices];
    ofstream new_graph(outfile);

    new_graph<<nVertices;

    srand48(time(0));

    for(int i = 0 ; i < nVertices -1; i++){
        adj[i].push_back(i+1);
        adj[i+1].push_back(i);
        new_graph<<"\n"<<i<<" "<<i+1;
        nArestas++;
    }


    while(nArestas<nMaxArestas){
        int i = lrand48()%nVertices;
        int j = lrand48()%nVertices;
        bool in = false;
        if(i != j){
            for(int k = 0 ; k < adj[i].size(); k++){
                if(adj[i][k]==j){
                    in=true;
                }
            }
            if(!in){
                adj[i].push_back(j);
                adj[j].push_back(i);
                new_graph<<"\n"<<i<<" "<<j;
                nArestas++;
            }
        }
    }

    new_graph.close();

    return 1;
}