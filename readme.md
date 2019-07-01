# Grafo

G = {v, e}

Grafo = {Vertice ,  Aresta} 

E - Arestas, unem 2 vértoces pode, ter peso, podem, ter direção
V - Vertices, podem ter várias arestas (ou nenhuma), podem ter vaçpres asspcoadps.

## Representação recomendada para grafos esparsos:
    Lista de adjacencias

## Opreções no grafo
    - adjacente(g, v, v)
    - vizinhos(g, v)
    - addAresta(g, v, u, p)
    - addVertex(G, v)
    - removeAresta(G, v, u)
    - removeVertex(G, v)

    - conectado(G, v) : lista dos vertices, em G a partir de v, que formam o grafo conectado F.

> Distãncia de manhattan - Taxi distance
> A*
> D*
> Euristica == chute
> Caminho euleriano


1 -> 3 
     3 -> 5
     3 -> 4
          4 <-> 5
          4 <-> 2
1 <- 2


Vertice 
    Ordem

Vértice | In | Out 
--------|----|----
1   | 1 | 1
2 | 1 | 2
3 | 1 | 2
4 | 2 | 2
5 | 2 | 0


## Passo a passo
1. Escolhe vértice com maior ordem de sída
2. Marca o vértice como visitado
3. Marca os vértices adjascentes como visitáveis
4. Remove o vértice
5. Volta para 1 



## Aplicação de grafo:
- GPS
- Logística
- Financeira
- Redes de computadores
    BGP (Roteamento)
    STP (Bridge)
- Redes neurais e ia
- antenas de celular
- Planejamento urbano
- automatos
    linguagens livres de contexto


