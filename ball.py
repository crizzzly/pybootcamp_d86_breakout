from turtle import Turtle

START_SPEED = 1.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = START_SPEED
        self.stopped = False
        self.speed(10)


    def move(self):
        if not self.stopped:
            new_x = self.xcor() + self.x_move*self.move_speed
            new_y = self.ycor() + self.y_move*self.move_speed
            self.hideturtle()
            self.goto(new_x, new_y)
            self.showturtle()

    def toggle_stopp(self):
        self.stopped = True if not self.stopped else False


    def bounce_y(self):
        self.y_move *= -1
        # self.move_speed *= 1.1
        print(f"bounce_y speed{self.move_speed}")

    def bounce_x(self):
        self.x_move *= -1
        print(f"bounce_x speed{self.move_speed}")

    def increase_speed(self):
        # if self.x_move > 0:
        #     self.x_move += 1
        # else:
        #     self.x_move -= 1
        # if self.y_move > 0:
        #     self.y_move += 1
        # else:
        #     self.y_move -= 1
        self.move_speed *= 1.1
        print(f"speed{self.move_speed}")

    def reset_position(self, x, y):
        self.hideturtle()
        # self.penup()
        self.goto(x, y)
        self.showturtle()
        self.bounce_y()


    def reset_speed(self):
        self.move_speed = START_SPEED
