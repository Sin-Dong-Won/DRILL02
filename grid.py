import turtle
turtle.shape('turtle')
turtle.left(90)
a = 90

for grid in range(5): 
 turtle.forward(500) 
 turtle.right(a)
 turtle.forward(100)
 turtle.right(a)
 a = a * -1

turtle.forward(500)
turtle.right(90)
turtle.forward(500)
turtle.right(90)

for grid in range(5): 
 turtle.forward(100)
 turtle.left(a)
 turtle.forward(500)
 turtle.right(a)
 a = a * -1
