from turtle import Turtle
ALIGN ="center"
FONT = ("Arial",24,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shapesize(stretch_len=2,stretch_wid=2)
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.update_score()
       

    def update_score(self):
         self.write(f"score:{self.score}",align=ALIGN,font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!",align=ALIGN,font=FONT)


    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()
        


