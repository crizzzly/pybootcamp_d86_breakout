from turtle import Turtle

class Brick(Turtle):
    def __init__(self, posx, posy, col):
        super().__init__()
        self.shape("square")
        self.color(col)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.goto(posx, posy)
    
    def delete(self):
        self.goto(-350, -450)