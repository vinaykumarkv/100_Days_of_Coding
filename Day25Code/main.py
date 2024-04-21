import turtle
import pandas
import gc

screen = turtle.Screen()
screen.title("U. S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
states = pandas.read_csv("50_states.csv")
state_list = states["state"].tolist()
x_list = states["x"].tolist()
y_list = states["y"].tolist()

turtle.shape(image)
pen = turtle.Turtle()
pen.hideturtle()
Score = 0
lives = 1
correct_guess = []


def compare_state(a, state_list):
    for d in state_list:
        if a == d:
            print("pass")
            return True
    return False


game_is_on = True
answer = screen.textinput(title=f"Guess the state", prompt="What's the name of the state?").title()

while game_is_on and Score != 50:

    if compare_state(answer, state_list):
        correct_guess.append(answer)
        pen.penup()
        position = states[states["state"] == answer]
        pen.goto(int(position["x"]), int(position["y"]))
        pen.write(answer)
        Score += 1

    else:
        turtle.TK.messagebox.showinfo(title="The Turtle says:", message=f"Wrong Answer, Try again!!")
        lives -= 1
        if lives > 0:
            pass
        else:
            game_is_on = False
            break

    answer = screen.textinput(title=f"Your Score:{Score}/50", prompt="Guess another state?").title()
    print(answer)
not_guessed = []
not_guessedx = []
not_guessedy = []
#code to push states not guessed into csv file df = df.append(new_row, ignore_index=True)
for a in state_list:
    for b in correct_guess:

        if a == b:
            pass
        else:
            not_guessed.append(a)
            not_guessedx.append(x_list[state_list.index(a)])
            not_guessedy.append(y_list[state_list.index(a)])


if len(correct_guess) == 0:
    not_guessed = state_list
    not_guessedx = x_list
    not_guessedy = y_list

print(not_guessed)

data_initial = {
    "state": ["s"],
    "x": [0],
    "y": [0]
}


new_dataframe = pandas.DataFrame(data_initial)
print(new_dataframe)
for i in range(0, len(not_guessed)):
    not_guessed_states = states[states["state"] == not_guessed[i]]
    new_row = {"state":not_guessed[i], "x":str(not_guessedx[i]), "y":str(not_guessedy[i])}
    # new_dataframe = new_dataframe.append(new_row, ignore_index = True)
    new_dataframe.loc[len(new_dataframe)] = new_row



new_dataframe.to_csv("Unguessed_Sates.csv")

# turtle.mainloop()

screen.exitonclick()
