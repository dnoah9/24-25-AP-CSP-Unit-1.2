# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl

import random as rand
from itertools import filterfalse

#-----game configuration----
spot_color = "red"
spot_size = 2
spot_shape = "circle"
clicks = 1
score = 0
font_setup = ("Arial", 20, "bold")
timer = 30
counter_interval = 1000
timer_up = False



#-----initialize turtle-----
spot = trtl.Turtle()
score_writer= trtl.Turtle()
counter =  trtl.Turtle()
spot.color(spot_color)
spot.fillcolor(spot_color)
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.speed(0)

#-----game functions--------
spot.penup()
def change_position():
    new_xpos = rand.randint(-400, 400)
    new_ypos = rand.randint(-300, 300)
    spot.goto(new_xpos,new_ypos)
def spot_clicked( x, y):
    update_score()
    change_position()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)


score_writer.penup()
score_writer.goto(-350, 300)
score_writer.hideturtle()


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
counter.penup()
counter.goto(300, 300)
counter.hideturtle()



#-----events----------------
spot.onclick(spot_clicked)

wn = trtl.Screen()
wn.bgcolor("purple")
wn.ontimer(countdown, counter_interval)
wn.mainloop()