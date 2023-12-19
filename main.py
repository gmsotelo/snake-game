from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
from title import Title
from again import Again
import time

# Default parameters for game
WIDTH = 700
HEIGHT = 650

# Set up the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
scoreboard = Scoreboard()


def play():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    food = Food()
    scoreboard.create_borders()

    # Draw Title screen
    title = Title(WIDTH, HEIGHT)
    screen.onkeypress(title.game_start, "space")
    while title.waiting:
        screen.update()

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 230 or snake.head.ycor() < -230:
            game_is_on = False
            time.sleep(1)
            Again()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                time.sleep(1)
                Again()

    # Start a new game or close
    if not game_is_on:
        screen.onkey(play_again, "y")
        screen.onkey(exit_game, "n")


def play_again():
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)
    scoreboard.reset()
    snake.reset()
    play()


def exit_game():
    exit()


# Plays the game
play()

screen.exitonclick()
