# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shapesize(spot_size)
spot.color(spot_color)
spot.fillcolor(spot_color)
#-----game functions--------
def spot_clicked( x, y):
    print("Hello World!")
#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()

wn.mainloop()