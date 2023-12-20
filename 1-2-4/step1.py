import turtle as trtl

drawer = trtl
"""
x = starting distance
y = incremental distance

1.go forward x
2.turn left 90 degrees
3. go forward x + y
4. turn left 90 degrees


1. forward x


"""

def spiral():
    drawer.speed(0)
    x = 10
    y = 10
    for step in range(25):
        if step >= 4:
            drawer.left(90)
            draw_door()
            draw_barriers()
            drawer.forward(x + y)
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
def door_random():
    door = rand.randint()

spiral()
wn = trtl.Screen()
wn.mainloop()
