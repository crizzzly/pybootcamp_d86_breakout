import tkinter as tk
from turtle import Screen, Turtle
from paddle import Paddle
from brick import Brick
from ball import Ball
from scoreboard import Scoreboard
import time

UPPER_BORDER = 300
LEFT_BORDER = -320
RIGHT_BORDER = 320
SCREEN_WIDTH = 660
SCREEN_HEIGHT = 750
LEFT_BORDER_BRICKS = -280

POINTS = {
    "cyan": 1,
    "purple": 2,
    "blue": 3,
    "green": 4,
    "yellow": 5,
    "orange": 6,
    "red": 7
}


def is_collided_with(item_a, item_b):
    w, h = 0, 0
    if item_b.turtlesize()[1] == 5:
        w = 60
    elif item_b.turtlesize()[1] == 4:
        w = 40
    if item_b.turtlesize()[0] == 1:
        h = 13
    elif item_b.turtlesize()[0] < 1:
        h = 7

    return abs(item_a.xcor() - item_b.xcor()) < w and abs(item_a.ycor() - item_b.ycor()) < h



class Breakout:
    def __init__(self):
        self.game_over = False
        self.game_is_on = True
        self.is_paused = False
        self.single_player = True

        self.paddle_is_small = False
        self.hit_yellow = False
        self.hit_red = None
        self.hit_upper_wall = False

        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.title("Breakout - By C. Rost")
        self.screen.tracer(0)

        self.canvas = self.screen.getcanvas()
        self.timer_id = None

        self.pause = Turtle()
        self.start_splash = Turtle()
        self.gme_ovr = Turtle()
        self.count = Turtle()
        self.player_start_text = Turtle()

        self.paddle = Paddle((0, -330))
        self.ball = Ball()
        self.players =[Scoreboard(0), Scoreboard(1)]
        self.active_player = 0

        self.screen.onkey(self.paddle.go_left, "Left")
        self.screen.onkey(self.paddle.go_right, "Right")
        self.screen.onkey(self.toggle_gameplay, "space")
        self.screen.onkey(self.set_one_player, "a")
        self.screen.onkey(self.set_two_player, "b")
        self.screen.onkey(self.reload_game, 'y')
        self.screen.listen()

        self.bricks = []
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan"]

        self.brick_distance = 60
        self.x1 = LEFT_BORDER_BRICKS + 25
        self.y1 = UPPER_BORDER - self.brick_distance

        self.seconds_to_start = 3
        self.count_secs = self.seconds_to_start

        self.brick_hits = 0
        self.frame = 0
        self.paddle_frame = 0
        self.brick_frame = 0

        # Show Splash Screen before drawing game
        self.splash_screen()

    def toggle_gameplay(self):
        self.is_paused = not self.is_paused
        if not self.game_is_on:
            self.player_start_text.clear()
            self.game_is_on = True
            self.play_game()
        print(f'PAUSED = {self.is_paused}')

    def reload_game(self):
        self.players[self.active_player].hits = 0
        self.paddle.reset_position()
        self.ball.reset_position(self.paddle.xcor(), -310)
        self.hit_yellow = False
        self.hit_upper_wall = False
        self.hit_red = False
        self.draw_bricks()
        self.draw_frame()
        if self.game_over:
            self.ball.reset_speed()
            self.gme_ovr.clear()
            for i in range(len(self.players)):
                self.players[i].reset_scoreboard()
            self.game_over = False

        self.screen.update()
        self.ready_player()

    def run_timer(self):
        if self.seconds_to_start >= 0:
            self.seconds_to_start -= 1

    def update(self):
        print(f"update: {self.seconds_to_start}")
        self.run_timer()
        self.count.clear()
        if self.seconds_to_start >= 0:
            self.count.write(f"{self.seconds_to_start}", align="center", font=("Courier", 50, "normal"))
            self.screen.ontimer(self.update, 1000)
            # self.timer_id = self.canvas.after(1000, self.update)

        else:
            print("stop counting")
            # self.canvas.after_cancel(self.timer_id)
            self.player_start_text.clear()
            self.game_is_on = True
            self.play_game()

    def ready_player(self):
        print(f"starting counter for player{self.active_player+1}")

        self.seconds_to_start = self.count_secs
        self.count.clear()
        self.count.hideturtle()
        self.count.color("white")
        self.count.pu()
        self.count.goto(0, -150)

        p = "ONE" if self.active_player == 0 else "TWO"
        self.player_start_text.hideturtle()
        self.player_start_text.color("white")
        self.player_start_text.pu()
        self.player_start_text.goto(0, -50)
        self.player_start_text.write(f"READY PLAYER {p}?", align='center', font=("Courier", 50, "normal"))

        self.update()

    def set_one_player(self):
        print("One Player")
        self.start_splash.clear()
        self.single_player = True

        self.reload_game()
        self.ready_player()

    def set_two_player(self):
        print("Two Player")
        self.start_splash.clear()
        self.single_player = False
        self.reload_game()
        self.ready_player()

    def game_over_screen(self):
        self.gme_ovr.color("white")
        self.gme_ovr.hideturtle()
        self.gme_ovr.pu()
        self.gme_ovr.goto(0, 0)
        self.gme_ovr.write("GAME OVER", align="center", font=("Courier", 50, "normal"))
        self.gme_ovr.goto(0, -50)
        self.gme_ovr.write("New game? 'y'\nExit on click", align="center", font=("Courier", 25, "normal"))
        self.screen.exitonclick()

    def splash_screen(self):
        self.start_splash.hideturtle()
        self.start_splash.color("white")
        self.start_splash.pu()
        self.start_splash.goto(0, 50)
        self.start_splash.write("BREAKOUT", align='center', font=("Courier", 50, "normal"))
        self.start_splash.goto(0, 0)
        self.start_splash.write("Enter 'a' to play in single modus\n"
                                "'b' to play with two players.", align='center', font=("Courier", 15, "normal"))
        self.screen.exitonclick()

    def draw_bricks(self):
        for j in range(len(self.colors)):
            y_val = self.y1 - j * 25
            for i in range(7):
                # first brick should be drawn at -260 (left corner)
                # brick is 40 x 20 px
                x_val = self.x1 + i * (self.brick_distance + 25)
                b = Brick(x_val, y_val, self.colors[j])
                self.bricks.append(b)

    ################### FRAME ###################

    @staticmethod
    def draw_frame():
        frame = Turtle()
        frame.hideturtle()
        frame.color('grey')
        frame.pu()
        ################### LEFT SIDE ###################
        frame.goto(LEFT_BORDER - 15, SCREEN_HEIGHT / 2)
        frame.setheading(180)
        frame.pd()
        frame.begin_fill()
        for _ in range(2):
            frame.fd(30)
            frame.left(90)
            frame.fd(SCREEN_HEIGHT)
            frame.left(90)
        frame.end_fill()
        frame.pu()
        ################### MIDDLE ###################
        frame.goto(-325, UPPER_BORDER)
        frame.setheading(0)
        frame.pd()
        frame.begin_fill()
        for _ in range(2):
            frame.fd(SCREEN_WIDTH)
            frame.left(90)
            frame.fd(5)
            frame.left(90)
        frame.end_fill()
        frame.pu()
        ################### RIGHT SIDE ###################
        frame.goto(RIGHT_BORDER + 15, SCREEN_HEIGHT / 2)
        frame.setheading(0)
        frame.pd()
        frame.begin_fill()
        for _ in range(2):
            frame.fd(30)
            frame.right(90)
            frame.fd(SCREEN_HEIGHT)
            frame.right(90)
        frame.end_fill()
        frame.pu()


    def other_player(self):
        return 1 if self.active_player == 0 else 0

    # TODO: Check Ball Speed
    def play_game(self):
        if self.single_player:
            self.players[1].clear()
            self.players[1].game_over = True

        if self.timer_id is not None:
            self.canvas.after_cancel(self.timer_id)

        while self.game_is_on:
            if self.is_paused:
                self.screen.update()
                self.pause.color("white")
                self.pause.hideturtle()
                self.pause.pu()
                self.pause.goto(0, -50)
                self.pause.write("PAUSE", align="center", font=("Courier", 100, "normal"))
            else:
                self.screen.update()
                self.frame += 1
                self.pause.clear()
                self.ball.move()

                # Detect collision with wall
                if self.ball.xcor() > RIGHT_BORDER or self.ball.xcor() < LEFT_BORDER:
                    print("Side Wall")
                    self.ball.bounce_x()

                # Detect collision with upper wall
                if self.ball.ycor() > UPPER_BORDER:
                    print("Upper Wall")
                    self.ball.bounce_y()
                    # paddle shrinks to one-half its size after the ball
                    # has broken through the red row and hit the upper wall
                    if self.hit_upper_wall is False and self.hit_red is True:
                        self.hit_upper_wall = True
                        self.paddle.shrink()

                # Detect collision with paddle
                if is_collided_with(self.ball, self.paddle):
                    print("paddle")
                    if self.frame - self.paddle_frame > 1:
                        self.ball.bounce_y()
                    self.paddle_frame = self.frame

                # Detect collision with brick
                for br in self.bricks:
                    if is_collided_with(self.ball, br):
                        if self.frame - self.brick_frame > 1:
                            self.brick_frame = self.frame
                            br.delete()
                            self.bricks.remove(br)
                            self.players[self.active_player].hits += 1
                            print(f"Brick {self.players[self.active_player].hits}")
                            self.ball.bounce_y()
                            self.players[self.active_player].point(POINTS[br.color()[0]])


                            # if all bricks are gone
                            if len(self.bricks) == 0:
                                self.players[self.active_player].level_up()
                                if not self.players[self.active_player].game_over:
                                    self.game_is_on = False
                                    self.reload_game()
                                else:
                                    self.game_is_on = False
                                    self.game_over_screen()

                            # increase speed every 4th and 12th brick and if the first yellow brick was hit
                            if self.players[self.active_player].hits == 4 or self.players[self.active_player].hits == 12:
                                self.ball.increase_speed()
                                print(f"Hit {self.players[self.active_player].hits} - increasing speed")
                            if "yellow" in br.color() and self.hit_yellow == False:
                                self.ball.increase_speed()
                                print("Hit Yellow Brick")
                                self.hit_yellow = True
                            if "red" in br.color():
                                self.hit_red = True

                # Detect paddle misses:
                if self.ball.ycor() < -400:
                    print("ball out ")
                    self.players[self.active_player].reduce_life()
                    self.ball.reset_position(self.paddle.xcor(), -320)

                    # end game if both are game over
                    if self.players[self.active_player].game_over and self.players[self.other_player()].game_over:
                        self.game_is_on = False
                        self.game_over = True
                        self.game_over_screen()

                    # set other player to active if he's not game over
                    elif self.players[self.active_player].game_over:
                        self.active_player = self.other_player()
                        print(f"switching to player {self.active_player}")
                        self.game_is_on = False
                        self.reload_game()
                        self.ready_player()






if __name__ == "__main__":
    Breakout()
