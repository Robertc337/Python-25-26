from myfunctions import *
from random import randint
turtle.colormode(255)
turtle.tracer(0)

bob.speed(0)
bob.width(2)

turtle.bgcolor("white")
bob.color("black")
for times in range(5000):
    bob.forward(times)
    bob.right(131)
for times in range(15):
  x = randint(-400,400)
  y = randint(-400,400)
  jump(x,y)
  bob.color("light blue")
  bob.width(15)
  star()
for times in range(15):
  x = randint(-1000,1000)
  y = randint(-400,400)
  jump(x,y)
  bob.color("white")
  bob.width(15)
  star()
