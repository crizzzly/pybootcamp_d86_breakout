from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1
        self.stopped = False

    def move(self):
        if not self.stopped:
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)

    def toggle_stopp(self):
        self.stopped = True if not self.stopped else False


    def bounce_y(self) :
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    
    def increase_speed(self):
        # self.move_speed += 0.5
        self.x_move += 1
        self.y_move += 1

    def reset_position(self, x, y):
        self.hideturtle()
        # self.penup()
        self.goto(x, y)
        self.move_speed = 0.1
        self.showturtle()
        self.bounce_y()
