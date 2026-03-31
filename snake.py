from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        snake_segment.speed("fastest")
        self.snake_list.append(snake_segment)

    def reset_snake(self):
        self.snake_list.clear()
        self.create_snake()

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self):
        for n in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[n - 1].xcor()
            new_y = self.snake_list[n - 1].ycor()

            self.snake_list[n].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
