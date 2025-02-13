"""
Practica 2025-02-11
Dibujar una linea desde punto A a punto B usando .dot()
No. Control 21760550
Alumno: Ilse Paloma Machado Gonzalez
Grupo: 8SE
Materia: IA
"""


import turtle as t
from random import random

"""
def draw_dotted_line():
    t.penup()
    for _ in range(10):
        t.dot()
        t.forward(10)
    t.hideturtle()

t.speed(0)
draw_dotted_line()
t.done()
"""

def draw_dotted_line(x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    
    if x1 == x2:  # para identificar si es una linea vertical
        t.setheading(90)  # cambia la orientcion con 90grados 
        while t.ycor() < y2:
            t.dot(5)
            t.forward(10)
    else:  # else para hacer la linea horizontal
        while t.xcor() < x2:
            t.dot(5)
            t.forward(10)
    
    t.hideturtle()

t.speed(3)  # Cambia la velocidad del dibujo
draw_dotted_line(-100, 0, 100, 0)  # este es una linea horizontal
draw_dotted_line(0, -100, 0, 100)  # linea vertical
t.done() #para mantener abierta la ventana de ejecucion del dibujo

