from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
RIGHT=0
UP=90
LEFT=180
DOWN=270
class Snake():
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment=Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def right (self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def up (self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def left (self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down (self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move(self):
        for seg_num in range(2, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].position())
        self.head.forward(MOVE_DISTANCE)

