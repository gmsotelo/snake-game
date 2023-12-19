from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    # Create the snake body
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setpos(position)
            self.segments.append(new_segment)

    # Add a new segment
    def extend(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_pos = self.segments[len(self.segments) - 1].position()
        self.segments.append(new_segment)
        self.segments[len(self.segments) - 1].goto(new_pos)

    # Constantly move snake forward
    def move(self):
        for seg_num in range((len(self.segments) - 1), 0, -1):
            new_pos = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(new_pos)
        self.head.forward(20)

    def reset(self):
        for seg in self.segments:
            seg.setpos(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # Move snake up
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    # Move snake up
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    # Move snake left
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    # Move snake right
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
