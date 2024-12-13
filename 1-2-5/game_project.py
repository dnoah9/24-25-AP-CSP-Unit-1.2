import turtle

wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.bgcolor("lightblue")
wn.tracer(0)

# drawScore
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Player 1: 0      Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Score
score_1 = 0
score_2 = 0

# leftpaddle
leftpaddle = turtle.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-370, 0)

# rightpaddle
rightpaddle = turtle.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(370, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1


# movement
def paddle_1_up():
    y = leftpaddle.ycor()
    y += 20
    leftpaddle.sety(y)


def paddle_1_down():
    y = leftpaddle.ycor()
    y -= 20
    leftpaddle.sety(y)


def paddle_2_up():
    y = rightpaddle.ycor()
    y += 20
    rightpaddle.sety(y)


def paddle_2_down():
    y = rightpaddle.ycor()
    y -= 20
    rightpaddle.sety(y)


# key inputs
wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")

# mainloop
while True:
    wn.update()
    # game over
    if score_1 == 20:
        pen.clear()
        ball.dx = 0
        ball.dy = 0
        ball.goto(0, 0)
        pen.write("Player 1 wins", align="center", font=("arial", 32, "normal"))

        if score_2 == 20:
            pen.clear()
        ball.dx = 0
        ball.dy = 0
        ball.goto(0, 0)
        pen.write("Player 2 wins", align="center", font=("arial", 32, "normal"))

        # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # walls
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= 1

    if ball.ycor() < 290:
        ball.sety(-290)
        ball.dy *= 1

    if ball.xcor() > 390:
        ball.goto(390, ball.xcor())
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}   Player 2: {}".format(score_1, score_2), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(-390, ball.xcor())
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}   Player 2: {}".format(score_1, score_2), align="center",
                  font=("Courier", 24, "normal"))

    # collision
    if 340 < ball.xcor() < 350 and (rightpaddle.ycor() + 40 > ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if -340 > ball.xcor() > -350 and (leftpaddle.ycor() + 40 > ball.ycor() > leftpaddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
    if 340 < ball.ycor() < 290 and (rightpaddle.xcor() + 40 > ball.xcor() > rightpaddle.xcor() - 40):
        ball.sety(340)
        ball.dx *= -1

    if -340 > ball.xcor() > -290 and (leftpaddle.xcor() + 40 > ball.xcor() > leftpaddle.xcor() - 40):
        ball.sety(-340)
        ball.dx *= -1


