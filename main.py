import turtle as t
from random import random

#for i in range(100):
 #   steps = int(random() * 100)
  #  angle = int(random() * 360)
   # t.right(angle)
    #t.fd(steps)

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
