class Vertice:
    def __init__(self, vertice, coordenada):
        self.vertice = vertice
        self.coordenada = coordenada
        self.arestas = []
    
    def __repr__(self):
        return f"{self.vertice}->{self.coordenada}"

class Aresta:
    def __init__(self, aresta, ligado):
        self.vertice = ligado
        self.aresta = aresta
    

class Grafo:
    def __init__(self):
        self.vertices = []

    def addVertice(self, vertice, coordenada, peso=None):
        self.vertices.append(Vertice(vertice, coordenada))

    def addAresta(self, vertice, aresta, ligado, peso=None):
        for v in self.vertices:
            if v == vertice:
                v.arestas.append(Aresta(aresta, ligado))