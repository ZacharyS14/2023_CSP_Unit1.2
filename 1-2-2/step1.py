# a121_catch_a_turtle.py
import turtle as trtl
import random as rand
import leaderboard as lb
#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----game configuration----
bob = trtl.Turtle()
score_writer = trtl.Turtle()
counter = trtl.Turtle()
bob_color = "yellow"
bob_shape = "circle"
bob_fillcolor = 2
score = 0
font_setup = ("Arial", 20, "normal")
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input ("Please enter your name:")
#-----initialize turtle-----
bob.shape(bob_shape)
bob.fillcolor(bob_color)
bob.shapesize(bob_fillcolor)
score_writer.penup()
counter.penup()
score_writer.goto(-450, 360)
counter.goto(340,360 )
#-----game functions--------
def bob_clicked(x, y):
    if timer_up is False:
        update_score()
        change_position()
    else:
        counter.hideturtle()
def change_position():
    bob.penup()
    new_xpos = rand.randint(1, 400)
    new_ypos = rand.randint(1, 400)
    bob.goto(new_xpos, new_ypos)
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
    global score
    global spot

    # get the names and scores from the leaderboard file
    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)

    # show the leaderboard with or without the current player
    if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

    else:
        lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)


#-----events----------------
bob.onclick(bob_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()