import turtle
import random

def Drunken_move():
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(50,100))
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(Drunken_move, ' ')
turtle.onkey(restart, 'Escape')
turtle.listen()
 
