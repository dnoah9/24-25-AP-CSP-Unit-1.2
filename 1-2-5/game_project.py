
import turtle as trtl



#player list
Player1_score=0
Player2_score=0





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

wn = trtl.Screen()
wn.bgcolor('black')
wn.mainloop()