# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl

#-----game configuration----
bob = trtl.Turtle()
bob_color = "yellow"
bob_shape = "circle"
bob_fillcolor = 2
#-----initialize turtle-----
bob.shape(bob_shape)
bob.fillcolor(bob_color)
bob.shapesize(bob_fillcolor)

#-----game functions--------
def onclick(f):
    print("bob was clicked")

#-----events----------------
bob.onclick()




wn = trtl.Screen()
wn.mainloop()