"""
Practica 2025-02-11
Dibujar un Cubo con t
No. Control 21760550
Alumno: Ilse Paloma Machado Gonzalez
Grupo: 8SE
Materia: IA
"""


import t as t
from random import random



def DrawLine():
    for i in range (4):
        t.forward(200)
        t.right(90)
        t.towards(0,20)

def DrawBackSquare():   
        t.left(45)
        t.forward(200)
        t.right(45)
        t.forward(200)
        t.right(90)
        t.forward(200)
        t.right(90)
        t.forward(200)
        t.right(90)
        t.forward(200)
        t.backward(200)

def DrawCube():
     t.right(90)
     t.forward(200)
     t.right(135)
     t.forward(200)
     t.right(135)
     t.forward(200)
     t.right(45)
     t.forward(200)
     t.left(180)
     t.forward(200)
     t.left(135)
     t.right(180)
     t.forward(200)
     t.left(90)
     t.forward(200)
     t.right(225)
     t.forward(200)

     
     
     
    

     

DrawLine()
DrawBackSquare()
DrawCube()




input('stop')
