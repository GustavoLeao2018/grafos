from turtle import *
from time import sleep

class Desenha:
    def __init__(self):
        self.janela = Screen()
        self.pen = Pen()

    def desenha(self, lista):
        for item in lista:
            self.pen.penup()
            self.pen.goto(item.coordenada)
            self.pen.pendown()
            self.pen.circle(3)
            self.pen.forward(5)
            self.pen.write(self.pen.pos())
            print(item)
            sleep(1)

