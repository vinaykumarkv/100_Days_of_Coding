"""This program will run only in Reeborg's world website: https://www.reeborg.ca/reeborg.html"""

while not at_goal():
    while front_is_clear():
        move()
    while not front_is_clear() and is_facing_north():
         turn_left()
         turn_left()
         turn_left()
    while not front_is_clear() and wall_on_right():
        turn_left()
    while not front_is_clear() and not wall_on_right():
        turn_left()
        turn_left()
        turn_left()