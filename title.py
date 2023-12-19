from turtle import Turtle
import time

FONT = ('Courier', 14, 'normal')


class Title(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.waiting = True
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.color("white")
        self.write(f"SNAKE", align='center', font=('Courier', 48, 'bold'))
        self.goto(0, -50)
        self.write(f"Press space to start", align='center', font=('Courier', 24, 'normal'))

    def game_start(self):
        if self.waiting:
            self.clear()
            self.goto(0, 0)
            self.write("3", align='center', font=('Courier', 24, 'bold'))
            time.sleep(1)
            self.clear()
            self.write("2", align='center', font=('Courier', 24, 'bold'))
            time.sleep(1)
            self.clear()
            self.write("1", align='center', font=('Courier', 24, 'bold'))
            time.sleep(1)
            self.clear()
            self.waiting = False
