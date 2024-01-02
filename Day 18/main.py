import turtle
from turtle import Turtle,Screen
import random

doly_the_turtle = Turtle()
doly_the_turtle.shape("turtle")
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.left(-90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# for t in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# doly_the_turtle.forward(10)
# for t in range(50):
#     doly_the_turtle.forward(10)
#     doly_the_turtle.pu()
#     doly_the_turtle.forward(10)
#     doly_the_turtle.pd()


    # Drawing shapes, square, circle, pentagon, hexagon
number_of_sides_of_shape = 360
colors = ["sienna","magenta","maroon","chartreuse","seashell","dark olive green","midnight blue"]


def draw_shapes(num_of_sides):
    angle = 360 / num_of_sides
    for t in range(num_of_sides):
        doly_the_turtle.forward(100)
        doly_the_turtle.right(angle)
for shapes in range(3,11):
    doly_the_turtle.color(random.choice(colors))
    draw_shapes(shapes)








screen = Screen()
screen.exitonclick()