from grafo import *
from desenha import *
from random import *

grafo = Grafo()
desenha = Desenha()

for i in range(1, 6):
    coordenada = (randint(-300,300), randint(-300, 300))
    grafo.addVertice(i, coordenada)

for item in grafo.vertices:
    if item == 0:
        print(item)
print("*"*10)
desenha.desenha(grafo.vertices)