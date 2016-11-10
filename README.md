
#<p align='center'>EEL857 - Otimização em Grafos - UFRJ 2016.2</p>
<p align='center'>Algoritmos para resolução do problema de cobertura minima de vertices</p>

Trabalho desenvolvido por: [Marcos Aurélio](https://github.com/Maasouza)<br>
Para a disciplina do Profº. Luidi Simonetti

1. Tecnologias
  * C++

2. Funções e Algoritmos

  - [ ] Algoritmo de força bruta
  - [ ] Algoritmo backtracking
  - [ ] Algoritmo branch and bound
  - [ ] Algoritmo utilizando a heurística XXXX
  - [X] Função para gerar um grafo aleatório

3. Instruções
    * [Download](https://github.com/Maasouza/MinVertexCover/archive/master.zip)

    * Clone

            git clone https://github.com/maasouza/minvertexcover.git

    * Para rodar o algoritmo

            cd minvertexcover/src
            make
            ./main --path ../path/to/graph.dat --type [BF|BT|BB|HT]

    * Para gerar um grafo

            cd minvertexcover/data
            make
            ./new --v nVertices --d densidade --path ../path/to/new_graph.dat

    * Visualizar o grafo

            O grafo pode ser visualizado localmente.
            Basta abrir o arquivo index.html (Firefox only).
            Exemplo https://maasouza.github.io/MinVertexCover/site/






