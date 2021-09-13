import turtle
import random

def left_move():
    turtle.sethead(180)
    turtle.forward(50)
    turtle.stamp()
    
def right_move():
    turtle.sethead(0)
    turtle.forward(50)
    turtle.stamp()

def up_move():
    turtle.sethead(90)
    turtle.forward(50)
    turtle.stamp()
    
def down_move():
    turtle.sethead(270)
    turtle.forward(50)
    turtle.stamp()

def reset():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(left_move, 'a')
turtle.onkey(right_move, 'd')
turtle.onkey(up_move, 'w')
turtle.onkey(down_move, 's')
turtle.onkey(reset, 'Escape')

turtle.listen()
    
