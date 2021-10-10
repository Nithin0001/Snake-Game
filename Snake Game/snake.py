from turtle import Turtle

STARTING_POS = [(-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.block = []
        self.create_snake()
        self.head = self.block[0]

    def create_snake(self):
        head = Turtle("square")
        head.penup()
        head.color("white")
        self.block.append(head)
        for pos in STARTING_POS:
            self.add_block(pos)

    def add_block(self, pos):
        new_block = Turtle("square")
        new_block.penup()
        new_block.color("black")
        new_block.goto(pos)
        self.block.append(new_block)

    def extend(self):
        self.add_block(self.block[-1].position())

    def move(self):
        for block_num in range(len(self.block) - 1, 0, -1):
            new_x = self.block[block_num - 1].xcor()
            new_y = self.block[block_num - 1].ycor()
            self.block[block_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
