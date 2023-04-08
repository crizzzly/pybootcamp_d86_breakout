from turtle import Turtle


class Scoreboard(Turtle):
    fontsize = 40

    def __init__(self, pl):
        super().__init__()
        self.game_over = False
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.highscore = 0
        self.lives = 1
        self.level = 1
        self.player = pl
        self.hits = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        if self.player == 0:
            x1 = -290
            y1 = 340
            x2 = -280
            y2 = 310
            align = 'left'
        else:
            x1 = 90
            y1 = 340
            x2 = 100
            y2 = 310
            align = 'right'
        self.clear()
        self.goto(x1, y1)
        self.write(self.level, align=align, font=("Courier", self.fontsize-20, "normal"))
        self.goto(x2, y2)
        self.write(f"{self.score:03d} ♥️ {self.lives}", align="left", font=("Courier", self.fontsize, "normal"))
        # self.write(f"{self.score:03d}", align="left", font=("Courier", self.fontsize, "normal"))
        # self.goto(-130, 310)
        # self.write(f"♥️ {self.lives}", align="center", font=("Courier", self.fontsize, "normal"))

    def point(self, val):
        self.score += val
        self.update_scoreboard()
     
    def point_less(self):
        self.score -= 1
        self.update_scoreboard()
    
    def reduce_life(self):
        self.lives -= 1
        if self.lives <= 0:
            self.game_over = True
        self.update_scoreboard()


    def level_up(self):
        self.level += 1
        if self.level > 2:
            self.game_over = True
            self.reset_scoreboard()
            if self.score > self.highscore:
                self.highscore = self.score

    def reset_scoreboard(self):
        self.hits = 0
        self.score = 0
        self.lives = 3
        self.level = 1
        self.update_scoreboard()



        
