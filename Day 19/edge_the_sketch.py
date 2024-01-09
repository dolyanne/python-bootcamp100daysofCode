from turtle import Turtle, Screen

doly = Turtle()

screen = Screen()
screen.listen()
def forward():
    doly.forward(10)
def backward():
    doly.backward(10)
def anti_clockwise():
    doly.left(10)
def clockwise():
    doly.right(10)
def clear():
    doly.clear()
    doly.pu()
    doly.home()
    doly.pd()




screen.onkey(fun=forward,key = "w")
screen.onkey(fun=backward,key = "s")
screen.onkey(fun=anti_clockwise,key = "a")
screen.onkey(fun=clockwise,key = "d")
screen.onkey(fun=clear,key = "c")

screen.exitonclick()