import random
from turtle import Turtle, Screen
import turtle as t
import colorgram
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
#
# # Move the turtle to the left before drawing shapes
# turtle.penup()
# turtle.goto(-600, 150)  # Move 400 pixels to the left
# turtle.pendown()
#
# # Shape Drawing
# shape = 3
# while shape <= 10:
#     turtle.pensize(5)
#     shape_degrees = 360 / shape
#     # random_color = random.choice(colors)
#     # turtle.color(random_color)
#     random_color()
#     for side in range(shape):
#         turtle.forward(100)
#         turtle.right(shape_degrees)
#     shape += 1
# #------------------------ x x x x ----------------------------
#
# # Random Walk
# turtle.penup()
# turtle.goto(-250, 0)  # Move further left and slightly down
# turtle.pendown()
#
# directions = [0,90,180,270]
# turtle.pensize(8)
#
# for a in range(120):
#     # random_color = random.choice(colors)
#     # turtle.color(random_color)
#     random_color()
#     turtle.forward(25)
#     turtle.setheading(random.choice(directions))
# #------------------------ x x x x ----------------------------
#
# # Spirograph
# turtle.setheading(0)
# turtle.pensize(1)
#
# turtle.penup()
# turtle.goto(0, 0)  # Move further left and slightly down
# turtle.pendown()
#
# for angle in range(0,60):
#     random_color()
#     turtle.left(6)
#     turtle.circle(70)
# #------------------------ x x x x ----------------------------

#Final valuable painting
#
# colors = colorgram.extract("painting.jpg",40)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b=  color.rgb.b
#
#     color_tuple = (r,g,b)
#     rgb_colors.append(color_tuple)
#
# print(rgb_colors)
color_list_from_image =   [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]

turtle.penup()
turtle.goto(250, -150)

def drawing_painting():
    vertical_pos = -150
    for a in range(0,3):
        for b in range(0,10):
            random_color = random.choice(color_list_from_image)
            turtle.fd(50)
            turtle.dot(20,random_color)

        vertical_pos += 50
        turtle.goto(250, vertical_pos)

drawing_painting()

turtle.pendown()
screen.exitonclick()
