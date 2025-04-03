import random
from turtle import Turtle, Screen
from random import Random
#trying out things

turtle = Turtle()
colors = ["red","blue","green","yellow","pink","orange","purple","cyan","grey","brown"]
shape = 3
while shape<=10:
    shape_degrees = 360/shape
    random_color = random.choice(colors)
    turtle.color(random_color)
    for side in range(shape):
        turtle.forward(100)
        turtle.right(shape_degrees)
    shape+=1

























screen = Screen()
screen.exitonclick()