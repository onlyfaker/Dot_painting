import random
from turtle import Turtle, Screen
import turtle as t
# Playing around with turtle

# Setup
turtle = Turtle()
turtle.ht()
screen = Screen()
screen.setup(width=1700, height=850)
turtle.speed(0)  # No animation delay
t.colormode(255)

#funciton for random RGB colors and not just a list of colors
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return turtle.pencolor(r,g,b)

# Move the turtle to the left before drawing shapes
turtle.penup()
turtle.goto(-600, 150)  # Move 400 pixels to the left
turtle.pendown()

# Shape Drawing
shape = 3
while shape <= 10:
    turtle.pensize(5)
    shape_degrees = 360 / shape
    # random_color = random.choice(colors)
    # turtle.color(random_color)
    random_color()
    for side in range(shape):
        turtle.forward(100)
        turtle.right(shape_degrees)
    shape += 1

# Random Walk (also moved to the left)
turtle.penup()
turtle.goto(-250, 0)  # Move further left and slightly down
turtle.pendown()

directions = [0,90,180,270]
turtle.pensize(8)

for a in range(120):
    # random_color = random.choice(colors)
    # turtle.color(random_color)
    random_color()
    turtle.forward(25)
    turtle.setheading(random.choice(directions))

# Spirograph
turtle.setheading(0)
turtle.pensize(1)

turtle.penup()
turtle.goto(0, 0)  # Move further left and slightly down
turtle.pendown()

for angle in range(0,60):
    random_color()
    turtle.left(6)
    turtle.circle(70)

screen.exitonclick()
