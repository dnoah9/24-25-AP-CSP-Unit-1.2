import turtle
import turtle as trtl
pong_ball=turtle.Turtle()
wn = trtl.Screen()
wn.bgcolor('lightblue')

#player list
Player1_score=0
Player2_score=0

#game configuration







#left paddle
leftpaddle=trtl.Turtle()
leftpaddle.speed(0)
leftpaddle.penup()
leftpaddle.goto(-400,0)
#left paddle shape/size
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)


#right paddle
rightpaddle = trtl.Turtle()
rightpaddle.speed(0)
rightpaddle.penup()
rightpaddle.goto(400,0)

#right paddle shape/size
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)


#pong
pong_ball.goto(0,0)
pong_ball.shape("circle")
pong_ball.color("white")
pong_ball.shapesize(stretch_wid=1,stretch_len=1)




wn.mainloop()