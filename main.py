from turtle import Screen, Turtle
from paddle import Paddle
from brick import Brick
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=650, height=800)
screen.title("Breakout - By C. Rost")
screen.tracer(0)

upper_border = 350
left_border = -280
right_border = 280

paddle = Paddle((0, -350))
ball = Ball()
scoreboard = Scoreboard()
bricks = []
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan"]
brick_distance = 60
x1 = left_border + 25
y1 = upper_border - brick_distance
for j in range(len(colors)): 
    y_val = y1  - j * 25
    for i in range(7):
        # first brick should be drawn at -260 (left corner)
        # brick is 40 x 20 px
        x_val = x1 + i * (brick_distance + 25)
        b = Brick(x_val, y_val, colors[j])
        bricks.append(b)

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 40 and abs(a.ycor() - b.ycor()) < 10


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.xcor() > right_border or ball.xcor() < left_border:
        ball.bounce_x()
        print("wall")
    if ball.ycor() > upper_border:
        print("wall")
        ball.bounce_y()

    #Detect collision with paddle
    if is_collided_with(ball, paddle):
        print("paddle")
        ball.bounce_y()
    
    # Detech collosion with brick
    for br in bricks:
        if is_collided_with(ball, br):
            print("brick")
            ball.bounce_y()
            scoreboard.point()
            br.delete()
            bricks.remove(br)


    #Detect paddle misses:
    if ball.ycor() < -400:
        scoreboard.reduce_life()
        if scoreboard.lifes <= 0:
            game_is_on = False
       
        ball.reset_position(paddle.xcor(), -320)

game_over = Turtle()
game_over.color("white")
game_over.pu()
game_over.goto(0, 0)
game_over.write("GAME OVER", align="center", font=("Courier", 50, "normal"))
screen.exitonclick()