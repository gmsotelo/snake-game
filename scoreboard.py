from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hi_score = 0
        self.goto(0, 250)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()

        if self.score > self.hi_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))

        with open("data.txt", mode="r") as file:
            high_score = int(file.read())
            self.hi_score = high_score

        self.write(f"Score: {self.score} High Score: {self.hi_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)

    def create_border(self, position, heading, forward):
        border = Turtle()
        border.color("white")
        border.hideturtle()
        border.penup()
        border.pensize(width=2)
        border.goto(position)
        border.pendown()
        border.setheading(heading)
        border.forward(forward)

    def create_borders(self):
        # Right Border
        self.create_border((290, 235), 270, 470)
        # Left Border
        self.create_border((-300, 235), 270, 470)
        # UP Border
        self.create_border((-300, 235), 0, 590)
        # Down Border
        self.create_border((-300, -235), 0, 590)
