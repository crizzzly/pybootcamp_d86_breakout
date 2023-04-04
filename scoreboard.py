from turtle import Turtle


class Scoreboard(Turtle):
    fontsize = 30

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lifes = 3
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 350) 
        self.write(f"💠 {self.score}", align="left", font=("Courier", self.fontsize, "normal"))
        self.goto(0, 350)
        self.write(f"♥️ {self.lifes}", align="center", font=("Courier", self.fontsize, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()
     
    def point_less(self):
        self.score -= 1
        self.update_scoreboard()
    
    def reduce_life(self):
        self.lifes -= 1
        self.update_scoreboard()

        
