
from myfunctions import *
from random import randint
turtle.colormode(255)

bob.speed(0)
bob.width(2)

'''
# circles design 1
turtle.bgcolor("cyan")
num = randint(2, 8)
border = "red"
fill = (255, 255, 0)

for times in range( num ):
  circle(20, border, fill )
  bob.forward(50)
  bob.right(15)



# circles design 2
turtle.bgcolor("black")
num = randint(10, 20)
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)
border = "yellow"
fill = (r,g,b)

for times in range( num ):
  circle(20, border, fill )
  bob.forward(50)
  bob.right(20)

'''

# circles design 3
turtle.bgcolor("black")
num = randint(10, 50)


for times in range( num ):
  sides = randint(3,10)
  r = randint(100,100)
  g = randint(0, 100)
  b = randint(100, 255)
  border = (r,g,b)
  fill = (r,g,b)
  x = randint(-300, 300)
  y = randint(-300, 300)
  radius = randint(5, 30)
  polygon(sides, 50, fill )
  jump(x,y)

 

