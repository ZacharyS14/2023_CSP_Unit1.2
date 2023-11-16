star = "*"
star2 = "*"
def outcome_stars():
    star = "*"
    star2 = "*"
    for step in range(5):
        print(star)
        star = star2 + (star)
outcome_stars()
