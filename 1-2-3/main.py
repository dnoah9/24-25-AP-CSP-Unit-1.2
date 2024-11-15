#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
ground_height = -150
apple_letter_x_offset = -25
apple_letter_y_offset = -50
drawer = trtl.Turtle()
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drop_apple():
  apple.goto(apple.xcor(), ground_height)

def draw_an_a():
  drawer.color("white")
  drawer.write("A", font=("Arial", 74, "bold"))

#-----function calls-----
drawer.hideturtle()
apple.penup()
draw_apple(apple)
draw_an_a()
wn.onkeypress(drop_apple, "a")
wn.listen()
wn.bgpic("background.gif")
trtl.mainloop()
