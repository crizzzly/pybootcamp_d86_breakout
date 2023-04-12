from turtle import Turtle

MOVE_VAL = 25


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.start_pos = position
        print(f"paddle size: {self.turtlesize()}, {self.screen.yscale}")

    def go_right(self):
        new_x = self.xcor() + MOVE_VAL
        if -310 < new_x < 310:
            self.hideturtle()
            self.goto(new_x, self.ycor())
            self.showturtle()

    def go_left(self):
        new_x = self.xcor() - MOVE_VAL
        if -310 < new_x < 310:
            self.hideturtle()
            self.goto(new_x, self.ycor())
            self.showturtle()

    def shrink(self):
        self.shapesize(stretch_wid=1, stretch_len=4)

    def reset_position(self):
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(self.start_pos)