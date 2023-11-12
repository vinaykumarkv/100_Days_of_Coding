from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=500)
turtle_list = []
color_list = ["red", "green", "yellow", "brown", "black", "orange", "maroon", "blue", "violet"]
pos_list = [(-230, -200), (-230, -150), (-230, -100), (-230, -50), (-230, -0), (-230, 50), (-230, 100), (-230, 150),
            (-230, 200)]
userbet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for i in range(0,8):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color_list[i])
    new_turtle.penup()
    new_turtle.goto(pos_list[i])
    turtle_list.append(new_turtle)
if userbet:
    race_on =True

while race_on == True:
    for turtle in turtle_list:
        # measuring if any turtle has moved more than 230 px
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == userbet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
