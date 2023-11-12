from turtle import Turtle, Screen


class Snake:

    def __init__(self):
        screen = Screen()
        self.all_turtles = []
        x_positions = [0, -20, -40]
        for turtle_index in range(0, 3):
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(x=x_positions[turtle_index], y=0)
            self.all_turtles.append(new_turtle)
        print(self.all_turtles)
        screen.update()

    def move_forward(self):
        self.all_turtles[0].forward(10)
        self.all_turtles[1].forward(10)
        self.all_turtles[2].forward(10)

    def move_left(self):
        self.all_turtles[0].lt(90)
        self.all_turtles[1].forward(20)
        self.all_turtles[1].lt(90)
        self.all_turtles[0].forward(40)
        self.all_turtles[1].forward(20)
        self.all_turtles[2].forward(40)
        self.all_turtles[2].lt(90)

    def move_right(self):
        self.all_turtles[0].rt(90)
        self.all_turtles[1].forward(20)
        self.all_turtles[1].rt(90)
        self.all_turtles[0].forward(40)
        self.all_turtles[1].forward(20)
        self.all_turtles[2].forward(40)
        self.all_turtles[2].rt(90)

    def move(self):
        screen=Screen()
        for i in self.all_turtles:
            i.forward(20)
            screen.listen()
            screen.onkey(key="w", fun=self.move_forward)
            screen.onkey(key="a", fun=self.move_left)
            screen.onkey(key="d", fun=self.move_right)

            if i.xcor() > 300 or i.xcor() < -300:
                i.hideturtle()
                i.goto(x=-300, y=0)
                i.speed("fastest")
                i.showturtle()
                i.speed(10)
