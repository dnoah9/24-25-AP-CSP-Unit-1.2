# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl

import random as rand


#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0
clicks = 1
#-----initialize turtle-----
spot = trtl.Turtle()
spot.color(spot_color)
spot.fillcolor(spot_color)
spot.shape(spot_shape)
spot.shapesize(spot_size)

#-----game functions--------
spot.penup()
def change_position():
    new_xpos = rand.randint(-400, 400)
    new_ypos = rand.randint(-300, 300)
    spot.goto(new_xpos,new_ypos)
def spot_clicked( x, y):
   change_position()
update_score
print(score)

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()