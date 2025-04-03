import random
from turtle import Turtle, Screen
# Playing around with turtle

# Setup
turtle = Turtle()
turtle.ht()
screen = Screen()
screen.setup(width=1700, height=850)
turtle.speed(0)  # No animation delay

colors = ["red", "blue", "green", "yellow", "pink", "orange", "purple", "cyan", "grey", "brown", "black", "brown"]

# Move the turtle to the left before drawing shapes
turtle.penup()
turtle.goto(-600, 150)  # Move 400 pixels to the left
turtle.pendown()

# Shape Drawing
shape = 3
while shape <= 10:
    shape_degrees = 360 / shape
    random_color = random.choice(colors)
    turtle.color(random_color)
    for side in range(shape):
        turtle.forward(100)
        turtle.right(shape_degrees)
    shape += 1

# Random Walk (also moved to the left)
turtle.penup()
turtle.goto(-250, 0)  # Move further left and slightly down
turtle.pendown()

for a in range(100):
    random_direction = random.randint(1, 3)
    random_color = random.choice(colors)

    turtle.color(random_color)
    turtle.pensize(8)

    if random_direction == 1:
        turtle.right(90)
    elif random_direction == 2:
        turtle.left(90)
    else:
        turtle.forward(25)





screen.exitonclick()
