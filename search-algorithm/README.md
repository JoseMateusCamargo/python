<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="130">

# Algoritmos de busca (Search Algorithms)

Em ciência da computação, um algoritmo de pesquisa é um algoritmo (normalmente envolvendo uma infinidade de outros
algoritmos mais específicos) que resolve um problema de pesquisa. Os algoritmos de busca funcionam para recuperar
informações armazenadas dentro de alguma estrutura de dados, ou calculadas no espaço de busca de um domínio de problema,
com valores discretos ou contínuos. Em termos gerais é um algoritmo que toma um problema como entrada e retorna a
solução para o problema, geralmente após resolver um número possível de soluções.

#### Let's Go Code! Some types of search algorithms

---

[Binary Search Tree (BST).](https://github.com/JoseMateusCamargo/python/blob/master/search-algorithm/bst_binary_search_tree.py)

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing
in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just
one.

---

[Depth First Search (DFS) in 2D grid.](https://github.com/JoseMateusCamargo/python/blob/master/search-algorithm/DSF_2D_grid.py)  
<i>(DFS to check for characters on diagonals in 2D grid)</i>

O <b>Depth First Search (DFS)</b> é um algoritmo para percorrer ou pesquisar estruturas de dados de árvore ou gráfico
que usa a ideia de retrocesso. Ele explora todos os nós indo para frente, se possível, ou usa backtracking.

* Time complexity:
    * A complexidade de tempo do DFS se toda a árvore for percorrida é `O(V)` onde V é o número de nós.
    * No caso de um gráfico, a complexidade do tempo é `O(V + E)` onde V é o número de vértices e E é o número de
      arestas.

<b>Example</b>  
Começando do nó de origem 1 , continuamos nos movendo para os nós adjacentes de 3 a 5 a 6, onde alcançamos o nível mais
distante. Em seguida, voltamos ao nó 6 anterior e mais uma vez investigamos até o nível mais distante onde atingimos o
nó 10, repetimos esse processo para todos os nós ainda não percorridos.

![Alt text](img/dsf.gif "Depth First Search (DFS)")