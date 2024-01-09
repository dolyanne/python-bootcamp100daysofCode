import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
def random_colour():
     r = random.randint(0,255)
     g= random.randint(0,255)
     b = random.randint(0,255)
     randomize_color = (r,g,b)
     return randomize_color

for _ in range (200):
     tim.color(random_colour())
     tim.circle(100)
     tim.setheading(tim.heading()+10)
     
     

screen = Screen()
screen.exitonclick()