import turtle as trtl
import random as rand
# maze configuration variables
num_sides = 25
path_width = 15
wall_color = "black"

# config maze
drawer = trtl.Turtle()
drawer.pensize(5)
drawer.pencolor(wall_color)
drawer.speed("fastest")

def drawSpiral():
    wall_len = path_width
    for w in range(num_sides):
        wall_len += path_width

        if (w > 4):
            # Initial turn for painter to be in the correct direction
            drawer.left(90)
            #create random #
            randomnum = rand.randint(1,2)
            if randomnum == 1:
                print("door first")
                draw_door()
                draw_barrier()
            else:
                print("barrier first")
                draw_barrier()
                draw_door()
            drawer.forward(wall_len - 10 - path_width - 40)

def draw_door():
    drawer.forward(10)
    drawer.penup()
    drawer.forward(path_width * 2)
    drawer.pendown()

def draw_barrier():
    # draw barrier wall
    drawer.forward(40)
    drawer.left(90)
    drawer.forward(path_width * 2)
    drawer.backward(path_width * 2)
    drawer.right(90)

drawSpiral()
drawer.hideturtle()

wn = trtl.Screen()
wn.mainloop()