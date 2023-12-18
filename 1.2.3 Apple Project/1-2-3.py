#   a123_apple_1.py
import turtle as trtl
import random as rand
# -----setup-----
apple_image = "apple.gif"  # Store the file name of your shape
pear_image = "pear.gif"
wn = trtl.Screen()
drawer = trtl.Turtle()
global checkletter
global letter
letter = "a"
randint = int(rand.randint(0, 26))
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.addshape(pear_image)  # Make the screen aware of the new file
apple_letter_x_offset = 25
apple_letter_y_offset = 50
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
if randint < len(letter_list):
 randint = randint
else:
 randint = int(rand.randint(0, 26))
apple = trtl.Turtle()
apple.penup()
wn.tracer(False)
# -----functions-----
def draw_apple(active_apple, letter):
   active_apple.showturtle()
   active_apple.shape(apple_image)
   drawLetter(active_apple, letter)
   wn.update()
def drawLetter(active_apple, letter):
   drawer.penup()
   drawer.goto(active_apple.xcor() - apple_letter_x_offset, active_apple.ycor() - apple_letter_y_offset)
   drawer.color("white")
   drawer.clear()
   drawer.write(letter, font=("Arial", 55, "bold"))
def reset_apple(active_apple):
   if letter_list:
       letter = rand.choice(letter_list)
       letter_list.remove(letter)
       active_apple.goto(rand.randint(-270, 270), 160)
       print(letter_list)
       draw_apple(active_apple, letter)
def drop_apple():
   wn.tracer(True)
   apple.goto(apple.xcor(), apple.ycor() - 400)
   apple.hideturtle()
   wn.tracer(False)
   reset_apple(apple)
def checkA():
    global letter
    if letter == "a":
        drop_apple()
def checkB():
    global letter
    if letter == "b":
        drop_apple()
def checkC():
    global letter
    if letter == "c":
        drop_apple()
def checkD():
    global letter
    if letter == "d":
        drop_apple()
def checkE():
    global letter
    if letter == "e":
        drop_apple()
def checkF():
    global letter
    if letter == "f":
        drop_apple()
def checkG():
    global letter
    if letter == "g":
        drop_apple()
def checkH():
    global letter
    if letter == "h":
        drop_apple()
def checkI():
    global letter
    if letter == "i":
        drop_apple()
def checkJ():
    global letter
    if letter == "j":
        drop_apple()
def checkK():
    global letter
    if letter == "k":
        drop_apple()
def checkL():
    global letter
    if letter == "l":
        drop_apple()
def checkM():
    global letter
    if letter == "m":
        drop_apple()
def checkN():
    global letter
    if letter == "n":
        drop_apple()
def checkO():
    global letter
    if letter == "o":
        drop_apple()
def checkP():
    global letter
    if letter == "p":
        drop_apple()
def checkQ():
    global letter
    if letter == "q":
        drop_apple()
def checkR():
    global letter
    if letter == "r":
        drop_apple()
def checkS():
    global letter
    if letter == "s":
        drop_apple()
def checkT():
    global letter
    if letter == "t":
        drop_apple()
def checkU():
    global letter
    if letter == "u":
        drop_apple()
def checkV():
    global letter
    if letter == "v":
        drop_apple()
def checkW():
    global letter
    if letter == "w":
        drop_apple()
def checkX():
    global letter
    if letter == "x":
        drop_apple()
def checkY():
    global letter
    if letter == "y":
        drop_apple()
def checkZ():
    global letter
    if letter == "z":
        drop_apple()
# -----function calls-----
draw_apple(apple, "a")
wn.onkeypress(checkA, "a")
draw_apple(apple, "b")
wn.onkeypress(checkB, "b")
draw_apple(apple, "c")
wn.onkeypress(checkC, "c")
draw_apple(apple, "d")
wn.onkeypress(checkD, "d")
draw_apple(apple, "e")
wn.onkeypress(checkE, "e")
draw_apple(apple, "f")
wn.onkeypress(checkF, "f")
draw_apple(apple, "g")
wn.onkeypress(checkG, "g")
draw_apple(apple, "h")
wn.onkeypress(checkH, "h")
draw_apple(apple, "i")
wn.onkeypress(checkI, "i")
draw_apple(apple, "j")
wn.onkeypress(checkJ, "j")
draw_apple(apple, "k")
wn.onkeypress(checkK, "k")
draw_apple(apple, "l")
wn.onkeypress(checkL, "l")
draw_apple(apple, "m")
wn.onkeypress(checkM, "m")
draw_apple(apple, "n")
wn.onkeypress(checkN, "n")
draw_apple(apple, "o")
wn.onkeypress(checkO, "o")
draw_apple(apple, "p")
wn.onkeypress(checkP, "p")
draw_apple(apple, "q")
wn.onkeypress(checkQ, "q")
draw_apple(apple, "r")
wn.onkeypress(checkR, "r")
draw_apple(apple, "s")
wn.onkeypress(checkS, "s")
draw_apple(apple, "t")
wn.onkeypress(checkT, "t")
draw_apple(apple, "u")
wn.onkeypress(checkU, "u")
draw_apple(apple, "v")
wn.onkeypress(checkV, "v")
draw_apple(apple, "w")
wn.onkeypress(checkW, "w")
draw_apple(apple, "y")
wn.onkeypress(checkY, "y")
draw_apple(apple, "z")
wn.onkeypress(checkZ, "z")
wn.listen()
wn.bgpic("background.gif")
wn.mainloop()