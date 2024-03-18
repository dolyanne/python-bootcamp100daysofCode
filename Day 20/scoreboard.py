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
        self.high_score =0
        # read highscore form data file
        with open("Day 20/data.txt",mode="r") as file:
            self.high_score = int(file.read())
        self.update_score()
       

    def update_score(self):
         self.clear()
         self.write(f"score:{self.score} highscore:{self.high_score}",align=ALIGN,font=FONT)
    def reset(self) :
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day 20/data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
            
        self.score = 0
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!",align=ALIGN,font=FONT)


    def increase_score(self):
        self.score +=1
        # self.clear()
        self.update_score()
        


