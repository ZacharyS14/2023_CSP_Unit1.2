# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
bob = trtl.Turtle()
bob_color = "yellow"
bob_shape = "circle"
bob_fillcolor = 2
score = 0
#-----initialize turtle-----
bob.shape(bob_shape)
bob.fillcolor(bob_color)
bob.shapesize(bob_fillcolor)

#-----game functions--------
def bob_clicked(x, y):
    change_position()
def change_position():
    bob.penup()
    new_xpos = rand.randint(1, 400)
    new_ypos = rand.randint(1, 400)
    bob.goto(new_xpos, new_ypos)
def update_score():
#-----events----------------
bob.onclick(bob_clicked)



wn = trtl.Screen()
wn.mainloop()