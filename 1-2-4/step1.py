import turtle as trtl
import random as rand
drawer = trtl
path_width = 5
wall_len = 25
wall_increment = 10
def spiral():
    drawer.speed(0)
    x = 10
    y = 10
    drawer.penup()
    drawer.goto(0,0)
    drawer.pendown()
    for step in range(26):
        if step <= 4:
            drawer.penup()
        else:
            drawer.left(90)
            draw_door()
            draw_barriers()
            drawer.forward(x + y - 30 - 10)
            y += 10

def draw_door():
    drawer.forward(10)
    drawer.penup()
    drawer.forward(10 * 2)
    drawer.pendown()
def draw_barriers():
    drawer.forward(40)
    drawer.left(90)
    drawer.forward(10 * 2)
    drawer.back(10 * 2)
    drawer.right(90)

def random():
    door = rand.randint(path_width * 2, (wall_len - path_width * 2))
    barrier = rand.randint(path_width * 2, (wall_len - path_width * 2))


spiral()
wn = trtl.Screen()
wn.mainloop()
