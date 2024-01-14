from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
x_positions =[-40,-20,0]
snakes =[]
for i in range(0,3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.pu()
    snake.goto(x=x_positions[i], y=0)
    snakes.append(snake)
 
game_is_on =True
while game_is_on:
    for s in snakes:
        s.forward(20)











screen.exitonclick()