import time
import turtle
from turtle import Turtle


# turtle screen design
window=turtle.Screen()
turtle.bgcolor('yellow')

# turtle1 specifications
turtle1=Turtle()
turtle1.pensize(5)
turtle1.shapesize(2,2)
turtle1.color('brown')
turtle1.shape('turtle')
turtle1.penup()
turtle1.goto(-100,100)
turtle1.pendown()

# turtle2 specifications
turtle2=Turtle()
turtle2.pensize(5)
turtle2.shapesize(2,2)
turtle2.color('green')
turtle2.shape('turtle')
turtle2.penup()
turtle2.goto(30,100)
turtle2.pendown()

# turtle1 movements(making square)
turtle1.forward(80)
turtle1.speed(5)
turtle1.right(90)
turtle1.forward(80)
turtle1.right(90)
turtle1.forward(80)
turtle1.right(90)
turtle1.forward(80)

# turtle2 movements(making square)
turtle2.forward(80)
turtle2.speed(5)
turtle2.right(90)
turtle2.forward(80)
turtle2.right(90)
turtle2.forward(80)
turtle2.right(90)
turtle2.forward(80)
