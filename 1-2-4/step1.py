import turtle as trtl
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
    trtl.speed(0)
    x = 10
    y = 10
    for step in range(25):
        trtl.left(90)
        trtl.forward(x + y)
        y += 10
        draw_door()
        trtl.forward(x)
        trtl.penup()
        trtl.forward(x * 2)
        trtl.pendown()
def draw_door():
    trtl.forward(40)
    trtl.left(90)
    trtl.forward(10 * 2)
    trtl.back(10 * 2)
    trtl.right(90)
def draw_barriers():
    trtl.forward(40)
    trtl.left(90)
    trtl.forward(10 * 2)
    trtl.back(10 * 2)
    trtl.right(90)

spiral()
wn = trtl.Screen()
wn.mainloop()
