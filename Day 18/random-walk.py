import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)

def random_colour():
     r = random.randint(0,255)
     g= random.randint(0,255)
     b = random.randint(0,255)
     randomize_color = (r,g,b)
     return randomize_color



########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", 
           "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.width(10)
direction = [0,90,180,270]

def random_walk():
     tim.forward(20)
     tim.setheading(random.choice(direction))
for _ in range(200):
     tim.color(random_colour())
     tim.speed("fastest")
     random_walk()

        


screen = Screen()
screen.exitonclick()


