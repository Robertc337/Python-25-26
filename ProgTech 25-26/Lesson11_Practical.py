import turtle
bob=turtle.Turtle()

bob.speed(0)

for times in range(100):
     bob.circle(times * 5)
     
     bob.forward(times * 8)
     bob.left(120)
     bob.right(5)
     bob.left(100)

     
