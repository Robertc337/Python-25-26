import turtle
bob = turtle.Turtle()

def comet(distance, angle):
  for times in range(10):
    bob.width(times)
    bob.forward(distance)
    bob.left(angle)

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()

def stair (distance,amount):
  for times in range( amount ):
    bob.forward( distance )
    bob.left( 90 )
    bob.forward( distance )
    bob.right( 120 )

def spiral():
  for times in range (10):
    bob.forward(times*2)
    bob.left(30)
    
